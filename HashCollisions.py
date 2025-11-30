import hashlib
import random
import string
from collections import Counter
import matplotlib.pyplot as plt

def random_salt(length):
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choice(alphabet) for _ in range(length))

def salted_hash(password, salt):
    h = hashlib.sha256()
    h.update((password + salt).encode('utf-8'))
    return h.hexdigest()

def collision_experiment(password, salt_length, trials=50000):
    hashes = []

    for _ in range(trials):
        salt = random_salt(salt_length)
        hashes.append(salted_hash(password, salt))

    counts = Counter(hashes)
    collisions = sum(c - 1 for c in counts.values() if c > 1)

    collision_rate = collisions / trials
    return collisions, collision_rate

#  different salt lengths
salt_lengths = [1, 2, 3, 4, 6, 8, 12, 16]

password = "tobby"  #   password adding salt to

results = []

for n in salt_lengths:
    collisions, rate = collision_experiment(password, n)
    print(f"Salt length {n}: Collisions = {collisions}, Rate = {rate:.10f}")
    results.append((n, collisions, rate))


x = [r[0] for r in results]  # salt lengths
y = [r[2] for r in results]  # collision rates

plt.plot(x, y, marker='o')
plt.yscale('log')  #  log because collisions drop fast
plt.xlabel("Salt Length (characters)")
plt.ylabel("Collision Rate (log scale)")
plt.title("Salt Collision Probability vs. Salt Length")
plt.grid(True)
plt.show()