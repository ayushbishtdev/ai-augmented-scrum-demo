def calculate_average(numbers):
    if not numbers:
        return 0.0
    total = 0.0
    count = 0
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError(f'Invalid element: {number}. All elements must be numeric.')
        total += number
        count += 1
    return total / count