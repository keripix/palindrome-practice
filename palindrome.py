#!/usr/bin/env python2
import re

"""
A simple exercise on detecting a palindrome.
"""


def reverse(text):
    return cleanse(text)[::-1]


def isPalindrome(text):
    return cleanse(text).lower() == reverse(text).lower()


def cleanse(text):
    return re.sub(r'[^A-Za-z]+', '', text)


if __name__ == '__main__':
    text = raw_input("Enter text: ")

    if (isPalindrome(text)):
        print("Yes, it is a palindrome")
    else:
        print("Nope, it is not a palindrome")
