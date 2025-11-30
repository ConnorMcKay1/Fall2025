from ListReader import TxtReader

import matplotlib.pyplot as plt



def categorize_password(pw):
    has_lower = any(c.islower() for c in pw)
    has_upper = any(c.isupper() for c in pw)
    has_digit = any(c.isdigit() for c in pw)
    has_symbol = any(not c.isalnum() for c in pw)

    # Class E = unicode / emoji / extended ASCII
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

    for pw in password_list:
        cat = categorize_password(pw)
        counts[cat] += 1

    percentages = {k: (v / total * 100) for k, v in counts.items()}
    return counts, percentages


def plot_categories(counts, percentages):
    labels = list(counts.keys())
    values = [counts[l] for l in labels]
    pct_values = [percentages[l] for l in labels]

    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, values, color='skyblue')

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

    plt.tight_layout()
    plt.show()



