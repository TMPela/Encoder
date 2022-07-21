import json

class Colors:
    def __init__(self):
        self.colors = []

    def load(self):
        with open('calibration.json','r') as file:   
            data = json.load(file) 

        for color in data['colors']:
            l = []
            l.append(color['code'])

            minRGB = []
            for value in color['min']:
                minRGB.append(value['r'])
                minRGB.append(value['g'])
                minRGB.append(value['b'])
            l.append(minRGB)

            maxRGB = []
            for value in color['max']:
                maxRGB.append(value['r'])
                maxRGB.append(value['g'])
                maxRGB.append(value['b'])
            l.append(maxRGB)

            self.colors.append(l)
        return self.colors




