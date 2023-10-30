# Importiere das benötigte Modul
import pygame

# Initialisiere das Spiel
pygame.init()

# Definiere die Farben
WEISS = (255, 255, 255)
SCHWARZ = (0, 0, 0)

# Definiere die Bildschirmgröße
BREITE = 800
HOEHE = 600

# Erstelle den Bildschirm
bildschirm = pygame.display.set_mode((BREITE, HOEHE))
pygame.display.set_caption("Flipperspiel")

# Definiere die Klasse für den Flipper
class Flipper(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Lade das Bild für den Flipper
        self.image = pygame.image.load("flipper.png").convert()
        self.image.set_colorkey(SCHWARZ)
        self.rect = self.image.get_rect()
        # Setze die Position des Flippers auf den Bildschirm
        self.rect.x = 350
        self.rect.y = 550

    def update(self):
        # Bewege den Flipper basierend auf der Mausposition
        self.rect.x = pygame.mouse.get_pos()[0] - 50

# Definiere die Klasse für den Ball
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Lade das Bild für den Ball
        self.image = pygame.image.load("ball.png").convert()
        self.image.set_colorkey(WEISS)
        self.rect = self.image.get_rect()
        # Setze die Startposition des Balls
        self.rect.x = 400
        self.rect.y = 300
        # Setze die Geschwindigkeit des Balls
        self.geschwindigkeit_x = 3
        self.geschwindigkeit_y = 3

    def update(self):
        # Bewege den Ball
        self.rect.x += self.geschwindigkeit_x
        self.rect.y += self.geschwindigkeit_y

        # Überprüfe Kollisionen mit den Rändern des Bildschirms
        if self.rect.x >= BREITE - 20 or self.rect.x <= 0:
            self.geschwindigkeit_x *= -1
        if self.rect.y >= HOEHE - 20 or self.rect.y <= 0:
            self.geschwindigkeit_y *= -1

# Erstelle eine Gruppe für die Sprites
alle_sprites = pygame.sprite.Group()
flipper = Flipper()
ball = Ball()
alle_sprites.add(flipper)
alle_sprites.add(ball)

# Starte die Hauptschleife des Spiels
spiel_laeuft = True
clock = pygame.time.Clock()

while spiel_laeuft:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spiel_laeuft = False

    # Aktualisiere alle Sprites
    alle_sprites.update()

    # Lösche den Bildschirm
    bildschirm.fill(SCHWARZ)

    # Zeichne alle Sprites auf den Bildschirm
    alle_sprites.draw(bildschirm)

    # Aktualisiere den Bildschirm
    pygame.display.flip()

    # Begrenze die Bildrate auf 60 FPS
    clock.tick(60)

# Beende das Spiel
pygame.quit()