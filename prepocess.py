
import cv2
import os

def generator_list_of_imagepath(path):
    image_list = []
    for image in os.listdir(path):
        if not image == '.DS_Store':
            image_list.append(path + image)
    return image_list


def process(test_image_path):
   image_list = generator_list_of_imagepath(test_image_path)
   ii=0
   for image in image_list:
      img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
      ii=ii+1
      cv2.imwrite("D:cnn/test/"+str(ii)+".jpg", img)

   # main function
if __name__ == "__main__":
    process("D:cnn/test1/")