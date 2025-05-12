
import math

t = int(input())  # Read number of test cases
results = []

for _ in range(t):
    n, k = map(int, input().split(" "))  # Read n and k
    if n % 2 == 1 and k % 2 == 1:
        results.append(str(math.ceil((n - k) / (k - 1)) + 1))
    elif n % 2 == 0 and k % 2 == 0:
        results.append(str(math.ceil(n / k)))
    elif n % 2 == 1 and k % 2 == 0:
        results.append(str(math.ceil((n - (k - 1)) / k) + 1))
    else:  # Case when n is even and k is odd
        results.append(str(math.ceil(n / (k - 1))))

print("\n".join(results))  # Print results, each on a new line
