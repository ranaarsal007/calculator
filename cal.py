import re

def add(num1,num2):
     return num1+num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1*num2

def divide(num1:int ,num2:int):
     return num1/num2
def expressionn():
    number = ""

    numbers = []
    index = 0
    for char in i:
        index += 1
        try:
            int(char)
            number += char
            if(index == len(i)):
                numbers.append(int(number))
        except Exception as e:
            numbers.append(int(number))
            numbers.append(char)
            number = ""

    num1 = 0
    num2 = 0
    op = ""

    j = 0
    for element in numbers:
        j += 1
        if type(element) == int and num1 == 0:
            num1 = element
        elif type(element) == int and num2 == 0:
            num2 = element
        elif type(element) == str:
            op = element

        if num1 and num2 and op:
                answer = 0
                if op == "*" :
                    answer = multiply(num1,num2)
                elif op == "+" :
                    answer = add(num1,num2)
                elif op == "-" :
                    answer = subtract(num1, num2)
                elif op == "/" :
                    answer = divide(num1,num2)

                num1 = answer
                num2 = 0
        if j == len(numbers):
            print(num1)

def bracket(expression):

    while "(" in expression:
        start = expression.rfind("(")
        end = expression.rfind(")", start)
        inside = expression[start + 1:end]
        result = expressionn(inside)
        expression = expression[:start] + str(int(result)) + expression[end +1:]
        return expressionn(expression)
    

def main():
    i = input("enter a number statement")
    result = bracket(i)
    print(result)
i = i[:startb] + i[endb + 1:]
main()