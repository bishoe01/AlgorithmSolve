n = int(input())
arr = [int(input()) for _ in range(n)]

end_of_array = n
tmp = []

def cut_array(start,end):
    global end_of_array,arr
    temp_arr = []
    for i in range(end_of_array):
        if(i < start or i> end):
            temp_arr.append(arr[i])
    
    end_of_array = len(temp_arr)
    for i in range(end_of_array):
        arr[i] = temp_arr[i]

        
for _ in range(2):
    s,e = map(int,input().split())
    cut_array(s -1 , e - 1 )

print(end_of_array)
for i in range( end_of_array ):
    print(arr[i])