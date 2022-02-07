import easygui as eg
from os.path import splitext
from os import walk
import utils

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

"""
Verilen directory'nin içerisinde istenilen özelliklere ait klasörler oluştur ve her birini onların
içine ayrı ayrı kaydet. Ayrıca orijinaller için de bir klasör aç
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
	_, _, filenames = next(walk(directory))

	for f in filenames:
		oldName, ext = splitext(f)
		if ext in fileExtList:
			pass

except Exception as e:
	print("Error:", e)
