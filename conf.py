# GEN TILES CONFS

# number of divisions per channel (R, G and B)
# DEPTH = 4 -> 4 * 4 * 4 = 64 colors
DEPTH = 4
# list of rotations, in degrees, to apply over the original image
ROTATIONS = [0]


#############################


# TILER CONFS

# number of divisions per channel
# (COLOR_DEPTH = 32 -> 32 * 32 * 32 = 32768 colors)
COLOR_DEPTH = 32
# Scale of the image to be tiled (1 = default resolution)
IMAGE_SCALE = 1
# tiles scales (1 = default resolution)
RESIZING_SCALES = [0.05]
# number of pixels shifted to create each box (tuple with (x,y))
# if value is None, shift will be done accordingly to tiles dimensions
PIXEL_SHIFT = None
# if tiles can overlap
OVERLAP_TILES = False
# render image as its being built
RENDER = False
# multiprocessing pool size
POOL_SIZE = 4

# out file name
OUT = 'out_lego_fixed_smallest.png'
# image to tile (ignored if passed as the 1st arg)
IMAGE_TO_TILE = None
# folder with tiles (ignored if passed as the 2nd arg)
TILES_FOLDER = None
