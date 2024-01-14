# Configuration file of the whole project
import scipy.io as scio
import matplotlib.pyplot as plt
import numpy as np
import os
import shutil
from PIL import Image
import random
from sklearn import svm 

length = 1024 # The length of each separated interval in time domain
frames = 25 # the length of a frame(帧)
thres = 4 # Lower bound of the efficient signal
sampling_rate = 51.2*1e3
fft_size = 2**14 #FFT sampling length
frame_shift = 10 # the length of frame shift