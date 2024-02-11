from problems.grid_challenge import select_gridChallenge
import unittest

class gridChallengeTest(unittest.TestCase):
    def test_give_uxf_vof_hmp_is_not_grid(self):
        prime_list = ['uxf','vof','hmp']
        is_grid = select_gridChallenge(prime_list)
        self.assertEqual(is_grid, 'NO')
    
    def test_give_vpvv_pvvv_vzzp_zzyy_is_grid(self):
        prime_list = ['vpvv','pvvv','vzzp','zzyy']
        is_grid = select_gridChallenge(prime_list)
        self.assertEqual(is_grid, 'YES')
    
    def test_give_ttt_zzz_zzz_is_not_grid(self):
        prime_list = ['ttt','zzz','zzz']
        is_grid = select_gridChallenge(prime_list)
        self.assertEqual(is_grid, 'NO')
    
    def test_give_zzzzzwz_zzzzzzw_wzzzzzz_zzwzzzz_zzyzzzz_zzzzyzz_zzzzzyz_is_not_grid(self):
        prime_list = ['zzzzzwz','zzzzzzw','wzzzzzz','zzwzzzz','zzyzzzz','zzzzyzz','zzzzzyz']
        is_grid = select_gridChallenge(prime_list)
        self.assertEqual(is_grid, 'NO')
    
    
    