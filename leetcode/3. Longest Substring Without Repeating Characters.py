'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

Time: O(n) Space: O(n)
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize a sliding window and a set to store the characters in the current window
        window_start, max_length, char_set = 0, 0, set()
        
        # Iterate through the string
        for window_end in range(len(s)):
            # Add the current character to the set
            curr_char = s[window_end]
            if curr_char in char_set:
                # If the current character is already in the set, remove the characters from the set
                # until the current character is removed
                while curr_char in char_set:
                    char_set.remove(s[window_start])
                    window_start += 1
            # Add the current character to the set
            char_set.add(curr_char)
            # Update the maximum length
            max_length = max(max_length, window_end - window_start + 1)
        
        return max_length

'''
Time: O(n) Space: O(1)
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize a sliding window and an array to store the index of each character in the current window
        window_start, max_length, char_indexes = 0, 0, [-1] * 128
        
        # Iterate through the string
        for window_end in range(len(s)):
            # Get the index of the current character in the array
            curr_char_index = ord(s[window_end])
            # Check if the character is in the current window
            if char_indexes[curr_char_index] >= window_start:
                # If the character is in the current window, update the window start to the next character
                window_start = char_indexes[curr_char_index] + 1
            # Update the index of the current character in the array
            char_indexes[curr_char_index] = window_end
            # Update the maximum length
            max_length = max(max_length, window_end - window_start + 1)
        
        return max_length
