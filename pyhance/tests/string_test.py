import unittest
import sys

sys.path.append("./pyhance")
import pyhance.string as string


class TestString(unittest.TestCase):
    # remove() tests
    def test_remove_lorem(self):
        string_input = string.string("Lorem ipsum")
        string_removal = "ipsum"
        result = string_input.remove(string_removal)

        self.assertEqual(
            result, string_input.replace(string_removal, ""),
            f"remove() method doesn't work properly. It returns {result}")

    def test_remove_e(self):
        string_input = string.string("Hayden helped Hayley win the Hackathon")
        string_removal = "e"
        result = string_input.remove(string_removal)

        self.assertEqual(
            result, string_input.replace(string_removal, ""),
            f"remove() method doesn't work properly. It returns {result}")

    def test_remove_2_es(self):
        string_input = string.string(
            "Harper hates how females are under-represented in computer science."
        )
        string_removal = "e"
        result = string_input.remove(string_removal, 2)

        self.assertEqual(
            result, string_input.replace(string_removal, "", 2),
            f"remove() method doesn't work properly. It returns {result}")

    # reverse() tests

    def test_reverse_lorem(self):
        string_input = string.string("Lorem ipsum")
        result = string_input.reverse()

        self.assertEqual(
            result, string_input[::-1],
            f"reverse() method doesn't work properly. It returns {result}")

    def test_reverse_hackathon(self):
        string_input = string.string("Hayden helped Hayley win the Hackathon")
        result = string_input.reverse()

        self.assertEqual(
            result, string_input[::-1],
            f"reverse() method doesn't work properly. It returns {result}")

    def test_reverse_cs_underrepresention(self):
        string_input = string.string(
            "Harper hates how females are under-represented in computer science."
        )
        result = string_input.reverse()

        self.assertEqual(
            result, string_input[::-1],
            f"reverse() method doesn't work properly. It returns {result}")


if __name__ == "__main__":
    unittest.main()