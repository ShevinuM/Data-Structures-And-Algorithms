# Time-Complexity - O(n^2). Non-sliding windows approach.
# This is my initial approach to this problem before I knew the sliding window method
def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        s_copy = s[:]
        temp_index = 0
        index = 0
        new_str = ""
        max_length = 0
        while index < len(s_copy):
            if temp_index < len(s_copy):
                character = s_copy[temp_index]
            if character not in new_str:
                new_str = new_str + character
                if len(new_str) > max_length:
                    max_length = len(new_str)
                temp_index += 1
            else:
                new_str = ""
                index+=1
                temp_index=index

        return max_length


# Time-Complexity O(n). Sliding window approach
def lengthOfLongestSubstringSlidingWindow(s):
    """
    :type s: str
    :rtype: int
    """
    substring = set()
    left = 0
    max = 0
    for character in s:
        while character in substring:
            substring.remove(s[left])
            left+=1
        substring.add(character)
        if len(substring) > max:
            max = len(substring)
    return max

def test():
    # Test - non sliding window approach
    print("Test for O(n^2) time complexity algorithm")
    print("_________________________________________")
    print("The length of the substring 'abcabcbb' is -> " + str(lengthOfLongestSubstring("abcabcbb")))
    print("The length of the substring 'bbbbb' is -> " + str(lengthOfLongestSubstring("bbbbb")))
    print("The length of the substring 'pwwkew' is -> " + str(lengthOfLongestSubstring("pwwkew")))
    print()

    # Test for sliding window approach
    print("Test for O(n) time-complexity sliding window approach")
    print("_____________________________________________________")
    print("The length of the substring 'abcabcbb' is -> " + str(lengthOfLongestSubstringSlidingWindow("abcabcbb")))
    print("The length of the substring 'bbbbb' is -> " + str(lengthOfLongestSubstringSlidingWindow("bbbbb")))
    print("The length of the substring 'pwwkew' is -> " + str(lengthOfLongestSubstringSlidingWindow("pwwkew")))
    print()

test()