import unittest
from matching_algorithm import find_matching_properties

class TestMatching(unittest.TestCase):
    def test_find_matching_properties(self):
        self.assertIsNotNone(find_matching_properties())
