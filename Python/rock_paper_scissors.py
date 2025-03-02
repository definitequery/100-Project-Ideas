#!/usr/bin/env python3

import random
from typing import Tuple, Literal, Dict, Optional


Hand = Literal['rock', 'paper', 'scissors']
Winner = Literal['player', 'computer', 'tie']


def get_computer_hand() -> Hand:
    """
    Generate a random hand choice for the computer.
    
    Returns:
        Hand: The computer's hand choice
    """
    choices: Tuple[Hand, ...] = ('rock', 'paper', 'scissors')
    return random.choice(choices)


def validate_player_input(player_input: str) -> Optional[Hand]:
    """
    Validate the player's input and convert to a standard hand.
    
    Args:
        player_input: The raw input from the player
    
    Returns:
        Optional[Hand]: The standardized hand or None if invalid
    """
    valid_inputs: Dict[str, Hand] = {
        'r': 'rock', 
        'rock': 'rock',
        'p': 'paper', 
        'paper': 'paper',
        's': 'scissors', 
        'scissors': 'scissors'
    }
    
    clean_input = player_input.lower().strip()
    return valid_inputs.get(clean_input)


def get_player_hand() -> Hand:
    """
    Get and validate the player's hand choice.
    
    Returns:
        Hand: The validated player hand choice
    """
    while True:
        player_input = input(
            "Enter your choice (r/rock, p/paper, s/scissors): "
        )
        
        hand = validate_player_input(player_input)
        if hand is not None:
            return hand
        
        print(
            "Invalid choice. Please enter 'r' or 'rock', "
            "'p' or 'paper', 's' or 'scissors'."
        )


def determine_winner(computer_hand: Hand, player_hand: Hand) -> Winner:
    """
    Determine the winner based on both hands.
    
    Args:
        computer_hand: The computer's hand choice
        player_hand: The player's hand choice
    
    Returns:
        Winner: The result of the round
    """
    if computer_hand == player_hand:
        return 'tie'
    
    winning_combinations: Dict[Hand, Hand] = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    
    return 'computer' if winning_combinations[computer_hand] == player_hand else 'player'


def display_result(computer_hand: Hand, player_hand: Hand, winner: Winner) -> None:
    """
    Display the result of a round.
    
    Args:
        computer_hand: The computer's hand
        player_hand: The player's hand
        winner: The winner of the round
    """
    print(f"\nComputer chose: {computer_hand}")
    print(f"You chose: {player_hand}")
    
    if winner == 'tie':
        print("It's a tie! Let's play again.\n")
    elif winner == 'player':
        print("You win!")
    else:
        print("Computer wins!")


def play_again() -> bool:
    """
    Ask the player if they want to play again.
    
    Returns:
        bool: True if the player wants to play again, False otherwise
    """
    try:
        response = input("\nDo you want to play again? (y/n): ").lower().strip()
        return response == 'y'
    except (KeyboardInterrupt, EOFError):
        return False


def play_game() -> None:
    """
    Main game function that orchestrates the rock-paper-scissors game.
    """
    print("Welcome to Rock, Paper, Scissors!")
    print("--------------------------------")
    
    try:
        while True:
            computer_hand = get_computer_hand()
            player_hand = get_player_hand()
            winner = determine_winner(computer_hand, player_hand)
            
            display_result(computer_hand, player_hand, winner)
            
            if winner != 'tie' and not play_again():
                print("Thanks for playing!")
                break
                
    except (KeyboardInterrupt, EOFError):
        print("\nGame interrupted. Thanks for playing!")


if __name__ == "__main__":
    play_game()