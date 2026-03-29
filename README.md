# AI-Enabled Smart Calculator

## Overview

This project is a command-line calculator developed using Python that performs basic arithmetic operations. In addition to standard functionality, it includes an AI-based mode that allows users to enter calculations in natural language.

A simple Machine Learning model is used to identify the intended mathematical operation from the user’s input.

---

## Features

### Basic Operations

* Addition
* Subtraction
* Multiplication
* Division

### Smart (AI) Mode

Users can enter commands in natural language such as:

* "add 5 and 3"
* "divide 10 by 2"

The system interprets the input and returns the correct result.

### Normal Mode

Works like a traditional calculator using numbers and operators.

### Error Handling

* Handles invalid inputs
* Prevents division by zero

---

## Technologies Used

* Python
* Scikit-learn
* CountVectorizer (for text processing)
* Multinomial Naive Bayes (for prediction)

---

## Project Structure

* `smart_calculator.py` → main program
* `README.md` → project documentation

---

##  Working Principle

### 1. Machine Learning Model

* A small dataset of keywords is created
* Words like *add, plus, sum* are mapped to addition
* Text input is converted into numerical form using CountVectorizer
* A Naive Bayes model is trained to classify operations

---

### 2. Smart Input Processing

* User enters a sentence (e.g., "add 5 and 3")
* Numbers are extracted from the text
* The ML model predicts the operation
* The result is calculated and displayed

---

### 3. Dual Mode System

#### 🔹 Smart Mode

* Activated by typing `smart`
* Accepts natural language input

Example:

```
Input: add 5 and 3
Output: 8
```

#### 🔹 Normal Mode

* User enters numbers and operators manually

Example:

```
Enter first number: 5  
Enter operator: +  
Enter second number: 3  
Result: 8  
```

---

## How to Run

### Step 1: Install dependencies

```
pip install scikit-learn
```

### Step 2: Run the program

```
python smart_calculator.py
```

---

##  Example Inputs

* add 10 and 5 → 15
* subtract 9 and 3 → 6
* multiply 4 and 2 → 8
* divide 8 by 2 → 4

---

##  Limitations

* Supports only basic arithmetic operations
* Works best with simple sentences
* Handles only two numbers at a time
* Limited vocabulary for prediction

---

##  Future Improvements

* Support complex mathematical expressions
* Add voice input functionality
* Improve accuracy with larger datasets
* Develop a graphical user interface (GUI)

---

##  Learning Outcomes

* Understanding basic Machine Learning concepts
* Text classification using Naive Bayes
* Natural language processing basics
* Applying AI in real-world applications

---

##  Author

Vidushi Singh

---

## 📸 Output Screenshot
<img width="1299" height="252" alt="image" src="https://github.com/user-attachments/assets/2e8a60cc-adad-4d33-8693-10a1b3f8cb5f" />


