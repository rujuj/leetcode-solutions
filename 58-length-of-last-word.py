class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        # replace words = s.split(" ") with:
        words = []
        oldChar = ""
        currWord = ""
        
        for char in s:
            if char != " ":
                if oldChar == " ": # this signifies the start of a new word
                    words.append(currWord) # add the old word to the list of words
                    currWord = "" # reset!
                currWord += char # add the new alphabet character into the current word being tracked
            oldChar = char
        words.append(currWord)
                    
        while "" in words:
            words.remove("")
        return len(words[-1])