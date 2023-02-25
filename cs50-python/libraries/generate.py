import random

# # random.choice
# coin = random.choice(["heads", "tails"])
# print(coin)


# # random randint
# number = random.randint(1, 6)
# print(number)

# random.shuffle
cards = ["jack", "king", "queen"]
random.shuffle(cards)

for card in cards:
    print(card)