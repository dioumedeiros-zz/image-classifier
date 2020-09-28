import os
import cv2

from range_color import Range
from logger import Logger


class ReadImage():
    def __init__(self):
        self.__width = 0
        self.__height = 0
        self.__krustyHair = 0
        self.__krustyTshirt = 0
        self.__krustyFace = 0
        self.__nedHair = 0
        self.__nedTshirt = 0
        self.__nedPants = 0
        self.__renderedImage = None
        self.__features = []
        self.__displayImage = False

    def read(self, img, displayImage=False):
        Logger.log(f'Image received {img}')
        image = cv2.imread(img)

        self.__displayImage = displayImage

        self.__height, self.__width, channels = image.shape

        if self.__displayImage == True:
            Logger.log('Cloned image')
            self.__renderedImage = image.copy()

        Logger.log('Handle width and height')
        for height in range(self.__height):
            for width in range(self.__width):
                pixel = image[height, width]
                self.handleRangeColors(pixel, width, height)

        if self.__displayImage == True:
            cv2.imshow('image', self.__renderedImage)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        return self.normalizeFeatures(img)

    """
      Receive a pixel (R, G, B) and call range_color.py
      https://stackoverflow.com/questions/28981417/how-do-i-access-the-pixels-of-an-image-using-opencv-python/50588950
    """

    def handleRangeColors(self, pixel, index_width, index_height):
        range = Range()
        b, g, r = pixel

        if range.isKrustyHair(r, g, b):
            self.__krustyHair += 1

            if self.__displayImage == True:
                self.set_color(self.__krustyHair,
                               index_width, index_height)

        if index_width > (self.__height / 2) and range.isKrustyTshirt(r, g, b):
            self.__krustyTshirt += 1

            if self.__displayImage == True:
                self.set_color(self.__krustyTshirt,
                               index_width, index_height)

        if index_width > (self.__height / 2 + self.__height / 3) and range.isKrustyFace(r, g, b):
            self.__krustyFace += 1

            if self.__displayImage == True:
                self.set_color(self.__krustyFace, index_width, index_height)

        if range.isNedHair(r, g, b):
            self.__nedHair += 1

            if self.__displayImage == True:
                self.set_color(self.__nedHair,
                               index_width, index_height)

        if index_width < (self.__height / 2 + self.__height / 3) and range.isNedTshirt(r, g, b):
            self.__nedTshirt += 1

            if self.__displayImage == True:
                self.set_color(self.__nedTshirt,
                               index_width, index_height)

        if index_width > (self.__height / 2 + self.__height / 3) and range.isNedPants(r, g, b):
            self.__nedPants += 1

            if self.__displayImage == True:
                self.set_color(self.__nedPants, index_width, index_height)

    """
      TODO: estudar como associar uma variável recebida com o self
      Ex.: receber `variable` e associar self.variable += 1
    """

    def set_color(self, variable, index_width, index_height):
        self.__renderedImage[index_height][index_width] = [0, 255, 128]

    def calcNormalize(self, value):
        if (value != 0.0):
            return (value / (self.__width * self.__height)) * 100

        return 0.0

    """
      Normalizes the features by the number of total pixels of the image to % 
    """

    def normalizeFeatures(self, img):
        Logger.log('Normalize Features')

        self.__krustyHair = self.calcNormalize(self.__krustyHair)
        self.__krustyTshirt = self.calcNormalize(self.__krustyTshirt)
        self.__krustyFace = self.calcNormalize(self.__krustyFace)
        self.__nedHair = self.calcNormalize(self.__nedHair)
        self.__nedTshirt = self.calcNormalize(self.__nedTshirt)
        self.__nedPants = self.calcNormalize(self.__nedPants)

        krustyOrNed = 0.0  # Krusty
        filename = os.path.basename(img)[0]

        if filename == 'n':
            krustyOrNed = 1.0  # Ned

        features = [
            self.__krustyHair,
            self.__krustyTshirt,
            self.__krustyFace,
            self.__nedHair,
            self.__nedTshirt,
            self.__nedPants,
            krustyOrNed
        ]

        Logger.log(features)
        return features
