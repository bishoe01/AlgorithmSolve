class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        answer = [0] * len(temperatures) #answer [ 0,0,0,0,0,0,0,0]
        stack =[] 

        for i in range(len(temperatures)): #74
            while stack and temperatures[stack[-1]]< temperatures[i]: #73< 74
                day = stack.pop()  #day = 0
                answer[day] = i - day #더 큰 온도 index - 기준점
            stack.append(i) #[0]
        return answer