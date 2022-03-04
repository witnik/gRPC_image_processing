import numpy as np
from PIL import Image
import io
import image_pb2
from scipy.signal import convolve2d

# helper function to convert an Image object to NLImage
def image_to_NLImage(image):
	image_arr = np.array(image)
	buf= io.BytesIO()
	image.save(buf, format=f"{image.format}")
	byte_im = buf.getvalue()

	return image_pb2.NLImage(color=image.mode == "RGB", data=byte_im, width=image.width, height=image.height)

# mean filter on a given 2D array
def meanfilter_arr(arr):
	kernel = np.ones((3,3)) 
	count = convolve2d(np.ones(arr.shape), kernel, mode='same')
	out = convolve2d(arr, kernel, mode='same') / count

	return out

def NLImage_image(NLImg):
	try:
		res_image = Image.open(io.BytesIO(NLImg.data))
		res_image.load()
	except:
		raise ValueError("Invalid bytes data")

	if (res_image.mode == "RGB") != NLImg.color:
		raise ValueError("Invalid color data")

	if NLImg.width != res_image.width or NLImg.height != res_image.height:
		raise ValueError("Invalid size data")

	return res_image