import sys

def min_cost_to_equal(x, y):
    if x == y:
        return 0
    
    cost = 0
    used_powers = set()
    
    def apply_operations(a):
        local_cost = 0
        while a:
            k = a & -a  # Get lowest power of 2
            if k not in used_powers:
                used_powers.add(k)
                local_cost += k
            a //= 2  # Move up the binary tree
        return local_cost
    
    cost += apply_operations(x)
    cost += apply_operations(y)
    
    return cost

# Read input
input = sys.stdin.read
data = input().split()
t = int(data[0])
index = 1
results = []

for _ in range(t):
    x, y = int(data[index]), int(data[index + 1])
    index += 2
    results.append(str(min_cost_to_equal(x, y)))

# Print all results at once for efficiency
sys.stdout.write("\n".join(results) + "\n")
