from helpers import draw_board, check_turn, check_for_win
import os

spots = {
    1: '1',
    2: '2',
    3: '3',
    4: '4',
    5: '5',
    6: '6',
    7: '7',
    8: '8',
    9: '9',
}
# draw_board(spots)

# spots[1] = "X"
# print("Second draw:")
# draw_board(spots)

playing = True
complete = False
turn = 0
prev_turn = -1

while playing:
    # reset the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)

    # if an invalid turn occured, let the player know
    if prev_turn == turn:
        print("Invalid spot selected, please pick another.")
    prev_turn = turn

    print("Player " + str((turn % 2) + 1) +
          "'s turn: Pick your spot or press q to quit")
    # get the input from the player
    choice = input()
    if choice == 'q':
        playing = False
    # Check if the player give a number from 1-9
    elif str.isdigit(choice) and int(choice) in spots:
        if not spots[int(choice)] in {"X", "O"}:
            # Valid Input, update the board
            turn += 1
            spots[int(choice)] = check_turn(turn)

    # Check if the game has ended
    if check_for_win(spots):
        playing, complete = False, True
    if turn > 8:
        playing = False

# Update the board one last time.
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)
# If there was a winner, say who won
if complete:
    if check_turn(turn) == 'X':
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")
else:
    # Tie Game
    print("No Winner")

print("Thanks for playing!")
