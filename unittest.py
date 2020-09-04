import unittest

class TestMyProgram(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO' .isupper())
        self.assertFalse('Foo' .isupper())

if name == 'main':
    unittest.main()