

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def possible_palindromic(l,r):
            while(l >= 0 and r < len(s) and s[l] == s[r]):
                l -= 1
                r += 1
            return s[l+1:r]

        pal = ""
        for i in range(len(s)):
            p = possible_palindromic(i,i)
            if len(p) > len(pal) : pal = p
            #for even
            p = possible_palindromic(i,i+1)
            if len(p) > len(pal) : pal = p

        return pal