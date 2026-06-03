import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

random_num = np.random.rand(10)
print(random_num)

style.use('ggplot')
plt.plot(random_num, 'g', label = 'Random Numbers', linestyle = '--', linewidth = 2,alpha = 0.5)
plt.annotate('Max',ha = 'center', va = 'bottom',xytext=np.argmax(random_num), xy=(np.argmax(random_num), random_num[np.argmax(random_num)]), arrowprops=dict(facecolor='black', shrink=0.05))
plt.title('Line Plot Example')
plt.xlabel('Numbers')
plt.ylabel('Range')
plt.legend()
plt.show()

