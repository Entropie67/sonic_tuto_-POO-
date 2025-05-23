import pygame
from pygame.locals import *

# Initialisation de Pygame
pygame.init()

# Définir la taille de la fenêtre
largeur, hauteur = 800, 600
clock = pygame.time.Clock()
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption('Fenêtre Pygame')

############################################
#           Decoupage des images           #
############################################

def decouper_spritesheet(hauteur, image, largeur_sprite, hauteur_sprite, nombre_images):
    """Découpe une spritesheet horizontale en une liste de surfaces."""
    images = []
    for i in range(nombre_images):
        rect = pygame.Rect(i * (largeur_sprite + 13), hauteur, largeur_sprite, hauteur_sprite)
        sous_image = image.subsurface(rect).copy()
        images.append(sous_image)
    return images

############################################
#                Classe Sonic              #
############################################

class Sonic:

    def __init__(self, spritesheet, sol_y):
        # Dimensions d’un sprite individuel
        self.sprite_largeur = 32
        self.sprite_hauteur = 45
        self.nombre_frames = 10
        # Extraction des frames d'attente
        self.images_idle = decouper_spritesheet(12, spritesheet, self.sprite_largeur, self.sprite_hauteur, self.nombre_frames)
        self.current_idle_index = 0
        self.temps_derniere_image = pygame.time.get_ticks()
        self.delai_animation = 500  # ms
        self.image = self.images_idle[self.current_idle_index]
        self.rect = self.image.get_rect()
        self.rect.center = (largeur // 2, hauteur // 2)  # position initiale

        self.vitesse = 150
        self.vitesse_y = 0
        self.gravite = 0.5
        self.vitesse_max = 10
        self.sol_y = sol_y
        self.en_mouvement = False

    def mettre_a_jour(self, touches, delta_time):
        self.en_mouvement = False
        if touches[K_LEFT]:
            self.rect.x -= self.vitesse * delta_time
            self.en_mouvement = True
        if touches[K_RIGHT]:
            self.rect.x += self.vitesse * delta_time
            self.en_mouvement = True
        if touches[K_SPACE] and self.rect.bottom >= self.sol_y:
            self.vitesse_y = -10
            self.en_mouvement = True

        self.appliquer_gravite()

        if not self.en_mouvement:
            self.gerer_animation_idle()
        self.image = self.images_idle[self.current_idle_index]

    def appliquer_gravite(self):
        self.vitesse_y += self.gravite
        if self.vitesse_y > self.vitesse_max:
            self.vitesse_y = self.vitesse_max
        self.rect.y += self.vitesse_y
        if self.rect.bottom >= self.sol_y:
            self.rect.bottom = self.sol_y
            self.vitesse_y = 0

    def gerer_animation_idle(self):
        maintenant = pygame.time.get_ticks()
        if maintenant - self.temps_derniere_image > self.delai_animation:
            self.current_idle_index = (self.current_idle_index + 1) % len(self.images_idle)
            self.temps_derniere_image = maintenant

    def dessiner(self, fenetre):
        fenetre.blit(self.image, self.rect.topleft)

############################################
#          Chargement des images           #
############################################

# Chargement de l'image de fond
fond = pygame.image.load('images/fonds/fond1.jpg').convert()
fond = pygame.transform.scale(fond, (largeur, hauteur))

# Chargement de la planche de sprites
spritesheet = pygame.image.load('images/personnage/sonic.png').convert_alpha()

# Position du sol (à adapter selon la taille du sprite et le fond)
sol_y = 530

############################################
#               Boucle Jeu                 #
############################################

# Création du personnage Sonic
sonic = Sonic(spritesheet, sol_y)
en_cours = True

while en_cours:
    for evenement in pygame.event.get():
        if evenement.type == QUIT:
            en_cours = False

    delta_time = clock.tick(60) / 1000  # en secondes
    touches = pygame.key.get_pressed()

    sonic.mettre_a_jour(touches, delta_time)

    fenetre.blit(fond, (0, 0))
    sonic.dessiner(fenetre)
    pygame.display.flip()

pygame.quit()
