class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_str = [i.lower() for i in s if i.isalnum()]
        return filtered_str == filtered_str[::-1]

    