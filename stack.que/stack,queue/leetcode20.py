class Solution:
    def isValid(self, s: str) -> bool:
        table = { '}':"{", "]":"[", ")":"("}
        answer = []
        for element in s:
            if(element in table.values()):
                answer.append(element)
            else:
                if(answer and table[element]==answer[-1]):
                    answer.pop()
                else:
                    return False
        
        if(answer):
            return False
        return True
