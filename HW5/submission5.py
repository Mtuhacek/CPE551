"""
Python Functions and Recursions
"""
"""
QUESTION 1: 
========================================================================================================
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
["((()))","(()())","(())()","()(())","()()()"]
Write a function named generateParenthesis that takes an integer as an input and returns a list of strings 
as an output. Note that you can define a function inside a function if necessary.
"""
def generateParenthesis(N):   
    output = []
    def backwards(parenthesis, opening, closing):
        if len(parenthesis) == 2 * N:
            output.append(parenthesis)
            return
        if opening < N:
            backwards(parenthesis + '(', opening + 1, closing)
        if closing < opening:
            backwards(parenthesis + ')', opening, closing + 1)
    backwards('', 0, 0)
    return output


"""
QUESTION 2: 
========================================================================================================
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.
Example 1:
========================================
Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:
=========================================
Input: "race a car"
Output: false
Write a function named isPalindrome that takes a string as an input and returns a bool as an output.
"""
import string
def isPalindrome(stringInput):
    if stringInput == '':
        return True
    else:
        stringNew = stringInput.replace(' ', '')
        stringNew = stringNew.lower()
        stringNew = stringNew.translate(str.maketrans('','', string.punctuation))
        if (stringNew == stringNew[::-1]):
            return True
        else:
          return False
