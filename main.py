from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

bid_history = {}


def find_highest_bidder(bidding_record):
  largestbid = 0
  winner = ""
  for bid in bidding_record:
    current_bid = bidding_record[bid]
    #print(f"Current bid is {current_bid}")
    if int(current_bid) > int(largestbid):
      largestbid = current_bid
      winner = bid
  print(f"{winner} is the winning bidder, with a bid of £{largestbid}")
  

print(logo)
print("Welcome to he secret auction program.")

Ask_again = True

while Ask_again == True:
  name = input("What is your name?: ")
  price = input("What is your bid?: £")
  bid_history[name] = price
  repeat = input("Add another members bid? Yes or No: ")
  if repeat.lower() == "no":
    Ask_again = False
  else: 
    clear()

find_highest_bidder(bid_history)





