class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ")": "(",
            "}": "{", 
            "]": "["
            }
        
        for char in s:
            if char in mapping:
                if stack and stack[-1] == mapping[char]:
                    stack.pop()
                    return False
            else:
                print(f"Adding {char} to stack")
                stack.append(char)
        
        return True if not stack else False 

    def isValid2(self, s: str) -> bool:
        stack = []
        mapping = {
            ")": "(",
            "}": "{", 
            "]": "["}
        
        for ch in s:
            if ch in mapping:
                top_element = stack.pop() if stack else '#'
                if top_element != mapping[ch]:
                    return False
            else:
                stack.append(ch)
        
        return not stack

if __name__ == "__main__":
    solution = Solution()
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("(", False),
        (")", False),
        ("{[()]}", True),
        ("{[(])}", False)
    ]

    for s, expected in test_cases:
        result = solution.isValid2(s)
        print(f"isValid('{s}') = {result}, expected = {expected}, {'PASS' if result == expected else 'FAIL'}")