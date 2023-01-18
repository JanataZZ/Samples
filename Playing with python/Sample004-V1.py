def sum_on_hand(hand):
    if len(hand) < 1:
        print('Parameter ERROR: Empty hands')
        return -1
    sum = 0
    digital_cards = ['2','3','4','5','6','7','8','9','10']
    face_cards = ['J', 'Q', 'K']
    for card in hand:
        if card in digital_cards:
            sum =sum + int(card)
        elif card in face_cards:
            sum = sum + 10
        elif card == 'A':
            sum = sum + 1
        else:
            print('Parameter ERROR: No such card:', card)
            return -1
    if sum <= 11 and 'A' in hand:
        sum = sum + 10
    return sum    

def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    sum_on_hand_1 = sum_on_hand(hand_1)
    sum_on_hand_2 = sum_on_hand(hand_2)
    if sum_on_hand_1 < 2 or sum_on_hand_2 < 2:
        print('Can not define who wins due parameter error')
        return -1
    if sum_on_hand_1 > 21:
        return False
    if sum_on_hand_2 > 21:
        return True
    if sum_on_hand_1 > sum_on_hand_2:
        return True
    else:
        return False    

    

hand_1 = ['2', 'A', '9']
hand_2 = ['A', 'A', '9', '3']
#hand_2 = []
#print(sum_on_hand(hand_1))
#print(sum_on_hand(hand_2))

print(blackjack_hand_greater_than(hand_1, hand_2))


