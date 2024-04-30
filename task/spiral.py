def spiral(mat):
    re=[]
    left,right,top,bottom=0,len(mat[0])-1,0,len(mat)
    while left<right:
        #left to right
        for i in range(left,right):
            re.append(mat[top][i])
        top-=1
        for i in range(right-1,-1,-1):
            re.append(mat[i][right])
        right-=1
        for i in range(b)
    


mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(spiral(mat))