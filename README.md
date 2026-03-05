# Modern Python Calculator (Tkinter)

A simple **GUI Calculator built with Python and Tkinter** that evaluates mathematical expressions using a custom parser.
The calculator supports basic arithmetic operations and bracket handling while providing a modern user interface.

---

## Features

* Graphical User Interface using **Tkinter**
* Custom **expression evaluation logic** (not using Python `eval()`)
* Supports:

  * Addition `+`
  * Subtraction `-`
  * Multiplication `*`
  * Division `/`
  * Parentheses `()`
* Input validation for safe calculations
* Backspace and clear functionality
* Modern styled buttons and display

---

## Preview

The calculator includes:

* Large display for expressions
* Grid-based button layout
* Buttons for numbers, operators, brackets, and controls

---

## Project Structure

```
calculator.py
README.md
```

Main components:

| Component            | Description                                              |
| -------------------- | -------------------------------------------------------- |
| `findbracket()`      | Converts an expression string into numbers and operators |
| `evaluate()`         | Processes the mathematical expression step by step       |
| `solve_expression()` | Validates and solves expressions safely                  |
| `CalculatorApp`      | Tkinter GUI for the calculator                           |

---

## Requirements

Python **3.x**

Tkinter (usually included with Python)

No external libraries are required.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/python-calculator.git
```

Navigate to the project folder:

```bash
cd python-calculator
```

Run the program:

```bash
python calculator.py
```

---

## Example Calculations

```
2+3
5*8
(10+5)*2
100/4
```

---

## How It Works

1. The user enters a mathematical expression using the GUI buttons.
2. The expression is validated to ensure only allowed characters are used.
3. The custom parser converts the string into numbers and operators.
4. The calculator processes the operations sequentially and displays the result.

---

## Limitations

* Does not fully implement **BODMAS precedence** yet.
* Decimal numbers may have limited support.
* Nested brackets may not work correctly in complex expressions.

---

## Future Improvements

Possible enhancements:

* Full **BODMAS/PEMDAS implementation**
* Better **decimal number handling**
* Keyboard input support
* History of calculations
* Dark mode UI
* Scientific calculator features

---

## License

This project is open-source and free to use for educational purposes.

---

## Author

Developed by **Rana Arsal**

Python GUI project using Tkinter.
