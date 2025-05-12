t = int(input())
results = []

for _ in range(t):
    n, x, k = map(int, input().split())
    commands = input().strip()
    
    # Simulate to find when we first reach position 0
    first_zero = -1
    pos = x
    for i in range(min(k, n * abs(x) * 2)):  # Upper bound on steps to reach 0
        if commands[i % n] == 'R':
            pos += 1
        else:
            pos -= 1
            
        if pos == 0:
            first_zero = i + 1
            break
    
    # If we never reach 0
    if first_zero == -1 or first_zero > k:
        results.append(0)
        continue
    
    # We reached 0 once
    count = 1
    
    # If we used all k steps to reach 0 the first time
    if first_zero == k:
        results.append(count)
        continue
    
    # We need to determine how often we'll reach 0 after resetting
    # Start from 0 and see if/when we reach 0 again
    pos = 0
    zero_positions = []
    
    # Simulate at most 2*n steps to find any cycles
    for i in range(min(2*n, k - first_zero)):
        if commands[i % n] == 'R':
            pos += 1
        else:
            pos -= 1
            
        if pos == 0:
            zero_positions.append(i + 1)
    
    # If we don't reach 0 again
    if not zero_positions:
        results.append(count)
        continue
    
    # Calculate remaining time after first_zero
    remaining = k - first_zero
    
    # Calculate how many zeros we'll see in the remaining time
    if len(zero_positions) == 1:
        # Only one zero in the sequence
        first_cycle_zero = zero_positions[0]
        # We reset at each zero, so we need to count how many complete sequences fit
        count += remaining // first_cycle_zero
        
        # Check if there's another zero in the remainder
        remainder = remaining % first_cycle_zero
        if remainder > 0:
            pos = 0
            for i in range(remainder):
                if commands[i % n] == 'R':
                    pos += 1
                else:
                    pos -= 1
                    
                if pos == 0:
                    count += 1
                    break  # We reset after hitting 0
    else:
        # Multiple zeros - need to find pattern
        first_cycle_zero = zero_positions[0]
        count += remaining // first_cycle_zero
        
        remainder = remaining % first_cycle_zero
        pos = 0
        for i in range(remainder):
            if commands[i % n] == 'R':
                pos += 1
            else:
                pos -= 1
                
            if pos == 0:
                count += 1
                break  # We reset after hitting 0
    
    results.append(count)

for result in results:
    print(result)