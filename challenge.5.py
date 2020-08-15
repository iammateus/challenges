# Balance Brackets
# A bracket is considered to be any one of the following characters: (, ), {, }, [, or ].
# We consider two brackets to be matching if the first element is an open-bracket, e.g., (, {, or [, and the second bracket is a close-bracket of the same type, e.g., ( and ), [ and ], and { and } are the only pairs of matching brackets.
# Furthermore, a sequence of brackets is said to be balanced if the following conditions are met:
# The sequence is empty, or
# The sequence is composed of two, non-empty, sequences both of which are balanced, or
# The first and last brackets of the sequence are matching, and the portion of the sequence without the first and last elements is balanced.
# You are given a string of brackets. Your task is to determine whether each sequence of brackets is balanced. If a string is balanced, return true, otherwise, return false
# SIGNATURE
# bool isBalanced(String s)
# INPUT
# String s with length between 1 and 1000
# OUTPUT
# A boolean representing if the string is balanced or not
# EXAMPLE 1
# s = {[()]} output: true
# EXAMPLE 2
# s = {}() output: true
# EXAMPLE 3
# s = {(}) output: false
# EXAMPLE 4
# s = ) output: false

characters = {
    "{": "}",
    "[": "]",
    "(": ")"
}

def isBalanced(s):

    while len(s) != 0:
        char = s[0]

        charIndex = None
        piecesToClose = []
        for index in range(len(s)):
            if index != 0 and s[index] in characters:
               piecesToClose.append(s[index])
            
            if characters[char] == s[index] and len(piecesToClose) == 0:
                charIndex = index

            for i in range(len(piecesToClose)):
                if i >= len(piecesToClose):
                    continue
                
                piece = piecesToClose[i]

                if s[index] == characters[piece]:
                    piecesToClose.pop(i)
        
        if charIndex is None:
            return False
        
        s = s[1: charIndex] + (s[charIndex + 1:] if charIndex + 1 <= len(s) - 1 else "")

    return True

s = input("Print the string: ")
print(isBalanced(s))