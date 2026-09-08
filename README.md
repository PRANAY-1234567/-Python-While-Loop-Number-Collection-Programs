# 🐍 Python While Loop – Number & Collection Programs

A collection of beginner-to-intermediate **Python programs using `while` loops** to practice number theory, mathematical sequences, tuples, lists, strings, and conditional logic.

These programs focus on developing **logical thinking, iteration skills, data processing, and problem-solving ability** using Python.

---

## 📌 Project Overview

This collection contains programs for:

* Finding factors of a number
* Checking perfect numbers
* Generating Fibonacci series
* Separating even and odd numbers from a tuple
* Filtering strings based on their middle-character condition
* Working with lists and tuples using `while` loops

The primary goal is to understand how the `while` loop can be used to solve different programming problems.

---

## 🛠️ Technologies Used

* **Python 3**
* `while` loops
* `if-else` statements
* Lists
* Tuples
* Strings
* `len()`
* Modulus operator `%`
* Multiple assignment
* Arithmetic operators

---

# 📂 Programs Included

## 1. Display Factors of a Given Number

### Problem

Write a Python program to display all the factors of a given number.

### Code

```python
num = int(input("Enter the number: "))

i = 1
out = []

while i <= num:
    if num % i == 0:
        out.append(i)
    i += 1

print(out)
```

### Example

```text
Enter the number: 12

[1, 2, 3, 4, 6, 12]
```

### Logic

A number `i` is a factor of `num` when:

```python
num % i == 0
```

For example, the factors of `12` are:

```text
1, 2, 3, 4, 6, 12
```

---

# 2. Check Whether a Number Is a Perfect Number

### Problem

Write a Python program to determine whether a given number is a **perfect number**.

A perfect number is a positive integer that is equal to the sum of its proper divisors.

### Code

```python
num = int(input("Enter the number: "))

i = 1
out = 0

while i < num:
    if num % i == 0:
        out = out + i
    i += 1

if out == num:
    print("Entered number is a perfect number")
else:
    print("Not a perfect number")
```

### Example

```text
Enter the number: 6

Entered number is a perfect number
```

### Explanation

The proper factors of `6` are:

```text
1, 2, 3
```

Their sum is:

```text
1 + 2 + 3 = 6
```

Therefore, `6` is a perfect number.

Other examples include:

```text
6
28
496
8128
```

---

# 3. Generate Fibonacci Series

### Problem

Write a Python program to generate the Fibonacci series.

### Code

```python
num = int(input("Enter the number: "))

a = 0
b = 1
i = 0

while i <= num:
    print(a, end=" ")
    a, b = b, a + b
    i += 1
```

### Example Output

```text
Enter the number: 10

0 1 1 2 3 5 8 13 21 34 55
```

### Logic

Each Fibonacci number is obtained by adding the previous two numbers:

```text
0 + 1 = 1
1 + 1 = 2
1 + 2 = 3
2 + 3 = 5
3 + 5 = 8
```

The statement:

```python
a, b = b, a + b
```

updates both variables simultaneously.

---

# 4. Separate Even and Odd Values From a Tuple

### Problem

Given a homogeneous tuple of integers, divide its values into two lists:

* Even numbers
* Odd numbers

### Code

```python
k = (1, 2, 3, 4, 5, 6, 7, 6, 8)

even = []
odd = []

i = 0

while i < len(k):
    if k[i] % 2 == 0:
        even.append(k[i])
    else:
        odd.append(k[i])
    i += 1

print(even)
print(odd)
```

### Output

```text
[2, 4, 6, 6, 8]
[1, 3, 5, 7]
```

### Logic

The modulus operator is used to identify even numbers:

```python
k[i] % 2 == 0
```

If the remainder is `0`, the value is even.

Otherwise, it is odd.

---

# 5. Fetch Strings Having a Middle Character

### Problem

Given a list of strings, display only the strings that contain **one middle character**.

### Code

```python
lst = ["apple", "cat", "Dog", "juy"]

i = 0

while i < len(lst):
    if len(lst[i]) % 2 != 0:
        print(lst[i])
    i += 1
```

### Output

```text
apple
cat
Dog
juy
```

