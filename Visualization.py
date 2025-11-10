from ListReader import *
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, NumberOfPasswords + 1)
y = np.array(PasswordLengthList)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()