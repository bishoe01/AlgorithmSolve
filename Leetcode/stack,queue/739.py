class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        std = 0
        answer = []
        for i in range(len(temperatures)-1):
            std = 0
            for k in range(i+1,len(temperatures)):
                if(temperatures[i] >= temperatures[k]):
                    if(k == len(temperatures)-1): #끝에있는친구
                        answer.append(0)
                        break;
                    else: 
                        std+=1    
                elif(temperatures[i] < temperatures[k]):
                    std+=1
                    answer.append(std)
                    break
        answer.append(0)
        return answer