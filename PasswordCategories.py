from ListReader import PasswordList, TxtReader
from tqdm import tqdm

import matplotlib.pyplot as plt
import string


TxtReader()
passwords = PasswordList


print("Loaded", len(passwords), "passwords")



def categorize_password(pw):
    has_lower = any(c.islower() for c in pw)
    has_upper = any(c.isupper() for c in pw)
    has_digit = any(c.isdigit() for c in pw)
    has_symbol = any(not c.isalnum() for c in pw)

    '''Class	Rule
        A	    Only lowercase letters (a-z)
        B	    Lowercase + digits (0-9) and no uppercase, no symbols
        C	    Lower + upper + digits and no symbols
        D	    Lower + upper + digits + symbols
        E	    Contains unicode/emoji/extended ASCII (anything > ASCII 126)**
    '''

    try:
        pw.encode('ascii')
        is_unicode = False
    except UnicodeEncodeError:
        is_unicode = True

    if is_unicode:
        return 'E'
    if has_lower and not (has_upper or has_digit or has_symbol):
        return 'A'
    if has_lower and has_digit and not (has_upper or has_symbol):
        return 'B'
    if has_lower and has_upper and has_digit and not has_symbol:
        return 'C'
    if has_symbol:
        return 'D'
    return 'A'


def compute_category_stats(password_list):
    counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}
    total = len(password_list)

    for pw in tqdm(password_list, desc="Categorizing passwords", unit="pw"):
        cat = categorize_password(pw)
        counts[cat] += 1

    percentages = {k: (v / total * 100) for k, v in counts.items()}
    return counts, percentages


counts, percentages = compute_category_stats(passwords)



def plot_categories(counts, percentages):
    labels = list(counts.keys())
    values = [counts[l] for l in labels]
    pct_values = [percentages[l] for l in labels]

    colors = {
        'A': 'skyblue',
        'B': 'lightgreen',
        'C': 'orange',
        'D': 'red',
        'E': 'purple'
    }
    bar_colors = [colors[l] for l in labels]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, values, color=bar_colors)

    plt.title("Password Complexity Classes", fontsize=14)
    plt.ylabel("Number of Passwords", fontsize=12)
    plt.xlabel("Complexity Class", fontsize=12)

    for bar, pct in zip(bars, pct_values):
        height = bar.get_height()
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{pct:.2f}%",
            ha='center',
            va='bottom',
            fontsize=11,
            fontweight='bold'
        )

    legend_labels = [
        "A: Only lowercase letters (a-z)",
        "B: Lowercase + digits (0-9), no uppercase, no symbols",
        "C: Lower + upper + digits, no symbols",
        "D: Lower + upper + digits + symbols",
        "E: Unicode/emoji/extended ASCII"
    ]
    plt.legend(bars, legend_labels, title="Category Rules", fontsize=10)

    plt.tight_layout()
    plt.show()


plot_categories(counts, percentages)



