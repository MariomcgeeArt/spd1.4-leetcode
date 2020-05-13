class Solution:
    def commonChars(self, A):
        
        # Add first word in list 
        prev_word = [char for char in A[0]]
        
        
        # Loop through the list starting from second item since we already marked the first above 
        for word in A[1:]:
            current_word = []
            for char in word:
                if char in prev_word:
                    # If the current word we are iterating over is in the prev_word then append to the current_word list
                    current_word.append(char)
                    # Need to remove the just visited char otherwise we will keep adding it to our current_word list 
                    prev_word.remove(char)
            
            prev_word = current_word
            
        return prev_word

solution = Solution ()
print(solution.commonChars(['hello','there']))