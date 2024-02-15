class Solution:
    def isPalindrome(self, s: str) -> bool:
        reverse = ''
        s = s.casefold()
        for i in s:
            if i.isalnum() == True:
                reverse = i + reverse
            else:
                s = s.replace(i,'')
        return s == reverse