import pygame
import random
from pygame.locals import *

# Inisialisasi Pygame
pygame.init()

# Membuat ukuran labirin
cell_size = 25
peta_width = 16
peta_height = 16
width = peta_width * cell_size
height = peta_height * cell_size

# Membuat ukuran jendela game
width = 400
height = peta_height * cell_size
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Hunter x Hider")

class Droid:
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def move(self, dx, dy):
        self.rect.x += dx * cell_size
        self.rect.y += dy * cell_size
        
droid_merah = Droid(1, 1, (255, 0, 0))
droid_hijau = Droid(2, 2, (0, 255, 0))

# Class pencari
class Hunter:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("DroidMerah.png")
        self.image = pygame.transform.scale(self.image, (int(cell_size * 0.9), int(cell_size * 0.9)))
        self.rect = self.image.get_rect()
        self.rect.center = ((x * cell_size) + (cell_size // 2), (y * cell_size) + (cell_size // 2))
        self.speed = 1
        self.visited = set()

    def move(self):
        x = self.rect.centerx // cell_size
        y = self.rect.centery // cell_size

        if (x, y) not in self.visited:
            self.visited.add((x, y))

        possible_moves = [(x+dx, y+dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
        valid_moves = [(px, py) for px, py in possible_moves if 0 <= px < peta_width and 0 <= py < peta_height and peta[py][px] == 0 and (px, py) not in self.visited]

        if valid_moves:
            next_pos = random.choice(valid_moves)
            self.rect.center = ((next_pos[0] * cell_size) + (cell_size // 2), (next_pos[1] * cell_size) + (cell_size // 2))
        else:
            self.backtrack()

    def backtrack(self):
        x = self.rect.centerx // cell_size
        y = self.rect.centery // cell_size

        possible_moves = [(x+dx, y+dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
        valid_moves = [(px, py) for px, py in possible_moves if 0 <= px < peta_width and 0 <= py < peta_height and peta[py][px] == 0 and (px, py) in self.visited]

        if valid_moves:
            next_pos = random.choice(valid_moves)
            self.rect.center = ((next_pos[0] * cell_size) + (cell_size // 2), (next_pos[1] * cell_size) + (cell_size // 2))
        else:
            self.visited.clear()
            self.move()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Klasifikasi Kelas Droid Hijau Hider
class penghindar:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("DroidHijau.png")
        self.image = pygame.transform.scale(self.image, (int(cell_size * 0.9), int(cell_size * 0.9)))
        self.rect = self.image.get_rect()
        self.rect.center = ((x * cell_size) + (cell_size // 2), (y * cell_size) + (cell_size // 2))
        self.speed = 1
        self.visited = set()
        

    def move(self):
        x = self.rect.centerx // cell_size
        y = self.rect.centery // cell_size

        if (x, y) not in self.visited:
            self.visited.add((x, y))

        possible_moves = [(x+dx, y+dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
        valid_moves = [(px, py) for px, py in possible_moves if 0 <= px < peta_width and 0 <= py < peta_height and peta[py][px] == 0 and (px, py) not in self.visited]

        if valid_moves:
            next_pos = random.choice(valid_moves)
            self.rect.center = ((next_pos[0] * cell_size) + (cell_size // 2), (next_pos[1] * cell_size) + (cell_size // 2))
        else:
            self.backtrack()

    def backtrack(self):
        x = self.rect.centerx // cell_size
        y = self.rect.centery // cell_size

        possible_moves = [(x+dx, y+dy) for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]]
        valid_moves = [(px, py) for px, py in possible_moves if 0 <= px < peta_width and 0 <= py < peta_height and peta[py][px] == 0 and (px, py) in self.visited]

        if valid_moves:
            next_pos = random.choice(valid_moves)
            self.rect.center = ((next_pos[0] * cell_size) + (cell_size // 2), (next_pos[1] * cell_size) + (cell_size // 2))
        else:
            self.visited.clear()
            self.move()
            
    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Membuat labirin
peta = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Mendapatkan posisi awal droid merah dan droid hijau
while True:
    droid_merah_x, droid_merah_y = random.randint(1, peta_width - 2), random.randint(1, peta_height - 2)
    droid_hijau_x, droid_hijau_y = random.randint(1, peta_width - 2), random.randint(1, peta_height - 2)
    if (
        peta[droid_merah_y][droid_merah_x] == 0
        and peta[droid_hijau_y][droid_hijau_x] == 0
        and (droid_merah_x != droid_hijau_x or droid_merah_y != droid_hijau_y)
    ):
        break
# Membuat objek RedDroid dan GreenDroid
droid_merah = Hunter(droid_merah_x, droid_merah_y)
droid_hijau = penghindar(droid_hijau_x, droid_hijau_y)

# Loop utama game
running = True
clock = pygame.time.Clock()
game_started = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = True

    if game_started:
        # Menggerakkan droid merah dan hijau secara otomatis
             droid_merah.move()
             droid_hijau.move()

    if droid_merah.rect.colliderect(droid_hijau.rect):
            game_started = False
            # Lakukan tindakan setelah permainan berakhir, seperti menggambar pesan akhir
            end_text = pygame.font.Font(None, 50).render("Game Over", True, (255, 255, 255))
            screen.blit(end_text, (width // 2 - end_text.get_width() // 2, height // 2 - end_text.get_height() // 2))

    # Menggambar jendela game
    screen.fill((0, 0, 255))

    # Menggambar labirin
    for y in range(peta_height):
        for x in range(peta_width):
            rect = pygame.Rect(x * cell_size, y * cell_size, cell_size, cell_size)
            if peta[y][x] == 0:
                pygame.draw.rect(screen, (255, 255, 255), rect)
            else:
                pygame.draw.rect(screen, (0, 0, 0), rect)

    if not game_started:
        # Menggambar droid merah dan hijau sebelum permainan dimulai
        droid_merah.draw(screen)
        droid_hijau.draw(screen)

    else:
        if game_started:
            # Menggambar droid merah dan hijau
            droid_merah.draw(screen)
            droid_hijau.draw(screen)
            
    pygame.display.flip()
    clock.tick(10)

# Menutup Pygame
pygame.quit()