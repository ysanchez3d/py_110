# Running Totals
# Write a function that takes a list of numbers and returns a list with the same number of elements, but with each element's value being the running total from the original list.

def running_total(totals):
    results = []

    for i in range(len(totals)):
        if i == 0:
            results.append(totals[i])
        else:
            results.append(results[-1] + totals[i])
            
    return results



# Examples
print(running_total([2, 5, 13]) == [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20])
      == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True
# Show