from unittest import TestCase, main
from Handshake import no_of_handshakes


class TestHandshake(TestCase):
# Test outputs that should give zero
    def test_negative(self):
        expected = 0
        result = no_of_handshakes(-10)
    def test_zero(self):
        expected = 0
        result = no_of_handshakes(0)
        self.assertEqual(expected, result)
    def test_one(self):
        expected = 0
        result = no_of_handshakes(1)
        self.assertEqual(expected, result)
# Test first output to give an answer
    def test_two(self):
        expected = 1
        result = no_of_handshakes(2)
        self.assertEqual(expected, result)
# Test a larger output
    def test_large_number(self):
        expected = 190
        result = no_of_handshakes(20)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    main()
