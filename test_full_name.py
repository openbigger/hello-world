#test case to test use function get_full_name in name.py
#运行之后会生成full_name.pyc，用来提高运行速度的编译文件，可删
import unittest
from full_name import get_full_name

class NameTestCase(unittest.TestCase):
    def test_first_last(self):
        full_name = get_full_name("janis","joplin")
        self.assertEqual(full_name,"Janis,Joplin")
    def test_middle(self):
        full_name = get_full_name("janis","joplin","maye")
        self.assertEqual(full_name,"Janis,Maye,Joplin")
unittest.main()