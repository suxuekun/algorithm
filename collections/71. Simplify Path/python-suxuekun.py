class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')

        ans = []


        for dir in dirs:
            if dir == '':
                continue
            elif dir == '..':
                if len(ans) > 0:
                    ans.pop()
            elif dir != '.':
                ans.append(dir)
        
        return '/'+'/'.join(ans)