import unittest
from unittest.mock import patch

import main


class MyTestCase(unittest.TestCase):

    def test_short_line(self):
        fake_args = [None, "12345"]
        with unittest.mock.patch('sys.argv', fake_args):
            self.assertEqual(main.function()[0], main.function()[1])

    def test_symbols(self):
        fake_args = [None, "!@#$%^&*()[]{}\|;:,./<>?~`"]
        with unittest.mock.patch('sys.argv', fake_args):
            self.assertEqual('!@#$%^&*()[]{}\|;:,./<>?~', main.function()[1])

    def test_no_spaces(self):
        fake_args = [None, "Resultshouldcontainonefunctionasetofteststotestfunctionandinstructiononhowtocompileit"]
        with unittest.mock.patch('sys.argv', fake_args):
            self.assertEqual('Resultshouldcontainonefun', main.function()[1])


if __name__ == '__main__':
    unittest.main()
