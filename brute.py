"""Brute force calcultion of the 123-game"""
import random
from datetime import datetime
from matplotlib import pyplot as pp

# Base deck of cards. Color/suite is not considered. 
deck = list(range(1,14))*4

def is_winning_deck(deck):
    """Check if a deck is a winning deck. Divide the pack into intervals of three, starting from index 0, 1, and 2. Check that none of these packs have the corresponding number in them. """
    return not (
        any([card == 1 for card in deck[::3]])
        or any([card == 2 for card in deck[1::3]])
        or any([card == 3 for card in deck[2::3]])
    )

wins = 0
losses = 0
log_interval = 50_000

print(f'Running simulation')
start = datetime.now()
i = 0
# For plotting
x = []
y = []
while True:
    try: 
        if ((i+1)%log_interval==0):
            print(f'{(i+1)} rounds done, win percentage: {wins / (i+1) * 100}')
            x.append(i)
            y.append(wins / (i) * 100)
        random.shuffle(deck)
        if is_winning_deck(deck):
            wins+=1
            continue
        losses+=1 
        i += 1
    except KeyboardInterrupt:
        break
stop = datetime.now()
duration = stop - start
print(f'Simulation done in {duration.total_seconds()} seconds')
win_percentage = wins / i * 100
print(f'Win percentage for simulation was {win_percentage} %')
print(f'Rounds: {i}')
pp.plot(x, y)
pp.show()
