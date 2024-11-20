# How Many?
# Write a function that counts the number of occurrences of each element in a given list. Once counted, print each element alongside the number of occurrences. Consider the words case sensitive e.g. ("suv" != "SUV").

# Example
vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

def count_occurrences(vehicles):
    count = dict()

    for vehicle in vehicles:
        count.setdefault(vehicle, 0)
        count[vehicle] += 1

    for vehicle, totals in count.items():
        print(f"{vehicle} => {totals}")

count_occurrences(vehicles)
# Expected Output
# your output sequence may appear in a different sequence
# car => 4
# truck => 3
# SUV => 1
# motorcycle => 2
