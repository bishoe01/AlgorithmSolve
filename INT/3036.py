from fractions import Fraction ##분수계산해주는 모듈
N = int(input())
arr = list(map(int,input().split())) ##리스트로 받기
std = arr[0] ## 첫번째 값을 기준값으로 저장해주기 
for i in range(1,len(arr)):
    print(Fraction(std,arr[i]).numerator,end="") ##numerator 은 분자
    print("/",end="") ##붙여서 출력하기 위한 end=""
    print(Fraction(std,arr[i]).denominator) ##denominator은 분모 
