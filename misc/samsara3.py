def generate_numbers_with_one_digit_changed(num):
    """Generate all possible numbers by changing one digit of the given number."""
    str_num = str(num)
    generated = []
    for i in range(len(str_num)):
        for d in '0123456789':
            if str_num[i] != d:
                new_num = int(str_num[:i] + d + str_num[i+1:])
                generated.append(new_num)
    return generated

def solution(numbers):
    # Create dictionary where keys are the number of digits, and values are sets of numbers
    digit_groups = {}
    for num in numbers:
        key = len(str(num))
        if key not in digit_groups:
            digit_groups[key] = set()
        digit_groups[key].add(num)
    
    # Check for each number if there's another number that can be obtained by changing one digit
    count = 0
    for num in numbers:
        key = len(str(num))
        for changed_num in generate_numbers_with_one_digit_changed(num):
            if changed_num in digit_groups[key] and changed_num != num:
                count += 1
    
    # We count every pair twice, so we divide by 2
    return count // 2

# Example
numbers = [1, 151, 241, 1, 9, 22, 351]
print(solution(numbers))  # Expected output: 3
