import cv2 as cv
import os as os
import skimage as skimage
from random import randint
import numpy as np


class DataAugmentation:
	def random_crop(self, img):
		width, height, chanel = img.shape
		x1 = randint(0, width)
		y1 = randint(0, height)

		edge_size = randint(0, width)
		x2 = x1 + edge_size
		y2 = y1 + edge_size
		temp = img[x1:x2, y1:y2, :]
		return cv.resize(temp, (height, width))

	def random_erasing(self, img):
		temp = img.copy()
		width, height, chanel = temp.shape
		x1 = randint(0, width)
		y1 = randint(0, height)

		x2 = randint(x1, width)
		y2 = randint(y1, height)

		temp[x1:x2, y1:y2, :] = 0
		return temp

	def contrast(self, img):
		# alpha value [1.0-3.0], beta value [0-100]
		return cv.convertScaleAbs(img, alpha=randint(100, 300) / 100, beta=randint(0, 100))

	def flip_horizontal(self, img):
		return cv.flip(img, 1)

	def flip_vertical(self, img):
		return cv.flip(img, 0)

	def flip_origin(self, img):
		return cv.flip(img, -1)

	def noise(self, img):
		out = skimage.util.random_noise(img, mode="gaussian")
		norm_image = cv.normalize(out, None, alpha=0, beta=255, norm_type=cv.NORM_MINMAX, dtype=cv.CV_32F)

		return norm_image.astype(np.uint8)

	def rotate_90_clockwise(self, img):
		return cv.rotate(img, cv.ROTATE_90_CLOCKWISE)

	def rotate_90_counter_clockwise(self, img):
		return cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)

	def random_rotation(self, img):
		angle = randint(30, 330)
		height, width = img.shape[:2]
		rotate_matrix = cv.getRotationMatrix2D(center=(width / 2, height / 2), angle=angle, scale=1)
		return cv.warpAffine(src=img, M=rotate_matrix, dsize=(width, height))

	def brightness(self, img):
		value = randint(-100, 100)
		hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
		h, s, v = cv.split(hsv)
		v = cv.add(v, value)
		v[v > 255] = 255
		v[v < 0] = 0
		final_hsv = cv.merge((h, s, v))
		img = cv.cvtColor(final_hsv, cv.COLOR_HSV2BGR)
		return img

	def saturation(self, img):
		value = randint(-100, 100)
		hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
		h, s, v = cv.split(hsv)
		s = cv.add(s, value)
		s[s > 255] = 255
		s[s < 0] = 0
		final_hsv = cv.merge((h, s, v))
		img = cv.cvtColor(final_hsv, cv.COLOR_HSV2BGR)
		return img

	def hue(self, img):
		value = randint(-100, 100)
		hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
		h, s, v = cv.split(hsv)
		h = cv.add(h, value)
		h[h > 255] = 255
		h[h < 0] = 0
		final_hsv = cv.merge((h, s, v))
		img = cv.cvtColor(final_hsv, cv.COLOR_HSV2BGR)
		return img

	def grayScale(self, img):
		return cv.cvtColor(img, cv.COLOR_BGR2GRAY)


class Other:
	@staticmethod
	def file_extentions(directory):
		fileExts = set()
		_, _, filenames = next(os.walk(directory))

		for f in filenames:
			_, ext = os.path.splitext(f)
			fileExts.add(ext)

		if '' in fileExts:  # deleting directory extension if exists
			fileExts.remove('')

		return fileExts

	@staticmethod
	def get_method_with_its_name(func_name):
		return getattr(DataAugmentation, func_name)
