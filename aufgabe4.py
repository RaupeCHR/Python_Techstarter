import math
import emoji
print(emoji.emojize("Python is :thumbs_up:"))

def zeichne_kreis(radius):
    for y in range(-radius, radius+1):
        for x in range(-radius, radius+1):
            distanz = math.sqrt(x**2 + y**2)
            if distanz <= radius:
                print(".", end=" ")
            else:
                print("@", end=" ")
        print()

radius = 10
zeichne_kreis(radius)
