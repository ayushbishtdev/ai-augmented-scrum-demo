def calculate_average(numbers):
    if not numbers:
        return 0.0
    total = 0.0
    count = 0
    for num in numbers:
        if isinstance(num, (int, float)):
            total += num
            count += 1
        else:
            raise TypeError(f"Invalid element '{num}' in list: must be int or float.")
    return total / count if count > 0 else 0.0