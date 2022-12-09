# Rock Paper Scissors
# a hand game originating from China, usually played between two people,
# in which each player simultaneously forms one of three shapes with an
# outstretched hand. These shapes are "rock" (a closed fist), "paper" 
# (a flat hand), and "scissors" (a fist with the index finger and middle 
# finger extended, forming a V). "Scissors" is identical to the 
# two-fingered V sign (also indicating "victory" or "peace") except 
# that it is pointed horizontally instead of being held upright in the 
# air.

# Author: Alliyson Bonner
# Github: https://github.com/alliysonbonner
# Linkedin: https://www.linkedin.com/in/alliyson
# Email: alliyson.bonner@gmail.com
# Date: December 07 2022


# Import Library: random
import random

def is_win(player, opponent):
  """is_win determines if the player beats the opponent or not.

     In this game rock beat scissors, scissors beat paper, and
     paper beats rock.
  
  Args:
      player(str): This is the choice that the human player 
      made in the game. For rock the string is 'r', for scissor
      the string is 's' and for paper the string is 'p'.
      
      opponent(str): This is the choice that the computer made 
      during the game. For rock the string is 'r', for scissor
      the string is 's' and for paper the string is 'p'.
      
  Returns(bool):
      True if the player beats the opponent. False if the
      opponent beats the player.
  """
  game_state = (player, opponent)
  return game_state == ('r', 's') or game_state == ('s', 'p') or game_state == ('p', 'r')
  
  
def play():
  """play starts the game of rock paper scissors

  Returns(str):
      tells whether or not you won the game.
  """
  # Select r, p, or s for the user and computer section in the game 
  user_choice = input("'r' for rock, 'p' for paper, 's' for scissors:\n")
  computer_choice = random.choice(['r', 'p', 's'])
	
  # returns the game results depending on if it is a tie, win, or loss.
  if user_choice == computer_choice:
    return 'It\'s a tie'
  
  elif is_win(user_choice, computer_choice):
    return 'You Won!'
  
  return 'HaHaHaHa, You Lost!'

if __name__ == "__main__":
  # Welcome players to the game
  print("Welcome to Rock! Paper! Scissors!")
  # Call funtion to start game
  game_results = play()
  # Display results: tied, won, or lost
  print(game_results)