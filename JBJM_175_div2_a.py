def count_fizzbuzz(n):
    # The numbers where i mod 3 = i mod 5 follow a cycle of length 15
    # There are exactly 3 such numbers in each cycle: 0, 6, and 12 (when considering 0-14)
    
    complete_cycles = n // 15
    remainder = n % 15
    
    # Each complete cycle contributes 3 numbers
    count = 3 * complete_cycles
    
    # Check how many additional numbers in the remainder portion
    for i in range(remainder + 1):  # +1 because we count from 0 to remainder (inclusive)
        if i % 3 == i % 5:
            count += 1
            
    return count

t = int(input())
results = []

for _ in range(t):
    n = int(input())
    results.append(count_fizzbuzz(n))

for result in results:
    print(result)