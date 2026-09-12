# import random
# from statistics import mean, median


# def generate_random_numbers(count=20, minimum=1, maximum=100):
#     return [
#         random.randint(minimum, maximum)
#         for _ in range(count)
#     ]


# def calculate_statistics(numbers):
#     return {
#         "count": len(numbers),
#         "sum": sum(numbers),
#         "average": mean(numbers),
#         "median": median(numbers),
#         "largest": max(numbers),
#         "smallest": min(numbers),
#         "even_numbers": len([number for number in numbers if number % 2 == 0]),
#         "odd_numbers": len([number for number in numbers if number % 2 != 0]),
#     }


# def display_numbers(numbers):
#     print("\nGenerated numbers:")
#     for index, number in enumerate(numbers, start=1):
#         print(f"{index:2}. {number}")


# def display_statistics(statistics):
#     print("\nStatistics:")
#     print("-" * 30)

#     for name, value in statistics.items():
#         title = name.replace("_", " ").title()

#         if isinstance(value, float):
#             print(f"{title:<20}: {value:.2f}")
#         else:
#             print(f"{title:<20}: {value}")


# def find_duplicates(numbers):
#     duplicates = []

#     for number in numbers:
#         if numbers.count(number) > 1 and number not in duplicates:
#             duplicates.append(number)

#     return duplicates


# def main():
#     print("=" * 40)
#     print("      RANDOM NUMBER ANALYZER")
#     print("=" * 40)

#     numbers = generate_random_numbers(
#         count=30,
#         minimum=1,
#         maximum=200
#     )

#     display_numbers(numbers)

#     statistics = calculate_statistics(numbers)
#     display_statistics(statistics)

#     duplicates = find_duplicates(numbers)

#     print("\nAdditional information:")
#     if duplicates:
#         print("Duplicate numbers:", duplicates)
#     else:
#         print("No duplicate numbers found.")

#     sorted_numbers = sorted(numbers)

#     print("\nSorted numbers:")
#     print(sorted_numbers)

#     print("\nNumber categories:")
#     print("Numbers above average:")
#     average = statistics["average"]

#     above_average = [
#         number for number in numbers
#         if number > average
#     ]

#     print(above_average)


# if __name__ == "__main__":
#     main()


# def fib(n):
#     if n==1:
        
#     elif n == 2:
#         print('0 1')
#     fib_seq = [0,1]
#     for i in range(2,n+1):
#         fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
#     for j in  fib_seq:
#         print(j,end=' ')

# n = int(input('enter n : '))
# fib(n)


# s = 'hello'
# reversed_s = ''
# for i in s:
#     reversed_s = i + reversed_s
# print(reversed_s)

# with open('demo.txt','r') as x:
#     print(x.readlines())

text = "somethingvipin 25something"
print(text.split('something'))




