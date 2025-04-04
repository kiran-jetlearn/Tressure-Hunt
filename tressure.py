import random
grid = []


def initialize_grid():
  for i in range(5):
    row = []  # Temporary list to store elements of each row
    # Loop to create 5 columns
    for j in range(5):
        row.append('-')  # Append '-' to the row
    grid.append(row)  # Add the row to the grid
    # Create a 5x5 grid filled with '-'
  return grid

# Function to randomly place the treasure on the grid
def place_treasure():
    row = random.randint(0, 4)  # Random row between 0 and 4
    col = random.randint(0, 4)  # Random column between 0 and 4
    return row, col

# Function to give hints based on player's guess
def give_hint(treasure_row, treasure_col, guess_row, guess_col):
    if guess_row < treasure_row:
        return "Move down"
    elif guess_row > treasure_row:
        return "Move up"
    elif guess_col < treasure_col:
        return "Move right"
    elif guess_col > treasure_col:
        return "Move left"
    return "Congratulations! You found the treasure!"

# Function to play the game
def treasure_hunt():
    # Initialize the grid and treasure
    grid = initialize_grid()
    treasure_row, treasure_col = place_treasure()
    
    print("Welcome to the Treasure Hunt Game!")
    attempts = 0  # Initialize the attempt counter

    # Start the game loop
    while True:
        # Show the grid to the player
        print("\nCurrent Grid:")
        for row in grid:
            print(" ".join(row))
        
        # Get player input for row and column guess
        try:
            guess_row = int(input("Enter the row number (0-4): "))
            guess_col = int(input("Enter the column number (0-4): "))
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 4.")
            continue
        
        # Ensure the guess is within bounds
        if guess_row not in range(5) or guess_col not in range(5):
            print("Invalid input. Please choose a row and column between 0 and 4.")
            continue
        
        # Increment the attempt counter
        attempts += 1

        # Check if the guess is correct
        if guess_row == treasure_row and guess_col == treasure_col:
            print("Congratulations! You found the treasure in {} attempts.".format(attempts))
            break
        else:
            # Provide a hint
            hint = give_hint(treasure_row, treasure_col, guess_row, guess_col)
            print("Hint: {}".format(hint))

# Run the Treasure Hunt Game
treasure_hunt()
