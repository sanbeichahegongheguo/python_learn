"""
import matplotlib.pyplot as plt
fig,ax=plt.subplots()
y1=[]
for i in range(50):
    y1.append(i)
    ax.cla()
    ax.bar(y1,label='test',height=y1,width=0.3)
    ax.legend()
    plt.pause(0.3)

"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
if __name__ == "__main__":
    fig = plt.figure()
    ims = []
    for i in range(1,10):
        im = plt.plot(np.linspace(0, i,10), np.linspace(0, np.random.randint(i),10))
        ims.append(im)
    ani = animation.ArtistAnimation(fig, ims, interval=200, repeat_delay=1000)
    ani.save("test.gif",writer='pillow')
    