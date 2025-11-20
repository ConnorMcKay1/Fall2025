from ListReader import *
import matplotlib.pyplot as plt
import numpy as np


#from  https://matplotlib.org/stable/plot_types/stats/hist_plot
#*********************
#**********************************************
# plt.style.use('_mpl-gallery')

# # make data
# np.random.seed(1)
# x = 4 + np.random.normal(0, 1.5, 200)

# # plot:
# fig, ax = plt.subplots()

# ax.hist(x, bins=8, linewidth=0.5, edgecolor="white")

# ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
#        ylim=(0, 56), yticks=np.linspace(0, 56, 9))

# plt.show()
#**********************************************
#*********************


#  Just a ba basic plot, not filtered
#*********************
#**********************************************
# x = np.arange(1, NumberOfPasswords + 1)
# y = np.array(PasswordLengthList)

# fig, ax = plt.subplots()
# ax.plot(x, y)
# plt.show()
#**********************************************
#*********************



y = np.array(PasswordLengthList)

fig, ax = plt.subplots(figsize=(10, 6))

ax.hist(y, bins=range(1, MaxPasswordLength), edgecolor='black', alpha=0.7)

# Change labels to rockyou
ax.set_title("Distribution of Password Lengths (RockYou.txt unFiltered)", fontsize=14)
ax.set_xlabel("Amount of Passwords", fontsize=12)
ax.set_ylabel("Password Length (# of characters)", fontsize=12)
ax.set_xticks(range(0, MaxPasswordLength, 2))  # might need to change spacing
ax.grid(axis='y', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()




#Histogram