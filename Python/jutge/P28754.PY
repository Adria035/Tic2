"""
Write a program that reads a number and prints its binary representation reversed.

Input

Input consists of a natural number.

Output

Print, reversed, the binary representation of the number, with as many zeros at its left as required.
"""
from easyinput import read

numero = read(int)

numero = bin(numero)
print(numero)


