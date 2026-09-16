import unittest
from unittest.mock import patch
import io
import sys
from src.guessing_game import play_game

# We need to mock the input since play_game uses sys.stdin.readline
class TestGuessingGame(unittest.TestCase):

    @patch('sys.stdin.readline')
    def test_win_game(self, mock_stdin):
        # Simulate the user guessing the correct number on the first try
        # We mock random.randint to always return 42
        with patch('random.randint', return_value=42):
            # Sequence of inputs: 42 then empty string to break loop
            mock_stdin.side_effect = ["42\n", ""]

            # Capture stdout to verify the output
            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                play_game()
                output = fake_out.getvalue()
                self.assertIn("Congratulations!", output)
                self.assertIn("guessed the number 42", output)

    @patch('sys.stdin.readline')
    def test_lose_game(self, mock_stdin):
        # Simulate the user guessing wrong 10 times
        with patch('random.randint', return_value=42):
            # 10 wrong guesses, then empty string
            mock_stdin.side_effect = ["1\n"] * 10 + [""]

            with patch('sys.stdout', new=io.StringIO()) as fake_out:
                play_game()
                output = fake_out.getvalue()
                self.assertIn("Sorry, you've used all 10 attempts", output)
                self.assertIn("number I was thinking of was 42", output)

    @patch('sys.stdin.readline')
    def test_invalid_input(self, mock_stdin):
        # Test that the game handles non-integer inputs without crashing
        with patch('random.randint', return_value=42):
            # One invalid input, then the correct guess
            mock_stdin.side_effect = ["abc\n", "42\n", ""]

            with patch('sys.stdout', new=io.StringIO() ) as fake_out:
                play_game()
                output = fake_out.getvalue()
                self.assertIn("Please enter a valid number!", output)
                self.assertIn("Congratulations!", output)

if __name__ == "__main__":
    unittest.main()