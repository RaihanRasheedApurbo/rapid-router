#! /usr/bin/env python
"""Generate JS code from an ASDL description."""

# TO DO
# handle fields that have a type but no name

import os, sys

import asdl

TABSIZE = 4
MAX_COL = 80

def get_c_type(name):
    """Return a string for the C name of the type.

    This function special cases the default types provided by asdl:
    identifier, string, int, bool.
    """
    # XXX ack!  need to figure out where Id is useful and where string
    if isinstance(name, asdl.Id):
        name = name.value
    if name in asdl.builtin_types:
        return name
    else:
        return "%s_ty" % name

def reflow_lines(s, depth):
    """Reflow the line s indented depth tabs.

    Return a sequence of lines where no line extends beyond MAX_COL
    when properly indented.  The first line is properly indented based
    exclusively on depth * TABSIZE.  All following lines -- these are
    the reflowed lines generated by this function -- start at the same
    column as the first character beyond the opening { in the first
    line.
    """
    size = MAX_COL - depth * TABSIZE
    if len(s) < size:
        return [s]

    lines = []
    cur = s
    padding = ""
    while len(cur) > size:
        i = cur.rfind(' ', 0, size)
        # XXX this should be fixed for real
        if i == -1 and 'GeneratorExp' in cur:
            i = size + 3
        assert i != -1, "Impossible line %d to reflow: %r" % (size, s)
        lines.append(padding + cur[:i])
        if len(lines) == 1:
            # find new size based on brace
            j = cur.find('{', 0, i)
            if j >= 0:
                j += 2 # account for the brace and the space after it
                size -= j
                padding = " " * j
            else:
                j = cur.find('(', 0, i)
                if j >= 0:
                    j += 1 # account for the paren (no space after it)
                    size -= j
                    padding = " " * j
        cur = cur[i+1:]
    else:
        lines.append(padding + cur)
    return lines

def is_simple(sum):
    """Return True if a sum is a simple.

    A sum is simple if its types have no fields, e.g.
    unaryop = Invert | Not | UAdd | USub
    """
    for t in sum.types:
        if t.fields:
            return False
    return True


class EmitVisitor(asdl.VisitorBase):
    """Visit that emits lines"""

    def __init__(self, file):
        self.file = file
        super(EmitVisitor, self).__init__()

    def emit(self, s, depth, reflow=1):
        # XXX reflow long lines?
        if reflow:
            lines = reflow_lines(s, depth)
        else:
            lines = [s]
        for line in lines:
            line = (" " * TABSIZE * depth) + line + "\n"
            self.file.write(line)


class TypeDefVisitor(EmitVisitor):
    def visitModule(self, mod):
        for dfn in mod.dfns:
            self.visit(dfn)

    def visitType(self, type, depth=0):
        self.visit(type.value, type.name, depth)

    def visitSum(self, sum, name, depth):
        if is_simple(sum):
            self.simple_sum(sum, name, depth)

    def simple_sum(self, sum, name, depth):
        self.emit("/* ----- %s ----- */" % name, depth);
        for i in range(len(sum.types)):
            self.emit("/** @constructor */", depth);
            type = sum.types[i]
            self.emit("function %s() {}" % type.name, depth)
        self.emit("", depth)

    def visitProduct(self, product, name, depth):
        pass


class StructVisitor(EmitVisitor):
    """Visitor to generate typdefs for AST."""

    def visitModule(self, mod):
        for dfn in mod.dfns:
            self.visit(dfn)

    def visitType(self, type, depth=0):
        self.visit(type.value, type.name, depth)

    def visitSum(self, sum, name, depth):
        pass

    def visitConstructor(self, cons, depth):
        pass

    def visitField(self, field, depth):
        # XXX need to lookup field.type, because it might be something
        # like a builtin...
        ctype = get_c_type(field.type)
        name = field.name
        if field.seq:
            if field.type.value in ('cmpop',):
                self.emit("asdl_int_seq *%(name)s;" % locals(), depth)
            else:
                self.emit("asdl_seq *%(name)s;" % locals(), depth)
        else:
            self.emit("%(ctype)s %(name)s;" % locals(), depth)

    def visitProduct(self, product, name, depth):
        pass


class PrototypeVisitor(EmitVisitor):
    """Generate function prototypes for the .h file"""

    def visitModule(self, mod):
        for dfn in mod.dfns:
            self.visit(dfn)

    def visitType(self, type):
        self.visit(type.value, type.name)

    def visitSum(self, sum, name):
        if is_simple(sum):
            pass # XXX
        else:
            for t in sum.types:
                self.visit(t, name, sum.attributes)

    def get_args(self, fields):
        """Return list of C argument into, one for each field.

        Argument info is 3-tuple of a C type, variable name, and flag
        that is true if type can be NULL.
        """
        args = []
        unnamed = {}
        for f in fields:
            if f.name is None:
                name = f.type
                c = unnamed[name] = unnamed.get(name, 0) + 1
                if c > 1:
                    name = "name%d" % (c - 1)
            else:
                name = f.name
            # XXX should extend get_c_type() to handle this
            if f.seq:
                if f.type.value in ('cmpop',):
                    ctype = "asdl_int_seq *"
                else:
                    ctype = "asdl_seq *"
            else:
                ctype = get_c_type(f.type)
            args.append((ctype, name, f.opt or f.seq))
        return args

    def visitConstructor(self, cons, type, attrs):
        args = self.get_args(cons.fields)
        attrs = self.get_args(attrs)
        ctype = get_c_type(type)
        self.emit_function(cons.name, ctype, args, attrs)

    def emit_function(self, name, ctype, args, attrs, union=1):
        args = args + attrs
        if args:
            argstr = ", ".join(["%s %s" % (atype, aname)
                                for atype, aname, opt in args])
            argstr += ", PyArena *arena"
        else:
            argstr = "PyArena *arena"
        margs = "a0"
        for i in range(1, len(args)+1):
            margs += ", a%d" % i
        self.emit("#define %s(%s) _Py_%s(%s)" % (name, margs, name, margs), 0,
                reflow = 0)
        self.emit("%s _Py_%s(%s);" % (ctype, name, argstr), 0)

    def visitProduct(self, prod, name):
        self.emit_function(name, get_c_type(name),
                           self.get_args(prod.fields), [], union=0)


