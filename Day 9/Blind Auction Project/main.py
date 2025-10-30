# Simple bidding program

# Function to find the highest bidder
import art
print(art.logo)
def find_highest_bidder(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

# Dictionary to store bids
bids = {}
continue_bidding = True

# Main bidding loop
while continue_bidding:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if should_continue == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == "yes":
        # Clears the screen (simulated by printing empty lines)
        print("\n" * 20)
