import string

alphabets = string.ascii_uppercase

players_cards = {}
for i in range(3):
    players_cards[alphabets[i]] = [letter for letter in input()]

first_player = 'A'

next_player = first_player
while True:
    current_player = next_player
    current_player_cards = players_cards[current_player]
    if current_player_cards:
        next_player = current_player_cards[0].upper()
        current_player_cards.pop(0)
    else:
        winner = current_player
        print(winner)
        exit()
