#!Take the number 192 and multiply it by each of 1, 2, and 3:

#192 × 1 = 192
#192 × 2 = 384
#192 × 3 = 576
#By concatenating each product we get the 1 to 9 pandigital, 192384576. 
#We will call 192384576 the concatenated product of 192 and (1,2,3)

#The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

#What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

largestNum = 123456789 #Start with the lowest possible pandigital

for i in range(1,10000):
    productString = ""
    for x in range(1,10):
        product = i*x
        productString = productString + str(product)
        #Only continue testing if we're exactly 9 digits long (1-9)
        if len(str(productString)) == 9:
            #See if we're all unique numbers (1-9) by comparing length against set() length, and make sure there's no 0 since we're doing 1-9 only. 
            if (len(set(productString)) == len(productString)) and '0' not in productString:
                if int(productString) > largestNum:
                    largestNum = int(productString)
                    baseNum = i
     
print(f"The largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) is: {largestNum}, formed from {i}")