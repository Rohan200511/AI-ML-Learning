def largest(a , b , c):
    return max(a , b , c)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Largest among ", a , b , c ,"is" , largest(a,b,c))