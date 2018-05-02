import pygame, sys, random, math

pygame.init()

size = width, height = 400, 200

screen = screen = pygame.display.set_mode(size)
pixel_array = pygame.PixelArray(screen)

points = []
point_frequency = 1
radiance = 5

def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

for x in range(0, len(pixel_array)):
    for y in range(0, len(pixel_array[x])):
        if random.randint(0, 100) < point_frequency:
            points.append((x,y))

for point in points:
    pixel_array[point[0], point[1]] = pygame.Color(255, 255, 255)

def draw_stuff():
    #Find the closest point for each pixel and set shading based on distance to that point
    for x in range(0, len(pixel_array)):
        for y in range(0, len(pixel_array[x])):
            print("Started point " + str(x) + ", " + str(y))
            smallest_distance = dist(x, y, points[0][0], points[0][1])
            for point in points:
                potential_distance = dist(x, y, point[0], point[1])
                if potential_distance < smallest_distance:
                    smallest_distance = potential_distance
            color = int(smallest_distance) * radiance
            color = 0 if color < 0 else color if color < 256 else 255
            pixel_array[x, y] = pygame.Color(color, color, color)

draw_stuff()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    #screen.fill(pygame.Color(0,0,0))
    
    pygame.display.flip()