import matplotlib.pyplot as plt

# Parameters
alphabet_size = 62  # a-zA-Z0-9
hash_size_bytes = 32  # SHA-256
salt_lengths = range(1, 17)  # 1 to 16 characters

table_sizes_bytes = []

for s in salt_lengths:
    num_entries = alphabet_size ** s
    total_bytes = num_entries * hash_size_bytes
    table_sizes_bytes.append(total_bytes)

# converts to GB 
def human_readable(size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024
    return f"{size:.2f} ZB"

table_sizes_hr = [total / 1024**3 for total in table_sizes_bytes]  # GB

plt.figure(figsize=(10,6))
plt.plot(list(salt_lengths), table_sizes_hr, marker='o')
plt.yscale('log')
plt.xlabel("Salt Length (characters)")
plt.ylabel("Rainbow Table Size (GB, log scale)")
plt.title("Rainbow Table Size vs Salt Length")
plt.grid(True)
plt.show()
