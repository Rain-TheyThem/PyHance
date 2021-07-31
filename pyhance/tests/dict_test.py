import unittest
import sys

sys.path.append("./pyhance")
import pyhance.dict as dictionary


class TestDict(unittest.TestCase):
    def test_item_at_key_1(self):
        dict_input = dictionary.dictionary({
            "abate": "a",
            "bat": "b",
            "catch": "c"
        })
        dict_index = 0
        result = dict_input.item_at(dict_index)

        self.assertEqual(
            result, "abate",
            f"item_at() method doesn't work properly. It returns {result}")

    def test_item_at_key_2(self):
        dict_input = dictionary.dictionary({
            "abate": "a",
            "bat": "b",
            "catch": "c"
        })
        dict_index = 1
        result = dict_input.item_at(dict_index)

        self.assertEqual(
            result, "bat",
            f"item_at() method doesn't work properly. It returns {result}")

    def test_item_at_key_3(self):
        dict_input = dictionary.dictionary({
            "abate": "a",
            "bat": "b",
            "catch": "c"
        })
        dict_index = 2
        result = dict_input.item_at(dict_index)

        self.assertEqual(
            result, "catch",
            f"item_at() method doesn't work properly. It returns {result}")
    
    def test_item_at_value_1(self):
        dict_input = dictionary.dictionary({
            "abate": "a",
            "bat": "b",
            "catch": "c"
        })
        dict_index = 0
        result = dict_input.item_at(dict_index, item_type="value")

        self.assertEqual(
            result, "a",
            f"item_at() method doesn't work properly. It returns {result}")
    
    def test_item_at_value_2(self):
        dict_input = dictionary.dictionary({
            "abate": "a",
            "bat": "b",
            "catch": "c"
        })
        dict_index = 1
        result = dict_input.item_at(dict_index, item_type="value")

        self.assertEqual(
            result, "b",
            f"item_at() method doesn't work properly. It returns {result}")
    
    def test_item_at_value_3(self):
        dict_input = dictionary.dictionary({
            "abate": "a",
            "bat": "b",
            "catch": "c"
        })
        dict_index = 2
        result = dict_input.item_at(dict_index, item_type="value")

        self.assertEqual(
            result, "c",
            f"item_at() method doesn't work properly. It returns {result}")
    
    def test_item_at_pair_1(self):
        dict_input = dictionary.dictionary({
            "abate": "a",
            "bat": "b",
            "catch": "c"
        })
        dict_index = 0
        result = dict_input.item_at(dict_index, item_type="pair")

        self.assertEqual(
            result, {"abate": "a"},
            f"item_at() method doesn't work properly. It returns {result}")
    
    def test_item_at_pair_2(self):
        dict_input = dictionary.dictionary({
            "abate": "a",
            "bat": "b",
            "catch": "c"
        })
        dict_index = 1
        result = dict_input.item_at(dict_index, item_type="pair")

        self.assertEqual(
            result, {"bat": "b"},
            f"item_at() method doesn't work properly. It returns {result}")
    
    def test_item_at_pair_3(self):
        dict_input = dictionary.dictionary({
            "abate": "a",
            "bat": "b",
            "catch": "c"
        })
        dict_index = 2
        result = dict_input.item_at(dict_index, item_type="pair")

        self.assertEqual(
            result, {"catch": "c"},
            f"item_at() method doesn't work properly. It returns {result}")

    def test_index_of_key_1(self):
        dict_input = dictionary.dictionary({
            "definition": "d",
            "eloquent": "e",
            "fun": "f"
        })
        dict_key = "definition"
        result = dict_input.index_of(dict_key)

        self.assertEqual(
            result, 0,
            f"index_of() method doesn't work properly. It returns {result}")
    
    def test_index_of_key_2(self):
        dict_input = dictionary.dictionary({
            "definition": "d",
            "eloquent": "e",
            "fun": "f"
        })
        dict_key = "eloquent"
        result = dict_input.index_of(dict_key)

        self.assertEqual(
            result, 1,
            f"index_of() method doesn't work properly. It returns {result}")
    
    def test_index_of_key_3(self):
        dict_input = dictionary.dictionary({
            "definition": "d",
            "eloquent": "e",
            "fun": "f"
        })
        dict_key = "fun"
        result = dict_input.index_of(dict_key)

        self.assertEqual(
            result, 2,
            f"index_of() method doesn't work properly. It returns {result}")
    
    def test_index_of_value_1(self):
        dict_input = dictionary.dictionary({
            "definition": "d",
            "eloquent": "e",
            "fun": "f"
        })
        dict_value = "d"
        result = dict_input.index_of(dict_value, item_type="value")

        self.assertEqual(
            result, 0,
            f"index_of() method doesn't work properly. It returns {result}")
    
    def test_index_of_value_2(self):
        dict_input = dictionary.dictionary({
            "definition": "d",
            "eloquent": "e",
            "fun": "f"
        })
        dict_value = "e"
        result = dict_input.index_of(dict_value, item_type="value")

        self.assertEqual(
            result, 1,
            f"index_of() method doesn't work properly. It returns {result}")
    
    def test_index_of_value_3(self):
        dict_input = dictionary.dictionary({
            "definition": "d",
            "eloquent": "e",
            "fun": "f"
        })
        dict_value = "f"
        result = dict_input.index_of(dict_value, item_type="value")

        self.assertEqual(
            result, 2,
            f"index_of() method doesn't work properly. It returns {result}")
    
    def test_index_of_pair_1(self):
        dict_input = dictionary.dictionary({
            "great": "g",
            "hello": "h",
            "idiosyncrasy": "i"
        })
        dict_pair = {"great": "g"}
        result = dict_input.index_of(dict_pair, item_type="pair")

        self.assertEqual(
            result, 0,
            f"index_of() method doesn't work properly. It returns {result}")
    
    def test_index_of_pair_2(self):
        dict_input = dictionary.dictionary({
            "great": "g",
            "hello": "h",
            "idiosyncrasy": "i"
        })
        dict_pair = {"hello": "h"}
        result = dict_input.index_of(dict_pair, item_type="pair")

        self.assertEqual(
            result, 1,
            f"index_of() method doesn't work properly. It returns {result}")
    
    def test_index_of_pair_3(self):
        dict_input = dictionary.dictionary({
            "great": "g",
            "hello": "h",
            "idiosyncrasy": "i"
        })
        dict_pair = {"idiosyncrasy": "i"}
        result = dict_input.index_of(dict_pair, item_type="pair")

        self.assertEqual(
            result, 2,
            f"index_of() method doesn't work properly. It returns {result}")


if __name__ == "__main__":
    unittest.main()