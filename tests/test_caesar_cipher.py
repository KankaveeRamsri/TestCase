from problems.caesar_cipher import caesarCipher
import unittest

class CaesarCipher(unittest.TestCase):
    def test_give_middle_Outz_and_2_is_okffng_Qwvb(self):
        string = 'middle_Outz'
        num = 2
        encrypted = caesarCipher(string, num)
        self.assertEqual(encrypted, 'okffng_Qwvb')
    
    def test_give_Ciphering_and_26_is_Ciphering(self):
        string = 'Ciphering'
        num = 26
        encrypted = caesarCipher(string, num)
        self.assertEqual(encrypted, 'Ciphering')
    
    def test_give_159357lcfd_and_98_is_159357fwzy(self):
        string = '159357lcfd'
        num = 98
        encrypted = caesarCipher(string, num)
        self.assertEqual(encrypted, '159357fwzy')
    
    def test_give_www_dot_abc_dot_xy_and_87_is_fff_dot_jkl_dot_gh(self):
        string = 'www.abc.xy'
        num = 87
        encrypted = caesarCipher(string, num)
        self.assertEqual(encrypted, 'fff.jkl.gh')
    
    def test_give_string_and_45_is_answer(self):
        string = 'DNFjxo?b5h*5<LWbgs6?V5{3M].1hG)pv1VWq4(!][DZ3G)riSJ.CmUj9]7Gzl?VyeJ2dIPEW4GYW*scT8(vhu9wCr]q!7eyaoy.'
        num = 45
        encrypted = caesarCipher(string, num)
        self.assertEqual(encrypted, 'WGYcqh?u5a*5<EPuzl6?O5{3F].1aZ)io1OPj4(!][WS3Z)kbLC.VfNc9]7Zse?OrxC2wBIXP4ZRP*lvM8(oan9pVk]j!7xrthr.')