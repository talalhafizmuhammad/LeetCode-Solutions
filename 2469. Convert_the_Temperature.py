class Solution(object):
    def convertTemperature(self, celsius):
        fah = celsius * 9/5 + 32
        kel = celsius + 273.15
        return [kel, fah]
        
