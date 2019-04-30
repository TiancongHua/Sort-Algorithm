#time complexity:O(n^2)
def BubbleSort(data):
    lenth=len(data)

    for i in range(lenth):
        for j in range(1,lenth):
            if data[j]<data[j-1]:
                data[j],data[j-1]=data[j-1],data[j]
    return data

data=[5,1,2,8,7,9]
print(BubbleSort(data))
