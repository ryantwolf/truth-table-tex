# Truth-Table-Tex
## Overview
Truth-Table-Tex is a script that I wrote to automate making truth tables in LaTeX, something I found very tedious to do.
## Installation
Clone the repository
```
git clone https://github.com/ryantwolf/truth-table-tex.git
```
## Usage
Run main.py with a command along the lines of 
```
python main.py
```
A series of prompts will follow, where you will be able to choose the base variables, the number of additional columns you would like, and the operations you want to perform for each column.\
The resulting truth table will be written to `output.tex`
## Examples
```
Enter the names of the variables (Space Separated):P Q R
How many additional columns do you need? 3
Which operation would you like to perform?
NOT (1) AND (2) OR (3) IMPLIES (4) 2
The current columns and their indecies are...
P (1) Q (2) R (3)
What are the numbers of the columns you would like to perform AND on? (Space Separated) 2 3
Which operation would you like to perform?
NOT (1) AND (2) OR (3) IMPLIES (4) 4
The current columns and their indecies are...
P (1) Q (2) R (3) Q\land R (4)
What are the numbers of the columns you would like to perform IMPLIES on? (Space Separated) 1 4
Which operation would you like to perform?
NOT (1) AND (2) OR (3) IMPLIES (4) 3
The current columns and their indecies are...
P (1) Q (2) R (3) Q\land R (4) P\to (Q\land R) (5)
What are the numbers of the columns you would like to perform OR on? (Space Separated) 2 5
Writing table to output.tex
```
Result:
```latex
$$\begin{array}{c|c|c|c|c|c} 
P & Q & R & Q\land R & P\to (Q\land R) & Q\lor (P\to (Q\land R))\\\hline 
F & F & F & F & T & T \\
F & F & T & F & T & T \\
F & T & F & F & T & T \\
F & T & T & T & T & T \\
T & F & F & F & F & F \\
T & F & T & F & F & F \\
T & T & F & F & F & T \\
T & T & T & T & T & T \\
\end{array}$$
```
![Rendered LaTeX](https://github.com/ryantwolf/truth-table-tex/blob/master/images/example.png)