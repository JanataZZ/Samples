print('Hi')

def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):
    if player_total < 15:
        return True
    else:
        return False

print (should_hit(6, 15, 0, 0))
