import argparse
import cv2

parser = argparse.ArgumentParser(description="Gets a photo from the user and resizes it.")

parser.add_argument("-i", "--image", required=True, type=str, help="Image file to resize")
parser.add_argument("-hi", "--height", required=True, type=int, help="Height in pixels")
parser.add_argument("-wi", "--width", required=True, type=int, help="Width in pixels")

args = parser.parse_args()

image = cv2.imread(args.image)
resized_image = cv2.resize(image, [args.width, args.height])

cv2.imwrite('output.jpg', resized_image)