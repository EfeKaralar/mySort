def myBubbleSort(array):    #time complexity HIGH. time complexity = how much time increases as number of inputs increases. worst case and large data should be taken into account O(N^2) --> upper bound
    tempArray = array
    #iter = 0
    while True:
        b = True 
        #iter += 1           
        for i in range(0, len(tempArray)-1):
            if tempArray[i] > tempArray[i+1]:
                temp = tempArray[i]
                tempArray[i]=tempArray[i+1]
                tempArray[i+1]=temp
                b = False
        if b:
            return tempArray        #return [iter,tempArray]
        
#print(myBubbleSort([3, 2, 6, 7, 5, 1]))    #to check

