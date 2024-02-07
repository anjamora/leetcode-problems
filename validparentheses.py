class Solution:
    def isValid(self, s: str) -> bool:
        open = "[{("
        close = "]})"
        stack = ""
        
        for i in s:
            if open.find(i) == 0:
                stack += "["
            elif open.find(i) == 1:
                stack += "{"
            elif open.find(i) == 2:
                stack += "("

            elif len(stack)==0:
                return False
            elif (close.find(i) == 0) and (stack[len(stack)-1] == open[close.find(i)]):
                stack = stack[0:len(stack)-1]
            elif (close.find(i) == 1) and (stack[len(stack)-1] == open[close.find(i)]):
                stack = stack[0:len(stack)-1]
            elif (close.find(i) == 2) and (stack[len(stack)-1] == open[close.find(i)]):
                stack = stack[0:len(stack)-1]
            else:
                return False

        if len(stack) == 0:
            return True