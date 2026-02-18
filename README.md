# Simple Python Calculator

A lightweight command-line calculator written in Python.
It parses a basic mathematical expression entered by the user and evaluates it sequentially.

## 📌 Features

* Supports basic arithmetic operations:

  * Addition (`+`)
  * Subtraction (`-`)
  * Multiplication (`*`)
  * Division (`/`)
* Accepts a single-line number statement (e.g., `2+7`, `10*5`, `8/2`)
* Sequential evaluation from left to right
* No external dependencies required

---

## 🛠 How It Works

1. The program prompts the user to enter a number statement.
2. The input string is parsed character by character.
3. Numbers and operators are separated into a list.
4. Operations are executed sequentially.
5. The final result is printed to the console.

Example input:

```
2+7
```

Output:

```
9
```

Example input:

```
10+5*2
```

Output:

```
30
```

> Note: The calculator evaluates expressions from left to right and does not follow mathematical operator precedence rules.

---

## 🚀 Getting Started

### Requirements

* Python 3.x

### Run the Program

```bash
python calculator.py
```

Then enter your expression when prompted:

```
enter a number statement
```

---

## 📂 Project Structure

```
calculator.py
README.md
```

---

## 🧠 Functions Overview

* `add(num1, num2)` → Returns the sum
* `subtract(num1, num2)` → Returns the difference
* `multiply(num1, num2)` → Returns the product
* `divide(num1, num2)` → Returns the quotient
* `main()` → Handles input parsing and calculation logic

---

## ⚠ Limitations

* No support for:

  * Parentheses
  * Decimal numbers
  * Negative numbers
  * Operator precedence (PEMDAS/BODMAS)
* Division by zero is not handled explicitly.
* Minimal error validation.

---

## 🔮 Possible Improvements

* Add operator precedence support
* Support floating-point numbers
* Implement better error handling
* Add unit tests
* Convert into a GUI application
* Package as a pip-installable CLI tool

---

## 📜 License

This project is open-source and free to use for learning purposes.

---

If you'd like, I can also create:

* A more advanced README (for GitHub portfolio presentation)
* A version with badges
* A version written more casually
* A technically deeper README explaining the parsing logic

Tell me your target (school project, portfolio, beginner repo, etc.) and I’ll tailor it precisely.
