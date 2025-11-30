def rps(p1, p2):
    if p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    if p1 == "scissors" and p2 == "rock":
        return "Player 2 won!"
    if p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    if p1 == "paper" and p2 == "scissors":
        return "Player 2 won!"
    if p1 == "rock" and p2 == "paper":
        return "Player 2 won!"
    if p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"

    return "Draw!"


player1 = input("digite p1")
player2 = input("digite p2")
r = rps("rock","rock" )
r2 = rps("scissors", "paper")
print(r)
