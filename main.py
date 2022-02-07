import easygui as eg
from os.path import splitext
from os import walk, mkdir
import utils
import cv2 as cv

"""
	+ Noise
	+ Cropping
	+ Flipping
	+ Brightness
	+ Contrast
	+ Saturation
	+ Hue
	+ GrayScale
	+ Random Erasing
	- Padding
	- Scaling
	- Rotation
	- Translation
"""

directory = eg.diropenbox(msg="Choose directory", title="Directory select box", default='.')

fileExtList = list(utils.Other.file_extentions(directory))

if len(fileExtList) == 0:
	raise "There are no file here!"
if len(fileExtList) == 1:
	fileExtList.append('')  # Dummy item, because multchoicebox need at least 2 item

fileExt = eg.multchoicebox(msg="Select file extentions", title="Select file extentions", choices=fileExtList)

choices = [i for i in dir(utils.DataAugmentation) if i[0] != '_']

selects = eg.multchoicebox(msg="Select augmentation types", title="augmentation types select box", choices=choices)

try:
	# Creating directories
	for i in selects:
		mkdir(directory + '/' + i)

	_, _, filenames = next(walk(directory))
	da = utils.DataAugmentation()
	for f in filenames:
		filename, ext = splitext(f)
		if ext in fileExt and filename[0] != '.':
			img = cv.imread(directory + '/' + f)
			for func_name in selects:
				method = utils.Other.get_method_with_its_name(func_name)
				out = method(da, img)
				cv.imwrite(directory + '/' + func_name + '/' + f, out)

except Exception as e:
	print("Error:", e)
