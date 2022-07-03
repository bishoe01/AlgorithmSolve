import collections
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter , seen , stack = collections.Counter(s),set(), []
        for element in s :
            counter[element]  -=1 #나온 원소는 카운터에서 1을 빼준다.
            if element in seen:
                continue
            while(stack and element < stack[-1] and counter[stack[-1]] > 0): #연결되는지를 판단 
        #stack이 있으면서 알파벳이 stack의 끝보다 작으면서 stack끝이 1개이상일 때 
                seen.remove(stack.pop())
        
            stack.append(element)
            seen.add(element)
        return ''.join(stack)
