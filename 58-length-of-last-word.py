class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        # replace words = s.split(" ") with:
        
        oldChar = ""
        currWord = ""
        
        for char in s:
            if char != " ":
                if oldChar == " ": # this signifies the start of a new word
                    # words.append(currWord) # we don't even need this here .. just get the last word
                    currWord = "" # reset!
                currWord += char # add the new alphabet character into the current word being tracked
            oldChar = char
        return len(currWord)