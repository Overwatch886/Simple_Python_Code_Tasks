def collatz(number) : 
    while number != 1 : 
            if (number % 2) == 0 :
                number = number // 2
                print (number)
            elif  (number%2) == 1 : 
                number = 3 * number + 1  
                print(number)
            continue  
while True : 
    try:
        number = int(input('Input a Number: (Input the code 886 to end this operation)'))
        result = collatz(number)
    except ValueError:
        print("Invalid input. Please enter an integer.")
    if number == 886 :
        break 


    
