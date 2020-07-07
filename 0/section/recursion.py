def factorial(n):
    if n < 1:
        return 1
    return n * factorial(n - 1)



def reverse(s):
    if len(s) == 0:
        return s
    return s[-1] + reverse(s[:-1])



def palindrome(s):
    return s == reverse(s)


print("Factorial Tests:")
print(f"0! = 1 = {factorial(0)}")
print(f"1! = 1 = {factorial(1)}")
print(f"3! = 6 = {factorial(3)}")
print(f"5! = 120 = {factorial(5)}")
print(f"2! = 2 = {factorial(2)}\n")


print("Reverse Tests:")
print(f"Hello -> olleH = {reverse('Hello')}")
print(f"\"\" -> \"\" = {reverse('')}")
print(f"A -> A = {reverse('A')}")
print(f"Hey there -> ereht yeH = {reverse('Hey there')}")
print(f"racecar -> racecar = {reverse('racecar')}\n")

print("Palindrome Tests:")
print(f"Hello -> False = {palindrome('Hello')}")
print(f"racecare -> True = {palindrome('racecar')}")
print(f"\"\" -> True = {palindrome('')}")
print(f"tacocat -> True = {palindrome('tacocat')}")
print(f"howdy -> False = {palindrome('howdy')}")
