class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def calc(expression):
            result = []
            for i,c in enumerate(expression):
                if c in '+-*':
                    left = calc(expression[:i])
                    right = calc(expression[i+1:])
                    
                    for a in left:
                        for b in right:
                            if c == '+':
                                result.append(a+b)
                            elif c == '-':
                                result.append(a-b)
                            else:
                                result.append(a*b)
            if not result:
                return [int(expression)]
            
            return result
        
        return calc(expression)
        
