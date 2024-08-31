import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
width, height = screen.get_size()

# Set up the font (50% bigger)
font_size = 21  # Increased from 14
font = pygame.font.Font(None, font_size)

# Set up the matrix rain
class Drop:
    def __init__(self, x, alphabet):
        self.x = x
        self.y = random.randint(-100, -10)
        self.speed = random.randint(2, 7)  # Slowed down by 50%
        self.alphabet = alphabet
        self.chars = [random.choice(self.alphabet) for _ in range(30)]  # Increased from 20 to 30
        self.opacities = [random.randint(50, 255) for _ in range(30)]  # Increased from 20 to 30

    def fall(self):
        self.y += self.speed
        if self.y > height:
            self.y = random.randint(-100, -10)
        
        # Update characters and opacities (50% slower change rate)
        if random.random() < 0.05:  # Changed from 0.1
            self.chars[0] = random.choice(self.alphabet)
        
        for i in range(len(self.opacities)):
            # Reduced fading speed by 50%
            self.opacities[i] = max(0, self.opacities[i] - random.randint(1, 3))  # Slowed down fading
        
        # Refresh faded characters
        if self.opacities[-1] == 0:
            self.chars.pop()
            self.opacities.pop()
            self.chars.insert(0, random.choice(self.alphabet))
            self.opacities.insert(0, 255)

    def draw(self, surface):
        for i, (char, opacity) in enumerate(zip(self.chars, self.opacities)):
            y = self.y + i * font_size
            if 0 <= y < height:
                color = (0, min(255, opacity + 50), 0)
                text = font.render(char, True, color)
                text.set_alpha(opacity)
                surface.blit(text, (self.x, y))

def main(alphabet=None):
    if alphabet is None:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    drops = [Drop(x, alphabet) for x in range(0, width, font_size)]

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

        screen.fill((0, 0, 0))

        for drop in drops:
            drop.fall()
            drop.draw(screen)

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()