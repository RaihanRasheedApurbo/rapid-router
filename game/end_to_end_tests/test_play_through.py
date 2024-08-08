from .base_game_test import BaseGameTest


class TestPlayThrough(BaseGameTest):
    def setUp(self):
        self.login_once()

    def _complete_episode(self, episode_number, level_number, **kwargs):
        page = self.go_to_episode(episode_number)
        self.complete_and_check_level(level_number, page, **kwargs)

    def _complete_level(self, level_number, **kwargs):
        page = self.go_to_level(level_number)
        self.complete_and_check_level(level_number, page, **kwargs)

    def test_episode_01(self):
        self._complete_episode(1, 1, check_algorithm_score=False)

    def test_level_001(self):
        self._complete_level(1, check_algorithm_score=False)

    def test_level_002(self):
        self._complete_level(2, check_algorithm_score=False)

    def test_level_003(self):
        self._complete_level(3, check_algorithm_score=False)

    def test_level_004(self):
        self._complete_level(4, check_algorithm_score=False)

    def test_level_005(self):
        self._complete_level(5, check_algorithm_score=False)

    def test_level_006(self):
        self._complete_level(6, check_algorithm_score=False)

    def test_level_007(self):
        self._complete_level(7, check_algorithm_score=False)

    def test_level_008(self):
        self._complete_level(8, check_algorithm_score=False)

    def test_level_009(self):
        self._complete_level(9, check_algorithm_score=False)

    def test_level_010(self):
        self._complete_level(10, check_algorithm_score=False)

    def test_level_011(self):
        self._complete_level(11, check_algorithm_score=False)

    def test_level_012(self):
        self._complete_level(12, check_algorithm_score=False)

    def test_episode_02(self):
        self._complete_episode(2, 13)

    def test_level_013(self):
        self._complete_level(13)

    def test_level_014(self):
        self._complete_level(14)

    def test_level_015(self):
        self._complete_level(15)

    def test_level_016(self):
        self._complete_level(16)

    def test_level_017(self):
        self._complete_level(17)

    def test_level_018(self):
        self._complete_level(18)

    def test_episode_03(self):
        self._complete_episode(3, 19)

    def test_level_019(self):
        self._complete_level(19)

    def test_level_020(self):
        self._complete_level(20)

    def test_level_021(self):
        self._complete_level(21)

    def test_level_022(self):
        self._complete_level(22)

    def test_level_023(self):
        self._complete_level(23)

    def test_level_024(self):
        self._complete_level(24)

    def test_level_025(self):
        self._complete_level(25)

    def test_level_026(self):
        self._complete_level(26)

    def test_level_027(self):
        self._complete_level(27)

    def test_level_028(self):
        self._complete_level(28)

    def test_episode_04(self):
        self._complete_episode(4, 29)

    def test_level_029(self):
        self._complete_level(29)

    def test_level_030(self):
        self._complete_level(30)

    def test_level_031(self):
        self._complete_level(31)

    def test_level_032(self):
        self._complete_level(32)

    def test_episode_05(self):
        self._complete_episode(5, 33)

    def test_level_033(self):
        self._complete_level(33)

    def test_level_034(self):
        self._complete_level(34)

    def test_level_035(self):
        self._complete_level(35)

    def test_level_036(self):
        self._complete_level(36)

    def test_level_037(self):
        self._complete_level(37)

    def test_level_038(self):
        self._complete_level(38)

    def test_level_039(self):
        self._complete_level(39, check_route_score=False)

    def test_level_040(self):
        self._complete_level(40)

    def test_level_041(self):
        self._complete_level(41)

    def test_level_042(self):
        self._complete_level(42)

    def test_level_043(self):
        self._complete_level(43)

    def test_episode_06(self):
        self._complete_episode(6, 44)

    def test_level_044(self):
        self._complete_level(44)

    def test_level_045(self):
        self._complete_level(45)

    def test_level_046(self):
        self._complete_level(46)

    def test_level_047(self):
        self._complete_level(47)

    def test_level_048(self):
        self._complete_level(48)

    def test_level_049(self):
        self._complete_level(49)

    def test_level_050(self):
        self._complete_level(50)

    def test_episode_07(self):
        self._complete_episode(7, 51, check_algorithm_score=False)

    def test_level_051(self):
        self._complete_level(51, check_algorithm_score=False)

    def test_level_052(self):
        self._complete_level(52, check_route_score=False)

    def test_level_053(self):
        self._complete_level(53)

    def test_level_054(self):
        self._complete_level(54, check_route_score=False)

    def test_level_055(self):
        self._complete_level(55)

    def test_level_056(self):
        self._complete_level(56)

    def test_level_057(self):
        self._complete_level(57)

    def test_level_058(self):
        self._complete_level(58)

    def test_level_059(self):
        self._complete_level(59, check_route_score=False)

    def test_level_060(self):
        self._complete_level(60, check_route_score=False)

    def test_episode_08(self):
        self._complete_episode(8, 61)

    def test_level_061(self):
        self._complete_level(61)

    def test_level_062(self):
        self._complete_level(62)

    def test_level_063(self):
        self._complete_level(63)

    def test_level_064(self):
        self._complete_level(64)

    def test_level_065(self):
        self._complete_level(65)

    def test_level_066(self):
        self._complete_level(66)

    def test_level_067(self):
        self._complete_level(67)

    def test_episode_09(self):
        self._complete_episode(9, 68, check_route_score=False)

    def test_level_068(self):
        self._complete_level(68, check_route_score=False)

    def test_level_069(self):
        self._complete_level(69, check_route_score=False)

    def test_level_070(self):
        self._complete_level(70, check_route_score=False)

    def test_level_071(self):
        self._complete_level(71)

    def test_level_072(self):
        self._complete_level(72)

    def test_level_073(self):
        self._complete_level(73)

    def test_level_074(self):
        self._complete_level(74, check_route_score=False)

    def test_level_075(self):
        self._complete_level(75)

    def test_level_076(self):
        self._complete_level(76, check_route_score=False)

    def test_level_077(self):
        self._complete_level(77, check_route_score=False)

    def test_level_078(self):
        self._complete_level(78, check_route_score=False)

    def test_level_079(self):
        self._complete_level(79, final_level=True)

    def test_episode_20(self):
        self._complete_episode(20, 1001, check_algorithm_score=False)
    
    def test_level_1001(self):
        self._complete_level(1001, check_algorithm_score=False)

    def test_level_1002(self):
        self._complete_level(1002, check_algorithm_score=False)

    def test_level_1003(self):
        self._complete_level(1003, check_algorithm_score=False)

    def test_level_1004(self):
        self._complete_level(1004, check_algorithm_score=False)

    def test_level_1005(self):
        self._complete_level(1005, check_algorithm_score=False)

    def test_level_1006(self):
        self._complete_level(1006, check_algorithm_score=False)

    def test_level_1007(self):
        self._complete_level(1007, check_algorithm_score=False)

    def test_level_1008(self):
        self._complete_level(1008, check_algorithm_score=False)

    def test_level_1009(self):
        self._complete_level(1009, check_algorithm_score=False)

    def test_level_1010(self):
        self._complete_level(1010, check_algorithm_score=False)

    def test_level_1011(self):
        self._complete_level(1011, check_algorithm_score=False)

    def test_level_1012(self):
        self._complete_level(1012, check_algorithm_score=False)

    def test_level_1013(self):
        self._complete_level(1013, check_algorithm_score=False)

    def test_episode_21(self):
        self._complete_episode(21, 1014, check_algorithm_score=False)

    def test_level_1014(self):
        self._complete_level(1014, check_algorithm_score=False)

    def test_level_1015(self):
        self._complete_level(1015, check_algorithm_score=False)

    def test_level_1016(self):
        self._complete_level(1016, check_algorithm_score=False)

    def test_level_1017(self):
        self._complete_level(1017, check_algorithm_score=False)

    def test_level_1018(self):
        self._complete_level(1018, check_algorithm_score=False)

    def test_level_1019(self):
        self._complete_level(1019, check_algorithm_score=False)

    def test_level_1020(self):
        self._complete_level(1020, check_algorithm_score=False)

    def test_level_1021(self):
        self._complete_level(1021, check_algorithm_score=False)

    def test_level_1022(self):
        self._complete_level(1022, check_algorithm_score=False)

    def test_level_1023(self):
        self._complete_level(1023, check_algorithm_score=False)

    def test_level_1024(self):
        self._complete_level(1024, check_algorithm_score=False)

    def test_level_1025(self):
        self._complete_level(1025, check_algorithm_score=False)

    def test_episode_22(self):
        self._complete_episode(22, 1026, check_algorithm_score=False)

    def test_level_1026(self):
        self._complete_level(1026, check_algorithm_score=False)

    def test_level_1027(self):
        self._complete_level(1027, check_algorithm_score=False)

    def test_level_1028(self):
        self._complete_level(1028, check_algorithm_score=False)

    def test_level_1029(self):
        self._complete_level(1029, check_algorithm_score=False)

    def test_level_1030(self):
        self._complete_level(1030, check_algorithm_score=False)

    def test_level_1031(self):
        self._complete_level(1031, check_algorithm_score=False)

    def test_level_1032(self):
        self._complete_level(1032, check_algorithm_score=False)

    def test_level_1033(self):
        self._complete_level(1033, check_algorithm_score=False)

    def test_level_1034(self):
        self._complete_level(1034, check_algorithm_score=False)

    def test_level_1035(self):
        self._complete_level(1035, check_algorithm_score=False)

    def test_level_1036(self):
        self._complete_level(1036, check_algorithm_score=False)

    def test_level_1037(self):
        self._complete_level(1037, check_algorithm_score=False)

    def test_level_1038(self):
        self._complete_level(1038, check_algorithm_score=False)

    def test_level_1039(self):
        self._complete_level(1039, check_algorithm_score=False)

    def test_level_1040(self):
        self._complete_level(1040, check_algorithm_score=False)

    def test_episode_25(self):
        self._complete_level(25, 1041, check_algorithm_score=False)
    
    def test_level_1041(self):
        self._complete_level(1041, check_algorithm_score=False)

    def test_level_1042(self):
        self._complete_level(1042, check_algorithm_score=False)

    def test_level_1043(self):
        self._complete_level(1043, check_algorithm_score=False)

    def test_level_1044(self):
        self._complete_level(1044, check_algorithm_score=False)

    def test_level_1045(self):
        self._complete_level(1045, check_algorithm_score=False)

    def test_level_1046(self):
        self._complete_level(1046, check_algorithm_score=False)

    def test_level_1047(self):
        self._complete_level(1047, check_algorithm_score=False)

    def test_level_1048(self):
        self._complete_level(1048, check_algorithm_score=False)

    def test_level_1049(self):
        self._complete_level(1049, check_algorithm_score=False)

    def test_episode_26(self):
        self._complete_episode(26, 1050, check_algorithm_score=False)

    def test_level_1050(self):
        self._complete_level(1050, check_algorithm_score=False)

    def test_level_1051(self):
        self._complete_level(1051, check_algorithm_score=False)

    def test_level_1052(self):
        self._complete_level(1052, check_algorithm_score=False)

    def test_level_1053(self):
        self._complete_level(1053, check_algorithm_score=False)

    def test_level_1054(self):
        self._complete_level(1054, check_algorithm_score=False)

    def test_level_1055(self):
        self._complete_level(1055, check_algorithm_score=False)

    def test_level_1056(self):
        self._complete_level(1056, check_algorithm_score=False)

    def test_level_1057(self):
        self._complete_level(1057, check_algorithm_score=False)

    def test_level_1058(self):
        self._complete_level(1058, check_algorithm_score=False)

    def test_level_1059(self):
        self._complete_level(1059, check_algorithm_score=False)

    def test_level_1060(self):
        self._complete_level(1060, check_algorithm_score=False)
