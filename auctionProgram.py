# from replit import clear
# HINT: You can call clear() to clear the output in the console.
from art import logo

bidding = {}
bidding_finished = False


def highest_bidder(bidding_record):
    highest_bid = 0
    winner = " "
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}.")


print(logo)
print("Welcome to the secret auction program")

while not bidding_finished:
    name = input("What is your name?: ")
    bid_price = int(input("Your bid amount? $"))
    bidding[name] = bid_price
    choice = input("Are there any other bidders?").lower()
    if choice == 'no':
        bidding_finished = True
        highest_bidder(bidding)
