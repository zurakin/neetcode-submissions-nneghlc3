class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        frequencies = defaultdict(int)
        for c in hand:
            frequencies[c] += 1
        hand = sorted([[num, freq] for num, freq in frequencies.items()])
        for i in range(len(hand)):
            frequency = hand[i][1]
            if frequency > 0:
                if i + groupSize > len(hand):
                    return False
                hand[i][1] = 0
                for j in range(i+1, i+groupSize):
                    if hand[j][0]-hand[j-1][0] != 1:
                        return False 
                    if hand[j][1] < frequency:
                        return False
                    hand[j][1] -= frequency
                
        return True
        # 1 2 2 3 3 4 4 5
        # 0 1 2 2 2 1 0
        # 0 0 1 1 1 1 0
        # 0 0 0 0 0 0 0
