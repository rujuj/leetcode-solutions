class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        # replace words = s.split(" ") with:
        
        oldChar = ""
        currCount = 0
        
        for char in s:
            if char != " ":
                if oldChar == " ":  # this signifies the start of a new word
                    # words.append(currWord) # we don't even need this here .. just get the last word
                    currCount = 0  # reset!
                currCount += 1  # add the new alphabet character into the current word being tracked
            oldChar = char
        return currCount
    
    
    # other ways to make this more efficient:
    # just start at the back (who says we need to go through the whole string?)
    # there must be a better way to keep track of the previous character?