import unittest
from commands import start

class TestCommands(unittest.TestCase):
    def test_start(self):
        self.assertEqual(start(), 'Welcome to zapCORRETOR!')
