import math
num = int(input()) # 팩토리얼해줄 숫자 입력받기
num = str(math.factorial(num)) #뒤집기 위한 str로 묶어주기, 0은 뒤집어서 맨앞에올 수 없기 때문이다.

result = num[::-1]  #-1부터 읽어줘서 문자열을 뒤집어 주는 효과이다.
cnt = 0  #0이 몇번들어가는지 카운트해주는 변수
for char in result: #뒤집힌 문자열의 문자하나씩 반복문돌려주기
    if(char == '0' ): # '0'으로 해줘야함 문자열이니까 , 0으로해주면 0 != '0'이기때문에 에러가 남
        cnt+=1
    else:  #0아닌 수 발견즉시 break끝내주기
        break
print(cnt)