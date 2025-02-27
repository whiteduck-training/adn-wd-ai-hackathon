import unittest
from copilot import reverse_string


class TestReverseString(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "Olleh")
        self.assertEqual(reverse_string("world"), "Dlrow")
        self.assertEqual(reverse_string("Python"), "Nohtyp")
        self.assertEqual(reverse_string(""), "")
        self.assertEqual(reverse_string("a"), "A")


if __name__ == "__main__":
    unittest.main()
