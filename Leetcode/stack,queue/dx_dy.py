command = input()
x,y = 0 , 0
dir_num = 0

dx ,dy= [0 ,1 ,0, -1] , [1 ,0 ,-1 ,0]

#rotation direction



for element in command:
    if(element == "L"):
        dir_num = (dir_num-1 )%4
    elif(element == "R"):
        dir_num = (dir_num+1)%4  
    else : #F
        x,y =x+dx[dir_num],y+ dy[dir_num]
print(x,y)

