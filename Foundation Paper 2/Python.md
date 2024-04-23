# Python

## MCQs

1. A
2. C
3. D
4. C
5. B

## Section Two

The corrected code is:

def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
    

numbers = [3,7,2,9,5]
print("Maximum number is:", find_max(numbers))

To improve the code 