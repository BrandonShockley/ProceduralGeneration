import pygame, sys, random

pygame.init()
scale = 1
size = width, height = 200, 140*scale

screen = pygame.display.set_mode(size)
pixel_array = pygame.PixelArray(screen)

black = pygame.Color(24, 37, 58)
white = pygame.Color(255, 144, 0)

#Set up initial condition
cells = []
for i in range(0, height):
    cells.append([])
    for j in range(0, width):
        cells[i].append(0)

random.seed()

def generate_init():
    for i in range(0, width):
        cells[0][i] = random.randint(0, 1)

def generate_ruleset(number):
    return {"111":(number>>7)&1, "110":(number>>6)&1, "101":(number>>5)&1, "100":(number>>4)&1, "011":(number>>3)&1, "010":(number>>2)&1, "001":(number>>1)&1, "000":(number&(1))}

ruleset_num = int(sys.argv[1])
ruleset = generate_ruleset(ruleset_num)

rule_110 = {"111":0, "110":1, "101":1, "100":0, "011":1, "010":1, "001":1, "000":0}
rule_30 = {"111":0, "110":0, "101":0, "100":1, "011":1, "010":1, "001": 1, "000":0}
rule_184 = {"111":1, "110":0, "101":1, "100":1, "011":1, "010":0, "001": 0, "000":0}

def generate(ruleset):
    new_cells = []
    for i in range(0, width):
        if i - 1 < 0:
            neighborhood = "0"
        else:
            neighborhood = str(cells[0][i - 1])
        
        neighborhood = neighborhood + str(cells[0][i])

        if i + 1 >= width:
            neighborhood = neighborhood + "1"
        else:
            neighborhood = neighborhood + str(cells[0][i + 1])
        new_cells.append(ruleset[neighborhood])
    #Shift old cells down one
    cells.insert(0, new_cells)
    cells.pop(len(cells) - 1)

def check_for_segregation():
    crossed_bounds = False
    last_index = 0
    for i in cells[0]:
        if last_index != i:
            if crossed_bounds == False:
                crossed_bounds = True
            else:
                return False
        last_index = i
    return True

def check_for_mono():
    last_index = cells[0][0]
    for i in cells[0]:
        if last_index != i:
            return False
        last_index = i
    return True
        
def check_for_alternating():
    last_index = cells[0][0]
    for i in range(1, width):
        if last_index == cells[0][i]:
            return False
        last_index = i
    return True

def draw_cells():
    for i in range(0, len(cells)):
        for j in range(0, width):
            if cells[i][j] == 1:
                set_pixel(j, i)

def set_pixel(x, y):
    #pygame.draw.rect(screen, white, pygame.Rect(x*scale, y*scale, scale, scale))
    for i in range(0, scale):
        for j in range(0, scale):
            if x*scale + i < width and y*scale + j < height:
                pixel_array[x*scale + i, y*scale + j] = white

generate_init()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    generate(ruleset)
    if check_for_segregation():
        #ruleset_num = ruleset_num + 1
        #ruleset = generate_ruleset(ruleset_num)
        print("Restarted")
        generate_init()
    draw_cells()
    pygame.display.flip()
    