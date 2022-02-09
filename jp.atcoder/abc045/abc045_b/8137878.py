import string

alphabets = string.ascii_uppercase

players = {}
for i in range(3):
    players[alphabets[i]] = [letter for letter in input()]

first_player = 'A'

next_player = first_player
while True:
    current_player = next_player
    current_player_cards = players[current_player]
    if current_player_cards:
        next_player = current_player_cards[0].upper()
        current_player_cards.pop(0)
    else:
        winner = current_player
        print(winner)
        exit()
