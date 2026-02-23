import tkinter as tk
from tkinter import ttk

def add(num1,num2):
     return num1+num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1*num2

def divide(num1:int ,num2:int):
     return num1/num2


def findbracket(i: str):
    numbers = []
    index = 0
    number = ""
    for char in i:
        index += 1
        try:
            int(char)
            number += char
            if(index == len(i)):
                numbers.append(int(number))
        except Exception as e:
              if number:
                numbers.append(int(number))
              numbers.append(char)
              number = ""

    return numbers


def evaluate(i):
    numbers = []

    while "(" in i:
        if '(' in i:
            if ')' in i:
                startb = i.find('(')
                endb = i.find(')')
                subi = i[startb+1:endb]
                numbers.extend(findbracket(subi))
                i = i.replace(f'({subi})', '')
            else:
                raise Exception("Invalid statement")
            
    numbers.extend(findbracket(i))    
   
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
            return num1

# ----------------------
# Calculator Logic
# ----------------------

def solve_expression(expression):
    try:
        # Safe evaluation (only math operators allowed)
        allowed = "0123456789+-*/(). "
        for char in expression:
            if char not in allowed:
                return "Error"
        return evaluate(expression)
    except:
        return "Error"


# ----------------------
# UI Design
# ----------------------

class CalculatorApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Modern Python Calculator")
        self.root.geometry("420x600")   # FIXED SIZE
        self.root.minsize(400, 550)
        self.root.configure(bg="#f4f4f4")

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("TButton",
                        font=("Segoe UI", 14),
                        padding=10)

        style.configure("TEntry",
                        font=("Segoe UI", 22),
                        padding=10)

        # Display
        self.entry = ttk.Entry(root, justify="right")
        self.entry.pack(fill="x", padx=20, pady=20, ipady=10)

        # Button Frame
        frame = tk.Frame(root, bg="#f4f4f4")
        frame.pack(expand=True, fill="both", padx=20, pady=10)

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "(", "+",
            ")", "C", "⌫", "="
        ]

        rows = 5
        cols = 4

        for i in range(rows):
            frame.rowconfigure(i, weight=1)

        for j in range(cols):
            frame.columnconfigure(j, weight=1)

        row = 0
        col = 0

        for button in buttons:
            action = lambda x=button: self.on_button_click(x)

            b = ttk.Button(frame, text=button, command=action)
            b.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

            col += 1
            if col == cols:
                col = 0
                row += 1

    def on_button_click(self, char):

        if char == "=":
            result = solve_expression(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(0, str(result))

        elif char == "C":
            self.entry.delete(0, tk.END)

        elif char == "⌫":
            current = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(0, current[:-1])   # FIXED BACKSPACE

        else:
            self.entry.insert(tk.END, char)


# ----------------------
# Run App
# ----------------------

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()