def hourglassSum(arr):
    sum_list=[]
    for i in range(len(arr)-2):
        for j in range(len(arr[0])-2):
            sum_list.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])

    return (max(sum_list))

