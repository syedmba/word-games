#!/bin/bash

source set_env.sh

# List of valid game names
valid_games=("wordle" "hangman")

# Function to display help information
show_help() {
  echo "Usage: $0 <game_name> [--help]"
  echo
  echo "Available games:"
  for game in "${valid_games[@]}"; do
    echo "  - $game"
  done
  echo
  echo "Options:"
  echo "  --help   Display this help message"
}

# Check if the first argument is provided
if [ $# -eq 0 ]; then
  echo "Error: No game name provided."
  show_help
  exit 1
fi

# Get the game name
game_name="$1"

# Check if the game name is valid
if [[ ! " ${valid_games[@]} " =~ " ${game_name} " ]]; then
  echo "Error: Invalid game name '$game_name'."
  show_help
  exit 1
fi

# Check for optional help argument
if [ "$2" == "--help" ]; then
  show_help
  exit 0
fi

# Main script logic for the chosen game
echo "Launching $game_name..."

# Game-specific logic here

if [ $game_name == "wordle" ]; then
    python ./games/wordle.py
elif [ $game_name == "hangman" ]; then
    # echo "Not yet implemented... Play wordle?"
    python ./games/hangman.py
fi
