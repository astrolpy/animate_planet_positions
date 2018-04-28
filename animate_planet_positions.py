import matplotlib.animation as animation
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math


def plot_circle(r):

    x = []
    y = []

    for i in range(360):
        x.append(r*math.cos(math.radians(i)))
        y.append(r*math.sin(math.radians(i)))

    plt.plot(x, y, color='k')
    return

def setup_solar_sys():

    mpl.rcParams['savefig.dpi'] = 500
    fig = plt.figure()

    #plot sun
    plt.scatter([0], [0], marker='o', color='goldenrod', s=1000)
  

    #Plot planet orbits
    plot_circle(3)#merc
    plot_circle(4)#ven
    plot_circle(5)#earth
    plot_circle(6)#mars
    plot_circle(8)#Jup
    plot_circle(10.5)#sat
    plot_circle(13)#ur
    plot_circle(15.5)#nep
    plot_circle(18)#plu



    plt.axis('equal')
    plt.axis('off')


    return

setup_solar_sys()


'''
pow_plots = []

powers = np.linspace(1, 2, 50)

for power in powers:
    pow_plot = plt.scatter( np.linspace(0, 1, 50), [i**power for i in np.linspace(0, 1, 50)])
    pow_plots.append([pow_plot])
    
anim=animation.ArtistAnimation(fig, pow_plots, interval=100,blit=True)
anim.save('vid1.mp4', writer=animation.writers['ffmpeg'](fps=15))
plt.show()


a = np.zeros(shape=(10,10))
fig = plt.figure()
ims = []

for i in range(10):
    for j in range(10):

        a[i][j] = 1
        im = plt.imshow(a)
        ims.append([im])
        
anim=animation.ArtistAnimation(fig, ims, interval=100,blit=True)
anim.save('vid2.mp4', writer=animation.writers['ffmpeg'](fps=15))
'''
plt.show()

