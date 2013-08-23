import numpy as np

SUITS = {'S':'spades','C':'clubs','D':'diamonds','H':'hearts'}
VALUES = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 
          'J':11, 'Q':12, 'K':13, 'A':14}
ROYAL_FLUSH = ['10','J','K','Q','A']

RANKS = {'one_pair':1,
         'two_pairs':2,
         'three_kind':3,
         'straight':4,
         'flush':5,
         'full_house':6,
         'four_kind':7,
         'straight_flush':8,
         'royal_flush':9}

def winner(hand1, hand2):
    #from IPython.core.debugger import Tracer
    #Tracer()()
    if hasattr(hand1, 'rank') and hasattr(hand2, 'rank'):
        if hand1.rank > hand2.rank:
            return hand1
        elif hand2.rank > hand1.rank:
            return hand2
        else:
            for key in RANKS.iterkeys():
                value = RANKS[key]
                if value == hand1.rank:
                    conflict = key
                else:
                    conflict = None
            if conflict == 'one_pair':
                if hand1.one_pair_value > hand2.one_pair_value:
                    return hand1
                elif hand2.one_pair_value > hand1.one_pair_value:
                    return hand2
                else:
                    value_to_pop = hand1.one_pair_value
                    for key in VALUES.iterkeys():
                        value = VALUES[key]
                        if value == value_to_pop:
                            key_to_pop = key
                            break
                    hand1_key_index = hand1.hand['values'].index(key_to_pop)
                    hand2_key_index = hand2.hand['values'].index(key_to_pop)
                    hand1.hand['values'].pop(hand1_key_index)
                    hand2.hand['values'].pop(hand2_key_index)
                    
                    hand1_key_index = hand1.hand['values'].index(key_to_pop)
                    hand2_key_index = hand2.hand['values'].index(key_to_pop)
                    hand1.hand['values'].pop(hand1_key_index)
                    hand2.hand['values'].pop(hand2_key_index)
                    
                    hand1_values = []
                    hand2_values = []
                    for value in hand1.hand['values']:
                        hand1_values.append(VALUES.get(value))
                    for value in hand2.hand['values']:
                        hand2_values.append(VALUES.get(value))
                    hand1_values.sort()
                    hand2_values.sort()
                    if hand1_values[len(hand1_values)-1] > hand2_values[len(hand2_values)-1]:
                        return hand1
                    return hand2
            
            elif conflict == 'full_house':
                hand1_values = [VALUES.get(value) for value in hand1.hand['values']]
                hand2_values = [VALUES.get(value) for value in hand2.hand['values']]
                for value in hand1_values:
                    if hand1_values.count(value) == 3:
                        hand1_threes = value
                        break
                for value in hand2_values:
                    if hand2_values.count(value) == 3:
                        hand2_threes = value
                        break
                
                if hand1_threes > hand2_threes:
                    return hand1
                return hand2
                
    if False in (hasattr(hand1, 'rank'), hasattr(hand2, 'rank')):
        if hasattr(hand1, 'rank'):
            return hand1
        elif hasattr(hand2, 'rank'):
            return hand2
        else:
            if hand1.highestCard > hand2.highestCard:
                return hand1
            return hand2

class Card(object):
    def __init__(self, s):
        self.suit = s[1]
        self.value = s[0]
        self.s = s
    def __repr__(self):
        return self.s


