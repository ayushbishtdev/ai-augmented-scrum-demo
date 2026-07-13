def calculate_average(numbers):
    if not numbers:
        return 0.0
    total = 0.0
    count = 0
    for number in numbers:
        if isinstance(number, (int, float)):
            total += number
            count += 1
        else:
            raise TypeError(f'Invalid element: {number}. All elements must be int or float.')
    return total / count if count > 0 else 0.0