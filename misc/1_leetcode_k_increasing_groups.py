# Link: https://leetcode.com/submissions/detail/1076957133/

from collections import defaultdict

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: 
            return False
        
        freq = defaultdict(int)
        for card in hand: freq[card] += 1
            
        hand.sort()
        current_card_group = []
        for i in range(len(hand)):
            curr_card = hand[i]
            # print(curr_card, freq)
            if freq[curr_card] == 0:
                continue 
                
            if len(current_card_group) == 0:
                # print('If case 1')
                current_card_group.append(curr_card)
                freq[curr_card] -= 1
            else:
                # print('If case 2')
                while len(current_card_group) < groupSize:
                    curr_card = current_card_group[-1]
                    nxt_card = curr_card + 1
                    if freq[nxt_card] == 0:
                        return False
                    freq[nxt_card] -= 1
                    current_card_group.append(nxt_card)
                current_card_group = []
        return True
