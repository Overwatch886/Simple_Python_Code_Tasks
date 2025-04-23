def collatz(number) : 
    while number != 1 : 
            if (number % 2) == 0 :
                number = number // 2
                print (number)
            elif  (number%2) == 1 : 
                number = 3 * number + 1  
                print(number)
            continue  
number = int(input('Input a Number'))
# TODO : Help me add a try except statement preventing non integer input from users
# QUESTION: Can you do it?

result = (collatz(number))
    
