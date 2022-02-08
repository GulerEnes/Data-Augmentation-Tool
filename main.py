import easygui as eg
from os.path import splitext
from os import walk, mkdir
import utils
import cv2 as cv

# GUI inputs
directory = eg.diropenbox(msg="Choose directory", title="Directory select box", default='.')

fileExtList = list(utils.Other.file_extentions(directory))

if len(fileExtList) == 0:
	raise "There are no file here!"
if len(fileExtList) == 1:
	fileExtList.append('')  # Dummy item, because multchoicebox need at least 2 item

fileExt = eg.multchoicebox(msg="Select file extentions that you want to process data augmentation on those",
						   title="Select file extentions",
						   choices=fileExtList)

choices = [i for i in dir(utils.DataAugmentation) if i[0] != '_']

selects = eg.multchoicebox(msg="Select augmentation types that you want to process",
						   title="augmentation types select box",
						   choices=choices)

# if directory_structure == True, then create one folder named 'augmented_images'
# Otherwise create folders seperately for each selected method
directory_structure = eg.boolbox(msg="\tDo you want to create all augmented images under only one folder?\n"
									 "If you choose 'Yes', your original images will keep seperate from others.\n\n"
									 "\tIf you choose 'No', all augmented images will create under separate folders.",
								 title="Directory structure choice window", choices=["Yes (recommended)", "No"])

try:
	# Creating directories
	if not directory_structure:
		for i in selects:
			mkdir(directory + '/' + i)
	else:
		mkdir(directory + '/augmented_images')

	# Data augmentation
	_, _, filenames = next(walk(directory))
	da = utils.DataAugmentation()
	for f in filenames:
		filename, ext = splitext(f)
		if ext in fileExt and filename[0] != '.':
			img = cv.imread(directory + '/' + f)
			for func_name in selects:
				method = utils.Other.get_method_with_its_name(func_name)
				out = method(da, img)
				if directory_structure:
					cv.imwrite(directory + '/augmented_images/' + func_name + '_' + f, out)
				else:
					cv.imwrite(directory + '/' + func_name + '/' + func_name + '_' + f, out)

except Exception as e:
	print("Error:", e)
