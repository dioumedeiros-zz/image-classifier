class Range():

    def isKrustyHair(self, red, green, blue):
        if 0 <= red <= 40 and 80 <= green <= 175 and 50 <= blue <= 185:
            return True

        return False

    def isKrustyTshirt(self, red, green, blue):
        if 160 <= red <= 220 and 100 <= green <= 180 and 150 <= blue <= 200:
            return True

        return False

    def isKrustyFace(self, red, green, blue):
        if 200 <= red <= 255 and 190 <= green <= 255 and 120 <= blue <= 235:
            return True

        return False

    def isNedHair(self, red, green, blue):
        if 0 <= blue <= 81 and 51 <= green <= 127 and 50 <= red <= 140:
            return True

        return False

    def isNedTshirt(self, red, green, blue):
        if 20 <= red <= 75 and 50 <= green <= 148 and 10 <= blue <= 63:
            return True

        return False

    def isNedPants(self, red, green, blue):
        if 40 <= red <= 150 and 55 <= green <= 150 and 50 <= blue <= 150:
            return True

        return False
