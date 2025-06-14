max_val = 0
best_i = 0

for i in range(5000):
    current_val = ((10 - 2*i) * (10 - 2*i)) * i
    if current_val > max_val:
        max_val = current_val
        best_i = i

print(best_i)  # Prints the i that gives maximum value
# Or if you really want it divided by 1000:
print(best_i / 1000)