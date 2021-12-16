def decryption(n,k):
    # check if  key equals 2
    if k ==2:
        #variable that hold first half of the string
        text1 = n[0:round(len(n)/2)]
        # variable that holds second half of the string
        text2 = n[round(len(n)/2):]
        string = ''
        # two varibales that will be used as counts for indices
        count1 = 0
        count2 = 0
        #for loop that runs to the length of n
        for i in range(1,len(n)+1):
            #check if its mod 2 and equals zero
            if i%2 == 0:
                string +=text2[count2]
                count2+=1
            else:
                #else increment the output string
                string+= text1[count1] 
                count1+=1
        return string
    #else if k equals 3
    elif k ==3: 
        check = (len(n)/3)%3%1   
        # if that output is less than 0.5 and not equal to zero
        if check <0.5 and check!=0:
            a = round(len(n)/3) + 1
        else:
            a = round(len(n)/3)
        extra1 = round((len(n) - a)/2)
        extra = round(a + extra1)
        c1 = len(n) - a - extra1
        # c1 which equals extra plus c1
        c = extra+c1
        text1 = n[0:a]
        text2 = n[a:extra]
        string3 = n[extra:]
        
        # initilaize final string output
        string = ''
        count1 = 0
        count2 = 0
        s3 = 0
        # inirialize count variaextrale
        count = 0
        
        # loop from zero to length of n
        for i in range(0,len(n)):
            if count == 0:
                string +=text1[count1]
                count1+=1
                count+=1
            elif count == 1:
                string+= text2[count2] 
                count2+=1
                count+=1
            else:
                string+= string3[s3] 
                s3+=1
                count = 0
        # retrun output string
        return string
    else:
        return 'Enter valid key, key should either be 2 or 3'
    
print(decryption('Pantxli et',2))
print(decryption('Pittlnea x',3))
print(decryption('Pittlnea x',4))