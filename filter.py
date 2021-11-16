from PIL import Image
import numpy as np

def cut_off_img(pixels, size):
    over_height = len(pixels) % size
    over_width = len(pixels[1]) % size
    return pixels[:len(pixels) - over_height, :len(pixels[1]) - over_width]

def get_colors(cutted_img, x, y):
    red = cutted_img[y][x][0]
    green = cutted_img[y][x][1]
    blue = cutted_img[y][x][2]
    return int(red) + int(green) + int(blue)

def set_colors(cutted_img, x, y, sum, step):
    cutted_img[y][x][0] = int(sum // step) * step
    cutted_img[y][x][1] = int(sum // step) * step
    cutted_img[y][x][2] = int(sum // step) * step

image = Image.open("img2.jpg")
pixels = np.array(image)
size = int(input("Размер мозайки: "))
step = 256 / int(input("Градация: "))
cutted_img = cut_off_img(pixels, size)
height = len(pixels)
width = len(pixels[1])
for x in range(width):
    for y in range(height):
        color = get_colors(pixels, x, y) / 3
        set_colors(pixels, x, y, color, step)


res = Image.fromarray(pixels)
res.save('res.jpg')
