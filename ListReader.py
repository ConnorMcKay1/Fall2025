# PasswordCategories.py
# Combined logic for reading password files and categorizing/analyzing them.

print("hellow\n")

PasswordList = []
PasswordLengthList = []

# -----------------------------------------------------------
# Read a plaintext password list (e.g., rockyou.txt, crackstation)
# -----------------------------------------------------------
def TxtReader(filename="rockyou.txt"):
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        for word in f:
            processed_word = word.rstrip("\n")
            PasswordList.append(processed_word)
    print("Loaded passwords from:", filename)
    print("Total passwords:", len(PasswordList))

# -----------------------------------------------------------
# Compute length of every password
# -----------------------------------------------------------
def WordLength(password_list, length_list):
    for word in password_list:
        length_list.append(len(word))
    return length_list

# -----------------------------------------------------------
# Identify max-length password
# -----------------------------------------------------------
def MaxLengthInfo(password_list, length_list):
    max_len = max(length_list)
    index = length_list.index(max_len)
    longest_pw = password_list[index]

    print("Longest password length:", max_len)
    print("Index of longest password:", index)
    print("Longest password:", longest_pw)

    return max_len, index, longest_pw

# -----------------------------------------------------------
# Example usage
# -----------------------------------------------------------
if __name__ == "__main__":
    print("-----------------")
    TxtReader()
    print("-----------------")

    WordLength(PasswordList, PasswordLengthList)
    MaxLengthInfo(PasswordList, PasswordLengthList)
