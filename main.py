import colorgram
colors = colorgram.extract('image.jpg', 20)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b 
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

[(236, 35, 108),(145, 28, 64), (239, 75, 35), (6, 148, 93), (232, 238, 234), (231, /hirs
168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74), (253, 223, 0), (85, 28, 93), (173, 36, 97), (246, 219, 44), (44, 172, 112), (215, 130, 165), (215, 56, 27)]