def superdigit(n,k):
#Initialize the p variable that concatenate the string n*k times
    p = n*k
#initialize the loop_digit variable that stores the result from the p variable
    loop_digit = p 
#While the length of the variable P is not equal to 1
    while len(loop_digit) != 1:
#Initialize a new variable called add that would hold the sum of the digits
        add = 0
#a for loop that loops through from zero to the length of digits
        for i in range(0,len(loop_digit)):
#Increment the add (sum) variable created in step 5 by an integer value of the current loop through
            add+=int(loop_digit[i])
#Re initialize loop_digit to the string of the current add variable so it can be concatenated
        loop_digit = str(add)
#return the loop digit
    return loop_digit
#print the superdigit
print(superdigit('9875',4))
