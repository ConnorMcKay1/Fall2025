import hashlib
import random
import string
import matplotlib.pyplot as plt

#  once the salt space is large, collisions essentially stop happening

def random_salt(length):
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choice(alphabet) for _ in range(length))

def salted_hash(password, salt):
    h = hashlib.sha256()
    h.update((password + salt).encode('utf-8'))
    return h.hexdigest()

def simulate_unique_hashes(password, salt_length, max_users=50000, step=1000):
    unique_counts = []
    hashes = set()

    for users in range(1, max_users + 1):
        salt = random_salt(salt_length)
        h = salted_hash(password, salt)
        hashes.add(h)
        if users % step == 0:
            unique_counts.append((users, len(hashes)))

    return unique_counts

#   simulation for different salt lengths
'''
4-char salt => 62^4 => 14.7 million possibilities

6-char salt => 62^6 => 56 billion possibilities

8-char salt => 62^8 => 218 trillion possibilities
'''

password = "tobby"
salt_lengths = [1, 2, 4, 6, 8]
max_users = 50000
step = 1000

plt.figure(figsize=(10, 6))


#creates an ordered pairs in a list (users, uniques)
for sl in salt_lengths:
    results = simulate_unique_hashes(password, sl, max_users=max_users, step=step)
    users = [r[0] for r in results]
    uniques = [r[1] for r in results]
    print(results)
    plt.plot(users, uniques, marker='o', alpha=0.5 ,label=f"{sl}-char salt")

plt.xlabel("Number of Users")
plt.ylabel("Number of Unique Hashes")
plt.title("Unique Hashed Variations vs. Number of Users")
plt.legend()
plt.grid(True)
plt.show()