class PokerHand(object):
    def __init__(self, s):
        hand = {}
        dealt = s.rstrip().split(' ')
        values = []
        suits = []
        for i in range(5):
            card = dealt[i]
            values.append(card[0])
            suits.append(SUITS.get(card[1]))
        
        hand['suits'] = suits
        hand['values'] = values
        
        self.s = s
        self.hand = hand
        self.isRoyalFlush = self.royal_flush()
        self.isStraightFlush = self.straight_flush()
        self.isFourOfKind = self.four_of_kind()
        self.isFullHouse = self.full_house()
        self.isFlush = self.flush()
        self.isStraight = self.straight()
        self.isThreeOfKind = self.three_of_kind()
        self.isTwoPair = self.two_pairs()
        self.isOnePair = self.one_pair()
        
        self.get_rank()
        self.highestCard = self.get_highest_card()
    
    def __repr__(self):
        return self.s
    
    def get_highest_card(self):
        all_values = [VALUES.get(value) for value in self.hand['values']]
        all_values.sort()
        return all_values[len(all_values)-1]
    
    def get_rank(self):
        if self.isOnePair:
            self.rank = RANKS.get('one_pair')
        if self.isTwoPair:
            self.rank = RANKS.get('two_pair')
        if self.isThreeOfKind:
            self.rank = RANKS.get('three_kind')
        if self.isStraight:
            self.rank = RANKS.get('straight')
        if self.isFlush:
            self.rank = RANKS.get('flush')
        if self.isFullHouse:
            self.rank = RANKS.get('full_house')
        if self.isFourOfKind:
            self.rank = RANKS.get('four_kind')
        if self.isStraightFlush:
            self.rank = RANKS.get('straight_flush')
        if self.isRoyalFlush:
            self.rank = RANKS.get('royal_flush')
        if not hasattr(self, 'rank'):
            self.rank = None
    
    def one_pair(self):
        if len(set(self.hand['values'])) > 4:
            return False
        all_values = [VALUES.get(value) for value in self.hand['values']]
        for value in all_values:
            if all_values.count(value) == 2:
                self.one_pair_value = value
        return True
    
    def two_pairs(self):
        if len(set(self.hand['values'])) > 3:
            return False
        all_values = set(self.hand['values'])
        counts_set = set([self.hand['values'].count(i) for i in all_values])
        return counts_set == set([1,2,2])
    
    def three_of_kind(self):
        for value in self.hand['values']:
            if self.hand['values'].count(value) > 2:
                return True
        return False
    
    def straight(self):
        number_values = []
        for value in self.hand['values']:
            number_values.append(VALUES.get(value))
        number_values.sort()
        d = np.diff(number_values)
        return np.all(d==1)
    
    def flush(self):
        if len(set(self.hand['suits'])) > 1:
            return False
        return True

    def four_of_kind(self):
        if len(set(self.hand['values'])) > 2:
            return False
        all_values = [VALUES.get(value) for value in self.hand['values']]
        for value in all_values:
            if all_values.count(value) == 4:
                return True
        return False
        
    def full_house(self):
        if len(set(self.hand['values'])) > 2:
            return False
        unique_vals = set(self.hand['values'])
        a, b = unique_vals.pop(), unique_vals.pop()
        if (self.hand['values'].count(a), self.hand['values'].count(b)) == (2,3):
            return True
        elif (self.hand['values'].count(a),self.hand['values'].count(b)) == (3,2):
            return True
        return False
        
    
    def royal_flush(self):
        suits = self.hand['suits']
        values = self.hand['values']
        if len(set(suits))>1:
            return False
        for value in ROYAL_FLUSH:
            if value not in values:
                return False
        return True
    
    def straight_flush(self):
        if len(set(self.hand['suits']))>1:
            return False
        number_values = []
        for value in self.hand['values']:
            number_values.append(VALUES.get(value))
        number_values.sort()
        d = np.diff(number_values)
        return np.all(d == 1)


if __name__ == "__main__":
    i = 0
    nolines = 0
    f = open('poker.txt','r')
    for line in f:
        nolines += 1
        hand = line.rstrip()
        hand1 = PokerHand(hand[:14])
        hand2 = PokerHand(hand[14:].lstrip())
        if hasattr(hand1, 'rank') and hasattr(hand2, 'rank'):
            if hand1.rank == hand2.rank:
                print nolines
        if winner(hand1, hand2) == hand1:
            i += 1
    print i
    f.close()
        