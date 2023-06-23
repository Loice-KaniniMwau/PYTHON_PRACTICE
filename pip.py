import string
# input and outputs the second largest number in the list using

# conditional statements and a for loop.
def second_larg(numbers):
    sorting=sorted(numbers)
    second_largest=sorting[-2]
    for num in numbers:
        if(num==second_largest):
            return second_largest

print(second_larg(numbers=[2,63,6,53,13,8]))

# Write a Python program that takes a year as input and
# determines if it is a leap year.
def leapyear(theyear):
    if(theyear % 4==0):
        return f"{theyear} is a leapyear"
    else:
        return theyear

print(leapyear(theyear=2020))

# Write a Python program that takes a string as input and
# checks if it is a palindrome (reads the same forwards and backwards),
# ignoring spaces and punctuation
def palindrome(mystring):
    ignorecase=mystring.casefold()
    remove_punct=ignorecase.translate(str.maketrans('','',string.punctuation))
    if(remove_punct==remove_punct[::-1]):
     print(f'{remove_punct} is a palindrome')
palindrome("Ra..Da'r")