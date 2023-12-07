import pandas as pd

hand_types = {(5,): 7, (4,1): 6, (3,2): 5, (3,1,1): 4, (2,2,1): 3, (2,1,1,1): 2, (1,1,1,1,1): 1}
card_values = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}

ranks = []
with open('07/input.txt') as f:
    for line in f:
        hand, bid = line.split()
        x = pd.Series([card_values[v] if v.isalpha() else int(v) for v in hand ])
        card_counts = x.value_counts()
        hand_type = tuple(card_counts.tolist())

        h = [card_values[card] if card.isalpha() else int(card) for card in hand]
        h.insert(0, hand_types[hand_type])
        h.append(int(bid))

        ranks.append(tuple(h))

res = 0
for i, hand in enumerate(sorted(ranks)):
    res += hand[-1] * (i+1)

print('ANSWER PART A: ', res)


hand_types = {(5,): 7, (4,1): 6, (3,2): 5, (3,1,1): 4, (2,2,1): 3, (2,1,1,1): 2, (1,1,1,1,1): 1}
card_values = {'A': 13, 'K': 12, 'Q': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1} 

ranks = []
c = 0
with open('07/input.txt') as f:
    for line in f:
        hand, bid = line.split()
        old_hand = hand

        x = pd.Series([card_values[v] if v.isalpha() else int(v) for v in hand ])
        card_counts = x.value_counts()

        try:
            num_jokers = card_counts.loc[1]

            if num_jokers == 5:
                hand = hand.replace('J', 'A')

            elif tuple(card_counts.tolist()) != (1,1,1,1,1) and tuple(card_counts.tolist()) != (2,2,1):
                if num_jokers == 2 and tuple(card_counts.tolist()) == (2,1,1,1):
                    card_counts = card_counts.sort_index(ascending=False)
                card_counts.pop(1)
                card_counts.loc[card_counts.first_valid_index()] += num_jokers
                
            else:
                if num_jokers != 2:
                    card_counts = card_counts.sort_index(ascending=False)
                card_counts.pop(1)
                card_counts.loc[card_counts.first_valid_index()] += num_jokers
           
        except:
            pass

        hand_type = tuple(sorted(card_counts.tolist(), reverse=True))
        hand = hand.replace('J', list(card_values.keys())[list(card_values.values()).index(card_counts.first_valid_index())])
        
        h = [card_values[card] if card.isalpha() else int(card) for card in old_hand]
        h.insert(0, hand_types[hand_type])
        h.append(int(bid))

        ranks.append(tuple(h))
        
res = 0
for i, hand in enumerate(sorted(ranks)):
    res += hand[-1] * (i+1)

print('ANSWER PART  B: ', res)

