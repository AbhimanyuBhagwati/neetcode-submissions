class Solution:
    def isValid(self, s: str) -> bool:
        _mapp= {
            ')':'(', 
            ']':'[',
             '}':'{'
        }
        mem_stack= []
        for i in s:
            if i in '({[':
                mem_stack.append(i)
            else:
                if len(mem_stack) <= 0: return False
                if mem_stack[-1] != _mapp.get(i):
                    return False
                else:
                    mem_stack.pop()
        if len(mem_stack) == 0:
            return True
        else:
            return False
            
