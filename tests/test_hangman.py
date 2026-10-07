"""
Unit tests for the Hangman game.
"""
import unittest
from unittest.mock import patch
import io
from src.hangman import play_hangman

class TestHangman(unittest.TestCase):
    """Test suite for the Hangman game logic."""

    @patch('sys.stdin.readline')
    def test_win_game(self, mock_stdin):
        """Test that the game recognizes a win when all letters are guessed."""
        # Mock get_secret_word to return "python"
        with patch('src.hangman.get_secret_word', return_value="python"):
            # Inputs: p, y, t, h, o, n then empty string
            mock_stdin.side_effect = ["p\n", "y\n", "t\n", "h\n", "o\n", "n\n", ""]

            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                result = play_hangman()
                output = fake_out.getvalue()
                self.assertTrue(result)
                self.assertIn("Congratulations!", output)
                self.assertIn("guessed the word: python", output)

    @patch('sys.stdin.readline')
    def test_lose_game(self, mock_stdin):
        """Test that the game recognizes a loss when attempts run out."""
        with patch('src.hangman.get_secret_word', return_value="python"):
            # 6 wrong guesses then empty string
            mock_stdin.side_effect = ["a\n", "b\n", "c\n", "d\n", "e\n", "f\n", ""]

            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                result = play_hangman()
                output = fake_out.getvalue()
                self.assertFalse(result)
                self.assertIn("Game over!", output)
                self.assertIn("secret word was: python", output)

    @patch('sys.stdin.readline')
    def test_invalid_input(self, mock_stdin):
        """Test that the game handles invalid inputs (too long or non-alpha)."""
        with patch('src.hangman.get_secret_word', return_value="python"):
            # Invalid inputs: "py" (too long), "1" (non-alpha), then the correct letters
            mock_stdin.side_effect = ["py\n", "1\n", "p\n", "y\n", "t\n", "h\n", "o\n", "n\n", ""]

            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                result = play_hangman()
                output = fake_out.getvalue()
                self.assertTrue(result)
                self.assertIn("Please enter a single letter!", output)

if __name__ == "__main__":
    unittest.main()
