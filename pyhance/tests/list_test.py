import unittest
import sys

sys.path.append("./pyhance")
import pyhance.list as list_

class TestList(unittest.TestCase):
    def test_remove_all_trues(self):
        input_list = list_.list_([True, False, False, "Hello", 2, 3, "idiom", True, 34, 985, "Jammy Jobs"])
        removed_item = True
        removed_list = [False, False, "Hello", 2, 3, "idiom", 34, 985, "Jammy Jobs"]
        result = input_list.remove_all(removed_item)

        self.assertEquals(
            result, removed_list,
            f"remove_all() method doesn't work properly. It returns {result}"
        )