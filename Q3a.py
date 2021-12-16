def encryption(n,k):
    #initialize 2-D array
    myarray = [[] for i in range(k)]
    #check if the key=2
    if k == 2:
        for i in range(0,len(n)):
            if i%2 == 0: 
                #ppend the value of n with index to the first array 
                myarray[0].append(n[i])
                
            else:
                # else append the value of n with index to the second array 
                myarray[1].append(n[i])
                #Convert individual indices to string, add them together and print to the console
        return ''.join(myarray[0])+''.join(myarray[1])
     #if key is equals to 3
    elif k == 3:
        count = 0
        # initialize 2-d array  
        myarray = [[],[],[]]
        for i in range(0,len(n)):
            if count == 0:
                myarray[0].append(n[i])
                #increment count
                count+=1
            elif count == 1:
                
                myarray[1].append(n[i])
                #increment count by 1
                count+=1
            else:
                #else the value of n with index as the loop operation to the third array in the myarray
                myarray[2].append(n[i])
                #increment by 1
                count = 0
                
        return ''.join(myarray[0])+''.join(myarray[1])+''.join(myarray[2])
    else:
        # if  the key is not 2 or 3 then
        return 'Inavalid key, key should be 2 or 3'

print(encryption('Plain text',2))
print(encryption('Plain text',3))
print(encryption('Plain text',4))




