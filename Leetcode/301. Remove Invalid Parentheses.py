class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans = set()
        mra = self.getMin(s)
        self.solution(s, mra, ans, set())

        return list(ans)

    def solution(self, s, mra, ans, visited):
        if s in visited:
            return
        visited.add(s)
        if mra == 0:
            mrnow = self.getMin(s)
            if mrnow == 0:
                if s not in ans:
                    ans.add(s)
            return

        for i in range(len(s)):
            left = s[0:i]
            right = s[i+1:]
            self.solution(left+right, mra-1, ans, visited)

    def getMin(self, s):
        stack = []
        for i in s:
            if i == "(":
                stack.append(i)
            elif i == ")":
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(i)
        return len(stack)

# "((()((s((((()"
