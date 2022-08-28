class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        oldChar = ""
        for i in range(len(s) - 1, -1, -1):
            if s[i]!= " ":
                if oldChar == " ":  # this signifies the start of a new word
                    if count > 0:
                        return count
                    count = 0  # reset!
                count += 1  # add the new alphabet character into the current word being tracked
            oldChar = s[i]
        return count
    
    # other ways to make this more efficient:
    # there must be a better way to keep track of the previous character?