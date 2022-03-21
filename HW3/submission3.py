#!/usr/bin/python

"""
Python Core object Types
"""


def add_binary(a, b):
    """
    This is to review binary operations
    ============================================================
    Given two binary strings, return their sum (also a binary string).
    Return None if one of the input strings are empty or contains characters different than 1 or 0.
    Example 1:
                Input: a = "11", b = "1"
                Output: result = "100"
    Example 2:
                Input: a = "1010", b = "1011"
                Output: result = "10101"
    """
    i=0
    flag = False
    while i < len(a):
        if (a[i]) == "0" or (a[i]) == "1":
            i+=1
        else:
            flag = True
            i+=1
    
    i=0
    while i < len(b):
        if (b[i]) == "0" or (b[i]) == "1":
            i+=1
        else:
            flag = True
            i+=1
     
    if len(a) == 0 or len(b) == 0:
        flag = True
            
            
    if (flag == True):
        return None
      
    if (flag == False):
        
        result = ""
        carry = 0
        i = -1
        times = max(len(a),len(b))
        if len(a) > len(b):
            b = (len(a)-len(b))*("0")+b
        if len(b) > len(a):
            a = (len(b)-len(a))*("0")+a
        times = times *(-1)
        times -= 1
        while i > times:
            if (int(a[i]) + int(b[i]) + carry) == 0:
                result = "0" + result
                i -= 1
            elif (int(a[i]) + int(b[i]) + carry) == 1:
                result = "1" + result
                i -= 1
                if carry == 1:
                    carry -=1
            elif (int(a[i]) + int(b[i]) + carry) == 2:
                result = "0" + result
                if carry == 0:
                    carry +=1
                i -= 1
            elif (int(a[i]) + int(b[i]) + carry) == 3:
                result = "1"  + result
                if carry == 0:
                    carry +=1
                i -= 1
        if carry == 1:
            result = "1" + result
        return result
    
    
def plus_one(digits):
    """
    This is to review loops and if statements
    ============================================================
    Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
    You can do this in-place!
    The digits are stored such that the most significant digit is at the head of the list, and each
    element in the array contain a single digit.
    You may assume the integer does not contain any leading zero, except the number 0 itself.
    Example 1:
            Input: digits = [1, 2, 3]
            Output: digits = [1, 2, 4]
            Explanation: The array represents the integer 123.
    Example 2:
            Input: digits = [1, 0, 9, 9]
            Output: digits = [1, 1, 0, 0]
    """
    i = 0
    newlist = []
    s = ""
    while i < len(digits):
        s = s + str(digits[i])
        i += 1
    s = int(s)
    s += 1
    s = str(s)
    i = 0
    while i < len(s):
        newlist.append(int(s[i]))
        i += 1
    digits = newlist
    return digits

def roman_to_integers(roman_string):
    
    """
    This is to review loops, if statements and dictionaries
    ============================================================
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    For example, two is written as II in Roman numeral, just two one's added together.
    Twelve is written as, XII, which is simply X + II. The number twenty seven is written
    as XXVII, which is XX + V + II.
    Roman numerals are usually written largest to smallest from left to right. However,
    the numeral for four is not IIII. Instead, the number four is written as IV. Because
    the one is before the five we subtract it making four. The same principle applies to
    the number nine, which is written as IX. There are six instances where subtraction is used:
    - I can be placed before V (5) and X (10) to make 4 and 9.
    - X can be placed before L (50) and C (100) to make 40 and 90.
    - C can be placed before D (500) and M (1000) to make 400 and 900.
    Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
    Example 1:
        Input: "III"
        Output: 3
    Example 2:
        Input: "IV"
        Output: 4
    Example 3:
        Input: "IX"
        Output: 9
    Example 4:
        Input: "LVIII"
        Output: 58
        Explanation: C = 100, L = 50, XXX = 30 and III = 3.
    Example 5:
        Input: "MCMXCIV"
        Output: 1994
        Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    """
    
    Roman_number = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, 'IV':4, 'IX':9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
    integer = 0
    i = 0
    while i < len(roman_string):
        if i+1 < len(roman_string) and roman_string[i:i+2] in Roman_number:
            integer += Roman_number[roman_string[i:i+2]]
            i += 2
        else:
            integer += Roman_number[roman_string[i]]
            i += 1
    
    return integer
