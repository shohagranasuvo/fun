import unittest
from unittest.mock import patch
from src.rock_paper_scissors import play

class TestRockPaperScissors(unittest.TestCase):
    """Test suite for the rock paper scissors game logic."""

    @patch('builtins.input', return_value='rock')
    @patch('random.choice', return_value='scissors')
    def test_win(self, mock_random, mock_input):
        """Test a winning scenario."""
        result = play()
        self.assertIn("You win!", result)

    @patch('builtins.input', return_value='rock')
    @patch('random.choice', return_value='paper')
    def test_lose(self, mock_random, mock_input):
        """Test a losing scenario."""
        self.assertIn("You lose!", play())

    @patch('builtins.input', return_value='rock')
    @patch('random.choice', return_value='rock')
    def test_tie(self, mock_random, mock_input):
        """Test a tie scenario."""
        self.assertIn("It's a tie!", play())

    @patch('builtins.input', return_value='lizard')
    def test_invalid(self, mock_input):
        """Test invalid input."""
        self.assertEqual(play(), "Invalid choice!")

if __name__ == "__main__":
    unittest.main()
