def is_palindrome(num):
    num_str = str(num)
    if num_str == num_str[::-1]:
        return True
    else:
        return False
Number = int(input("Enter a number: "))

if is_palindrome(Number):
    print(f"{Number} is a palindrome")
else:
    print(f"{Number} is not a palindrome")