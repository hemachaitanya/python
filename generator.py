# def odd_numbers_gererator(start, end):
#     for number in range(start, end+1):
#         if number % 2 != 0:
#             yeild = number

# for number in odd_numbers_gererator(10,23):
#     print(number)

def odd_numbers(start, end):
    results = []
    for number in range (start, end+1):
        if number%2 != 0:
            results.append(number)
    return results

odd_numbers(10,23)