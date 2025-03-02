import unittest
from rock_paper_scissors import validate_player_input, determine_winner, get_computer_hand


class TestInputValidation(unittest.TestCase):
    """Tests for the input validation functionality."""
    
    def test_valid_rock_inputs(self):
        """Test that rock inputs are correctly recognized."""
        self.assertEqual(validate_player_input('r'), 'rock')
        self.assertEqual(validate_player_input('rock'), 'rock')
        self.assertEqual(validate_player_input('RoCk'), 'rock')
        self.assertEqual(validate_player_input('  rock  '), 'rock')
    
    def test_valid_paper_inputs(self):
        """Test that paper inputs are correctly recognized."""
        self.assertEqual(validate_player_input('p'), 'paper')
        self.assertEqual(validate_player_input('paper'), 'paper')
        self.assertEqual(validate_player_input('PAPER'), 'paper')
        self.assertEqual(validate_player_input(' paper '), 'paper')
    
    def test_valid_scissors_inputs(self):
        """Test that scissors inputs are correctly recognized."""
        self.assertEqual(validate_player_input('s'), 'scissors')
        self.assertEqual(validate_player_input('scissors'), 'scissors')
        self.assertEqual(validate_player_input('ScIsSoRs'), 'scissors')
        self.assertEqual(validate_player_input('  scissors  '), 'scissors')
    
    def test_invalid_inputs(self):
        """Test that invalid inputs return None."""
        self.assertIsNone(validate_player_input('invalid'))
        self.assertIsNone(validate_player_input(''))
        self.assertIsNone(validate_player_input('  '))
        self.assertIsNone(validate_player_input('rocks'))
        self.assertIsNone(validate_player_input('scissor'))  # singular form


class TestWinnerDetermination(unittest.TestCase):
    """Tests for the winner determination logic."""
    
    def test_tie_scenarios(self):
        """Test scenarios where the game results in a tie."""
        self.assertEqual(determine_winner('rock', 'rock'), 'tie')
        self.assertEqual(determine_winner('paper', 'paper'), 'tie')
        self.assertEqual(determine_winner('scissors', 'scissors'), 'tie')
    
    def test_player_win_scenarios(self):
        """Test scenarios where the player wins."""
        self.assertEqual(determine_winner('rock', 'paper'), 'player')
        self.assertEqual(determine_winner('paper', 'scissors'), 'player')
        self.assertEqual(determine_winner('scissors', 'rock'), 'player')
    
    def test_computer_win_scenarios(self):
        """Test scenarios where the computer wins."""
        self.assertEqual(determine_winner('paper', 'rock'), 'computer')
        self.assertEqual(determine_winner('scissors', 'paper'), 'computer')
        self.assertEqual(determine_winner('rock', 'scissors'), 'computer')


class TestRandomHandGeneration(unittest.TestCase):
    """Tests for the computer's random hand generation."""
    
    def test_get_computer_hand_returns_valid_choice(self):
        """Test that the computer always selects a valid hand."""
        valid_choices = ('rock', 'paper', 'scissors')

        for _ in range(50):
            hand = get_computer_hand()
            self.assertIn(hand, valid_choices)
    
    def test_get_computer_hand_distribution(self):
        """Test that the random hand selection has a reasonable distribution."""
        results = {'rock': 0, 'paper': 0, 'scissors': 0}

        for _ in range(1000):
            hand = get_computer_hand()
            results[hand] += 1

        for count in results.values():
            self.assertGreater(count, 200)


if __name__ == '__main__':
    unittest.main()