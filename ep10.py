from matplotlib import pyplot as plt
import math

def f(x):
    try:
        return math.sqrt(x)
    except:
        if x > 0:
            return math.sqrt(x)

x = [i for i in range(-100, 101)] # 0 to 10
y = [f(x) for x in x] 

plt.plot(x, y, label='f(x) = sqrt(x)') # WolframAlpha
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()

# Showing the plot
plt.show()

