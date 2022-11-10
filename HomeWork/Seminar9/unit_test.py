import task_def as td
import unittest


class TestSplitFunctionFirst(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
#1
    def test_candy_bot_many_candy(self):
        self.assertTrue(1 <= td.candy_bot(100, 20) <= 20)
#2
    def test_candy_bot_few_candy(self):
        self.assertEqual(td.candy_bot(30, 40), 30)
#3
    def test_check_win_win(self):
        self.assertEqual(td.check_win(['О','О','О',4,5,6,7,8,9]),"О")
#4
    def test_check_win_continie(self):
        self.assertEqual(td.check_win(['О','О',3,4,5,6,7,8,9]),False)
#5
    def test_rle_encode(self):
        self.assertEqual(td.rle_encode('XXXSSSQADD'),'3X3S1Q1A2D')
#6
    def test_rle_decode(self):
        self.assertEqual(td.rle_decode('3X3S1Q1A2D'),'XXXSSSQADD')

class TestSplitFunctionSecond(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
#7
    def test_prime_multipliers_number(self):
        self.assertEqual(td.prime_multipliers_number(140),[2,2,5,7])
#8
    def test_view_uniq_elem_list(self):
        self.assertEqual(td.view_uniq_elem_list('235 52 5 5 52 234 55 235'),
                                                ['235','52','5','234','55'])
#9
    def test_matrix_add(self):
        self.assertEqual(td.Matrix([[1,3],[4,5]]).__add__
                        (td.Matrix([[2,2],[3,1]])).my_matrix,
                        [[3,5],[7,6]])
#10
    def test_matrix_str(self):
        self.assertEqual(td.Matrix([[1,3],[4,5]]).__str__(),'1 3 \n4 5 \n')


if __name__ == 'main':
    unittest.main()
