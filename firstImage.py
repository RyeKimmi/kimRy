img = open('pic.ppm', 'w')
img.write('P3\n500 500\n255\n')
r = 1
g = 1
b = 1
for x in range(500):
    for y in range(500):
        r = (r + 2) % 256
        g = (g * 2) % 256
        b = (r + g) % 256
        img.write(str(r) + ' ' + str(g) + ' ' + str(b) + ' ')
    img.write('\n')
img.close()