class FunctionVisitor(PrototypeVisitor):
    """Visitor to generate constructor functions for AST."""

    def emit_function(self, name, ctype, args, attrs, union=1):
        def emit(s, depth=0, reflow=1):
            self.emit(s, depth, reflow)
        argstr = ", ".join(["/* {%s} */ %s" % (atype, aname)
                            for atype, aname, opt in args + attrs])
        emit("/** @constructor */")
        emit("function %s(%s)" % (name, argstr))
        emit("{")
        for argtype, argname, opt in args:
            # XXX hack alert: false is allowed for a bool
            if not opt and not (argtype == "bool" or argtype == "int"):
                emit("goog.asserts.assert(%s !== null && %s !== undefined);" % (argname, argname), 1)

        if union:
            self.emit_body_union(name, args, attrs)
        else:
            self.emit_body_struct(name, args, attrs)
        emit("return this;", 1)
        emit("}")
        emit("")


    def emit_body_union(self, name, args, attrs):
        def emit(s, depth=0, reflow=1):
            self.emit(s, depth, reflow)
        for argtype, argname, opt in args:
            emit("this.%s = %s;" % (argname, argname), 1)
        for argtype, argname, opt in attrs:
            emit("this.%s = %s;" % (argname, argname), 1)

    def emit_body_struct(self, name, args, attrs):
        def emit(s, depth=0, reflow=1):
            self.emit(s, depth, reflow)
        for argtype, argname, opt in args:
            emit("this.%s = %s;" % (argname, argname), 1)
        assert not attrs

class PickleVisitor(EmitVisitor):

    def visitModule(self, mod):
        for dfn in mod.dfns:
            self.visit(dfn)

    def visitType(self, type):
        self.visit(type.value, type.name)

    def visitSum(self, sum, name):
        pass

    def visitProduct(self, sum, name):
        pass

    def visitConstructor(self, cons, name):
        pass

    def visitField(self, sum):
        pass


def cleanName(name):
    name = str(name)
    if name[-1] == "_": return name[:-1]
    return name

class FieldNamesVisitor(PickleVisitor):

    """note that trailing comma is bad in IE so we have to fiddle a bit to avoid it"""

    def visitProduct(self, prod, name):
        if prod.fields:
            self.emit('%s.prototype._astname = "%s";' % (name, cleanName(name)), 0)
            self.emit("%s.prototype._fields = [" % name,0)
            c = 0
            for f in prod.fields:
                c += 1
                self.emit('"%s", function(n) { return n.%s; }%s' % (f.name, f.name, "," if c < len(prod.fields) else ""), 1)
            self.emit("];", 0)

    def visitSum(self, sum, name):
        if is_simple(sum):
            for t in sum.types:
                self.emit('%s.prototype._astname = "%s";' % (t.name, cleanName(t.name)), 0)
                self.emit('%s.prototype._isenum = true;' % (t.name), 0)
        else:
            for t in sum.types:
                self.visitConstructor(t, name)

    def visitConstructor(self, cons, name):
        self.emit('%s.prototype._astname = "%s";' % (cons.name, cleanName(cons.name)), 0)
        self.emit("%s.prototype._fields = [" % cons.name, 0)
        if cons.fields:
            c = 0
            for t in cons.fields:
                c += 1
                self.emit('"%s", function(n) { return n.%s; }%s' % (t.name, t.name, "," if c < len(cons.fields) else ""), 1)
        self.emit("];",0)

_SPECIALIZED_SEQUENCES = ('stmt', 'expr')

def find_sequence(fields, doing_specialization):
    """Return True if any field uses a sequence."""
    for f in fields:
        if f.seq:
            if not doing_specialization:
                return True
            if str(f.type) not in _SPECIALIZED_SEQUENCES:
                return True
    return False

def has_sequence(types, doing_specialization):
    for t in types:
        if find_sequence(t.fields, doing_specialization):
            return True
    return False


class ChainOfVisitors:
    def __init__(self, *visitors):
        self.visitors = visitors

    def visit(self, object):
        for v in self.visitors:
            v.visit(object)
            v.emit("", 0)

common_msg = "/* File automatically generated by %s. */\n\n"

def main(asdlfile, outputfile):
    argv0 = sys.argv[0]
    components = argv0.split(os.sep)
    argv0 = os.sep.join(components[-2:])
    auto_gen_msg = common_msg % argv0
    mod = asdl.parse(asdlfile)
    if not asdl.check(mod):
        sys.exit(1)

    f = open(outputfile, "wb")

    f.write(auto_gen_msg)
    c = ChainOfVisitors(TypeDefVisitor(f),
                        )
    c.visit(mod)

    f.write("\n"*5)
    f.write("/* ---------------------- */\n")
    f.write("/* constructors for nodes */\n")
    f.write("/* ---------------------- */\n")
    f.write("\n"*5)
    v = ChainOfVisitors(
        FunctionVisitor(f),
        FieldNamesVisitor(f),
        )
    v.visit(mod)

    f.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print "usage: asdl_js.py input.asdl output.js"
        raise SystemExit()
    main(sys.argv[1], sys.argv[2])