### Explanation

A string has exactly **one middle character** when its length is odd.

For example:

```text
apple
01234
  2
```

The middle character is:

```text
p
```

For an even-length string, there are two middle characters.

Example:

```text
"book"

b o o k
  ↑ ↑
```

Therefore, the condition:

```python
len(lst[i]) % 2 != 0
```

checks whether the string has an odd number of characters.

---

# 🧠 Important Python Concepts

## 1. `while` Loop

A `while` loop executes a block of code repeatedly while a condition remains `True`.

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

---

## 2. Modulus Operator `%`

The modulus operator returns the remainder after division.

```text
10 % 2 → 0
11 % 2 → 1
```

It can be used to:

* Find even numbers
* Find odd numbers
* Find factors
* Check divisibility

---

## 3. Lists

Lists are mutable collections used to store multiple values.

```python
even = []
odd = []
```

Values can be added using:

```python
even.append(value)
```

---

## 4. Tuples

A tuple is an ordered collection that cannot be modified after creation.

```python
k = (1, 2, 3, 4, 5)
```

Individual elements can be accessed using indexes:

```python
k[0]
k[1]
k[2]
```

---

## 5. String Indexing

Python uses zero-based indexing.

For:

```text
apple
```

the indexes are:

```text
a → 0
p → 1
p → 2
l → 3
e → 4
```

The middle character is therefore at index:

```text
2
```

---

## 6. `len()`

The `len()` function returns the number of elements in a collection or characters in a string.

```python
len("apple")
```

Output:

```text
5
```

---

## 7. Multiple Assignment

Python allows multiple variables to be assigned in one statement.

```python
a, b = b, a + b
```

This is especially useful for generating the Fibonacci series.

---

# 🔄 Program Logic Overview

```text
                 Python While Loop
                        │
          ┌─────────────┼─────────────┐
          │             │             │
          ▼             ▼             ▼
       Numbers      Collections     Strings
          │             │             │
     ┌────┼────┐        │             │
     │    │    │        ▼             ▼
   Factor Perfect   Tuple Split   Middle Character
   Numbers Number   Even / Odd      Filtering
          │
          ▼
      Fibonacci
```


---

# 📊 Program Summary

| # | Program                  | Main Concept          |
| - | ------------------------ | --------------------- |
| 1 | Find Factors             | `%` + `while` loop    |
| 2 | Perfect Number           | Factors + accumulator |
| 3 | Fibonacci Series         | Multiple assignment   |
| 4 | Even/Odd Tuple           | Tuple + `%`           |
| 5 | Middle Character Strings | String length + `%`   |

---

# 🎯 Learning Objectives

After completing these programs, you should be able to:

* Use `while` loops for iterative problems.
* Work with lists and tuples.
* Use indexes to access collection elements.
* Apply the modulus operator effectively.
* Find factors of a number.
* Understand perfect numbers.
* Generate Fibonacci sequences.
* Separate values based on conditions.
* Determine whether a string has a single middle character.
* Build logical solutions without relying heavily on built-in functions.

---

# 🚀 Recommended Next Practice

After completing these programs, try solving:

### Number Programs

* Check whether a number is prime.
* Check whether a number is an Armstrong number.
* Check whether a number is a palindrome.
* Reverse a number.
* Find the sum of digits.
* Count the digits of a number.
* Find GCD and LCM.
* Generate prime numbers within a range.

### List & Tuple Programs

* Find the largest value.
* Find the smallest value.
* Find duplicate values.
* Count occurrences of each value.
* Remove duplicates without using `set()`.
* Separate positive and negative numbers.
* Find values at odd indexes.

### String Programs

* Count vowels and consonants.
* Reverse a string without slicing.
* Check whether a string is a palindrome.
* Count uppercase and lowercase characters.
* Find characters at odd indexes.
* Remove spaces from a string.
* Replace vowels with `*`.

---

## 👨‍💻 Author

**Pranay Vishwanath Jadhao**

This repository is created as part of **Python programming practice** to strengthen problem-solving skills, loop concepts, and fundamental data-structure operations.

---

## 📄 License

This project is created for **educational and learning purposes**.
