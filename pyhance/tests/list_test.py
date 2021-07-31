import unittest
import sys

sys.path.append("./pyhance")
import pyhance.list as list_

class TestList(unittest.TestCase):
    def test_remove_all_trues(self):
        input_list = list_.list_([True, False, False, "Hello", 2, 3, "idiom", True, 34, 985, "Jammy Jobs"])
        removed_item = True
        removed_list = [False, False, "Hello", 2, 3, "idiom", 34, 985, "Jammy Jobs"]
        input_list.remove_all(removed_item)

        self.assertEqual(
            input_list, list_.list_(removed_list),
            f"remove_all() method doesn't work properly. It returns {input_list}"
        )
    def test_remove_all_falses(self):
        input_list = list_.list_([True, False, False, "Hello", 2, 3, "idiom", True, 34, 985, "Jammy Jobs"])
        removed_item = False
        removed_list = [True, "Hello", 2, 3, "idiom", True, 34, 985, "Jammy Jobs"]
        input_list.remove_all(removed_item)

        self.assertEqual(
            input_list, list_.list_(removed_list),
            f"remove_all() method doesn't work properly. It returns {input_list}"
        )

    def test_remove_all_hellos(self):
        input_list = list_.list_([True, False, False, "Hello", 2, 3, "idiom", True, 34, 985, "Jammy Jobs"])
        removed_item = "Hello"
        removed_list = [True, False, False, 2, 3, "idiom", True, 34, 985, "Jammy Jobs"]
        input_list.remove_all(removed_item)

        self.assertEqual(
            input_list, list_.list_(removed_list),
            f"remove_all() method doesn't work properly. It returns {input_list}"
        )

    def test_remove_all_2s(self):
        input_list = list_.list_([2, 1, 3, 2, 849, "3", "akjfgh", 2, 34, 2, "2"])
        removed_item = "Hello"
        removed_list = [1, 3, 849, "3", "akjfgh", 34, "2"]
        input_list.remove_all(removed_item)

        self.assertEqual(
            input_list, list_.list_(removed_list),
            f"remove_all() method doesn't work properly. It returns {input_list}"
        )

if __name__ == "__main__":
    unittest.main()