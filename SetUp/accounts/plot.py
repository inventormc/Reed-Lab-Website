'''
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from io import StringIO
import PIL
import math

def plot(function, x_range):
    x = np.array(x_range)
    y = function(x)
    plt.plot(x,y)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)

    buffer = StringIO.StringIO()
    canvas = plt.get_current_fig_manager().canvas()
    canvas.draw()

    pilImage = PIL.Image.fromstring("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    pilImage.save(buffer, "PNG")
    plt.close()

    return buffer.getvalue()
'''
import random
import django
import datetime

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
def plot(function, x_range)
    fig=Figure()
    ax=fig.add_subplot(111)
    x = np.linspace(-10,10,400)
    y = y_values(function, x_range)
    ax.plot(x,y)
    canvas=FigureCanvas(fig)
    return canvas

def y_values(function, x_range):
    return function(x_range)
