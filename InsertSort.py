def InsertSort(data):

    lenth=len(data)
    for i in range(1,lenth):
        preIndex=i-1
        current=data[i]
        #change array[i] to right place,cost a lot
        while(preIndex>=0 and data[preIndex]>current):
            data[preIndex+1]=data[preIndex]
            preIndex-=1
        data[preIndex+1]=current
    return data

data=[5,1,2,8,7,9]

print(InsertSort(data))