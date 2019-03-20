import random

# Create a rock/paper/scissors REPL loop
# Have a computer AI to play against us
# Keep track of the score
# Rules: r beats s, s beats p, p beats r

wins = 0
losses = 0
ties = 0


def compare_answers(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 0
    elif (player_choice == "r" and computer_choice == "s") or  \
         (player_choice == "p" and computer_choice == "r") or  \
         (player_choice == "s" and computer_choice == "p"):
        return 1
    else:
        return -1


class Opponent:
    _choices = ['r', 'p', 's']

    def __init__(self):
        pass

    def get_choice(self):
        return self._choices[random.randrange(3)]


class RockOpponent(Opponent):
    def __init__(self):
        pass

    def get_choice(self):
        random_num = random.random()
        if random_num < 0.8:
            return "r"
        elif random_num < 0.9:
            return "p"
        else:
            return "s"


opponent = RockOpponent()
while True:
    print(f"Score: {wins} - {losses} - {ties}")
    cmd = input("\nChoose r/p/s: ")
    # AI picks a random choice from r/p/s
    ai_choice = opponent.get_choice()
    print(f"Computer chose {ai_choice}")
    results = compare_answers(cmd, ai_choice)
    if results == 1:
        wins += 1
        print("You win!")
    elif results == -1:
        losses += 1
        print("You lose")
    elif results == 0:
        ties += 1
        print("You tie")
    if cmd == "q":
        print("Goodbye!")
        break
