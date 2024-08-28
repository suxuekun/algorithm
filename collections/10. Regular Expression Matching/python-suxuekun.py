class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        head_match = s and (p[0] == s[0] or p[0] == ".")
        if len(p) >= 2 and p[1] == "*":
            return self.isMatch(s,p[2:]) or (head_match and self.isMatch(s[1:],p))
        else:
            return head_match and self.isMatch(s[1:],p[1:])