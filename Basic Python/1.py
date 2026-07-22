a = int(input("Enter first Integer: "))
b = int(input("Enter second Integer: "))
op = input("Enter any operator : (+ , - , * , /) : ")

case = op
match case:
    case "+":
        print (a + b)
    
    case "-":
        print(a - b)
    
    case "*":
        print(a * b)
        
    case "/":
        print(a / b)