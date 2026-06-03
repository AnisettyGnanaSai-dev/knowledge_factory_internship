import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

random_num = np.random.rand(10)
print(random_num)

style.use('ggplot')
plt.plot(random_num, 'g', label = 'Random Numbers', linestyle = '--', linewidth = 2)
plt.title('Line Plot Example')
plt.xlabel('Numbers')
plt.ylabel('Range')
plt.legend()
plt.show()

