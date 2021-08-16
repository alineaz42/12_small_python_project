import random


def play():
    user = input(
        "r of forck, p for paper, s for scissors or q to quite:  ")
    computer = random.choice(["r", "s", "p"])
    if user == computer:
        return f"Is's a tie! you chose {user} computer {computer}"
    # r>s,s>p,p>r

    elif is_win(user, computer):
        return f"You won! computer chose {computer}"

    else:
        return f"You lose! computer chose {computer}"


def is_win(player, opponent):
    # r>s,s>p,p>r
    if (player == "r" and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True


print(play())
