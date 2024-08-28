class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8 :
            return False
        
        check = False;
        for c in password:
            i = ord(c)
            if 97<=i<=122:
                check = True
                break;
        
        if not check:
            return False
        check = False
            
        for c in password:
            i = ord(c)
            if 48<=i<=57:
                check = True
                break;
                
        if not check:
            return False
        check = False
            
        for c in password:
            i = ord(c)
            if 65<=i<=90:
                check = True
                break;
                
        if not check:
            return False
        check = False
        
        pre = None;
        
        for c in password:
            if c == pre:
                return False
            pre = c
        
        for c in password:
            if c in "!@#$%^&*()-+":
                return True;
        return False
        