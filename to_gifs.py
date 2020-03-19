import sys
import imageio
import datetime
from utils.color_logger import *

logger = colorlog.getLogger("to_gifs")
e = sys.exit

# THIS NEEDS TOO MUCH TIME
# TODO make it fast


def create_gif(filenames, duration):
    images = []
    for filename in filenames:
        images.append(imageio.imread(filename))
    output_file = 'Gif-%s.gif' % datetime.datetime.now().strftime('%Y-%M-%d-%H-%M-%S')
    imageio.mimsave(output_file, images, duration=duration)
    return output_file

