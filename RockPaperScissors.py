import random

def is_win(player: str, opponent: str) -> bool:
    """Determines if the player beats the opponent or not.

    Args:
        player (str): The choice the human player made in the game.
            'r' for rock, 's' for scissors, and 'p' for paper.
        opponent (str): The choice the computer made in the game.
            'r' for rock, 's' for scissors, and 'p' for paper.

    Returns:
        bool: True if the player beats the opponent. False if the
            opponent beats the player.
    """
    return (player == 'r' and opponent == 's') or \
           (player == 's' and opponent == 'p') or \
           (player == 'p' and opponent == 'r')

def play() -> str:
    """Starts the game of rock, paper, scissors.

    Returns:
        str: The game result, whether it's a tie, win, or loss.
    """
    user_choice = input("Type 'r' for rock, 'p' for paper, 's' for scissors: ").lower()
    computer_choice = random.choice(['r', 'p', 's'])

    if user_choice == computer_choice:
        return 'It\'s a tie!'
    elif is_win(user_choice, computer_choice):
        return 'You won!'
    else:
        return 'You lost!'

if __name__ == '__main__':
    print('Welcome to Rock, Paper, Scissors!')
    game_result = play()
    print(game_result)
