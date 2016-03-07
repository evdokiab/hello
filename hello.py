
#x = [
#    [0 for  col in range(10)]
#     for row in range(20)
#    ]
x = [[0]*10 for i in range(20)]

def place(i,j):
    x[i][j] = 1
    x[i][j+1] =1
    return True
stop= False
i = 3
j = 8
while stop != True :
    if x[i][j] == 0 and x[i][j+1] == 0:
        stop = place(i,j)
    stop = True

print x
