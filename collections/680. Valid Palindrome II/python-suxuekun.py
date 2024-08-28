class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0;
        j = len(s)-1;
        count = 0;
        while i < j:
            if s[i] != s[j]:
                break;
            i+=1;
            j-=1;
        if i>j-1:
            return True
        s1 = s[i:j]
        if s1 == s1[::-1]:
            return True
        s2 = s[i+1:j+1]
        if s2 == s2[::-1]:
            return True
        return False
      
