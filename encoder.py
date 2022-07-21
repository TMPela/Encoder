import pygame, os, pyautogui, PIL

pygame.init()

size = [840, 1188]
screen = pygame.display.set_mode(size)

files = os.listdir('InputEncoder')

n01Count = 0

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
            if color[0] >= 95 and color[0] <= 135 and color[1] >= 55 and color[1] <= 95 and color[2] >= 0 and color[2] <= 35:
                l.append('012')
            elif color[0] >= 46 and color[0] <= 68 and color[1] >= 60 and color[1] <= 78 and color[2] >= 8 and color[2] <= 32:
                l.append('017')
            elif color[0] >= 45 and color[0] <= 58 and color[1] >= 45 and color[1] <= 58 and color[2] >= 8 and color[2] <= 25:
                l.append('N19')
            elif color[0] >= 98 and color[0] <= 112 and color[1] >= 30 and color[1] <= 42 and color[2] >= 18 and color[2] <= 28:
                l.append('L46')
            elif color[0] >= 142 and color[0] <= 155 and color[1] >= 92 and color[1] <= 102 and color[2] >= 98 and color[2] <= 112:
                l.append('C28')
            elif color[0] >= 215 and color[0] <= 228 and color[1] >= 125 and color[1] <= 135 and color[2] >= 28 and color[2] <= 48:
                l.append('N07')
            elif color[0] >= 218 and color[0] <= 230 and color[1] >= 125 and color[1] <= 135 and color[2] >= 70 and color[2] <= 85:
                l.append('R26')
            elif color[0] >= 112 and color[0] <= 125 and color[1] >= 70 and color[1] <= 85 and color[2] >= 72 and color[2] <= 88:
                l.append('M29')
            elif color[0] >= 0 and color[0] <= 36 and color[1] >= 20 and color[1] <= 44 and color[2] >= 28 and color[2] <= 56:
                l.append('N01')
                n01Count += 1
            elif color[0] >= 34 and color[0] <= 70 and color[1] >= 34 and color[1] <= 70 and color[2] >= 34 and color[2] <= 70:
                l.append(' 04')
            elif color[0] >= 60 and color[0] <= 128 and color[1] >= 60 and color[1] <= 105 and color[2] >= 60 and color[2] <= 98:
                l.append(' 04')
            elif color[0] >= 210 and color[0] <= 255 and color[1] >= 210 and color[1] <= 255 and color[2] >= 210 and color[2] <= 255:
                l.append('B34')   
            elif color[0] >= 0 and color[0] <= 20 and color[1] >= 0 and color[1] <= 32 and color[2] >= 0 and color[2] <= 28:
                l.append('N10') 
            elif color[0] >= 88 and color[0] <= 102 and color[1] >= 174 and color[1] <= 188 and color[2] >= 200 and color[2] <= 218:
                l.append('C15') 
            elif color[0] >= 58 and color[0] <= 72 and color[1] >= 108 and color[1] <= 128 and color[2] >= 190 and color[2] <= 208:
                l.append('C41') 
            elif color[0] >= 0 and color[0] <= 10 and color[1] >= 58 and color[1] <= 72 and color[2] >= 130 and color[2] <= 208:
                l.append('M43') 
            elif color[0] >= 0 and color[0] <= 10 and color[1] >= 110 and color[1] <= 126 and color[2] >= 160 and color[2] <= 174:
                l.append('M16')
            elif color[0] >= 148 and color[0] <= 212 and color[1] >= 148 and color[1] <= 216 and color[2] >= 148 and color[2] <= 218:
                l.append(' C2')
            elif color[0] >= 80 and color[0] <= 144 and color[1] >= 80 and color[1] <= 144 and color[2] >= 80 and color[2] <= 144:
                l.append(' M3')
            elif color[0] >= 60 and color[0] <= 95 and color[1] >= 46 and color[1] <= 65 and color[2] >= 66 and color[2] <= 95:
                l.append('N09')
            else:
                l.append(' - ')
            xc += 1
        codeList.append(l)
        yc += 1

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



