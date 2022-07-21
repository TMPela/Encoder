import pygame, os, pyautogui, PIL, json

from colors import Colors

pygame.init()

size = [840, 1188]
screen = pygame.display.set_mode(size)

files = os.listdir('InputEncoder')

n01Count = 0

colors = Colors()
calibration = colors.load()

for f in files:
    #print(f)
    name = f[5:8]

    image = pygame.image.load('InputEncoder/' + f)
    im = PIL.Image.open('InputEncoder/' + f)
    colorList = []
    
    for y in range(image.get_height()):
        l = []
        for x in range(image.get_width()): 
            l.append(im.getpixel((x, y)))
        colorList.append(l)

    codeList = []
    
    yc = 0
    for color in colorList:
        xc = 0
        l = []
        for color in colorList[yc]:
            found = False
            for c in calibration:
                minRGB = c[1]
                maxRGB = c[2]
                if color[0] >= minRGB[0] and color[0] <= maxRGB[0] and color[1] >= minRGB[1] and color[1] <= maxRGB[1] and color[2] >= minRGB[2] and color[2] <= maxRGB[2]:
                    l.append(c[0])
                    found = True
            if found == False:
                l.append(' - ')
            xc += 1
        codeList.append(l)
        yc += 1

    print(len(codeList[0]))

    fSize = 12
    nameFont = pygame.font.SysFont('arial', 26)
    font = pygame.font.SysFont('arial', fSize)

    surfaceList = []
    surfaceMatrix = []

    ycount = 0
    for code in codeList:
        xcount = 0
        l = []
        for code in codeList[ycount]:
            l.append(font.render(code, True, (0, 0, 0)))
            xcount += 1
        surfaceList.append(l)
        ycount += 1

    title = nameFont.render(name, True, (0, 0, 0))

    squareSize = 40

    gridSize = [17, 24]

    xOffset = 28
    yOffset = 60
    spacing = 7

    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    yCount = 0
    for surf in surfaceList:
        xCount = 0
        for surf in surfaceList[yCount]:
            xcenter = 0 #squareSize//2 - ((fSize//2) * 3)
            ycenter = 0 #fSize//2
            screen.blit(surf, (((squareSize + spacing) * xCount) + xOffset ,((squareSize + spacing) * yCount) + yOffset))
            xCount += 1
        yCount += 1

    screen.blit(title, (size[0]/2, 15))

    pygame.display.update()
    pygame.image.save(screen, 'OutputEncoder/Hoja ' + name + '.png')

print('Cantidades de venecitas:')
print(f'    N01: {n01Count}')



