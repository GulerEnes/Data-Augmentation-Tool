import cv2 as cv
import os as os
import skimage as skimage


class DataAugmentation:
	def crop(self, img):
		pass

	def random_erasing(self, img):
		pass

	def contrast(self, image, alpha, beta):
		# alpha value [1.0-3.0], beta value [0-100]
		return cv.convertScaleAbs(image, alpha=alpha, beta=beta)

	def flip_horizontal(self, img):
		return cv.flip(img, 1)

	def flip_vertical(self, img):
		return cv.flip(img, 0)

	def flip_origin(self, img):
		return cv.flip(img, -1)

	def noise(self, img):
		return skimage.util.random_noise(img, mode="gaussian")

	def rotate_90_clockwise(self, img):
		return cv.rotate(img, cv.ROTATE_90_CLOCKWISE)

	def rotate_90_counter_clockwise(self, img):
		return cv.rotate(img, cv.ROTATE_90_COUNTERCLOCKWISE)

	def brightness(self, img, value=0):
		hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
		h, s, v = cv.split(hsv)
		v = cv.add(v, value)
		v[v > 255] = 255
		v[v < 0] = 0
		final_hsv = cv.merge((h, s, v))
		img = cv.cvtColor(final_hsv, cv.COLOR_HSV2BGR)
		return img

	def saturation(self, img, value=0):
		hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
		h, s, v = cv.split(hsv)
		s = cv.add(s, value)
		s[s > 255] = 255
		s[s < 0] = 0
		final_hsv = cv.merge((h, s, v))
		img = cv.cvtColor(final_hsv, cv.COLOR_HSV2BGR)
		return img

	def hue(self, img, value=0):
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
	def run_a_func_with_name(func_name):
		obj = DataAugmentation()
		method = getattr(DataAugmentation, func_name)
		return method(obj)
