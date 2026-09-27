import unittest
from unittest.mock import patch
from src.fortune_teller import get_fortune

class TestFortuneTeller(unittest.TestCase):
    """Test suite for the fortune teller."""

    @patch('random.choice')
    def test_get_fortune(self, mock_choice):
        """Test that get_fortune returns a string from the list."""
        mock_choice.return_value = "Test fortune"
        self.assertEqual(get_fortune(), "Test fortune")

if __name__ == "__main__":
    unittest.main()
