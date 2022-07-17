arr = [4, 10 ,37 ,53, 88, 260, 67, 88, 500 ,400]

sum = 0 
avg = 0
for element in arr: 
    sum+= int(element)

answer = []

answer.append(sum)
avg = sum//len(arr)
answer.append(avg)
print(answer[0], answer[1])