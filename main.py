import pygame
from pygame.locals import QUIT

# Initialisation de Pygame
pygame.init()

# Définir la taille de la fenêtre
largeur, hauteur = 800, 600

fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption('Fenêtre Pygame')

#chargement d'une image :

# Chargement de l'image de fond
fond = pygame.image.load('images/fonds/fond1.jpg').convert()
fond = pygame.transform.scale(fond, (largeur, hauteur))

# Chargement de l'image du personnage avec transparence
personnage = pygame.image.load('images/personnage/sonic-stop.png').convert_alpha()
rect_perso = personnage.get_rect()

# Position initiale du personnage (au centre de l'écran)
x_perso = (largeur - personnage.get_width()) // 2 -50
y_perso = (hauteur - personnage.get_height()) // 2

rect_perso.center = (largeur // 2, hauteur // 2)  # centré dans la fenêtre
vitesse = 0.5

# Boucle principale
en_cours = True
while en_cours:
    for evenement in pygame.event.get():
        if evenement.type == QUIT:
            en_cours = False

    # Gestion des touches
    touches = pygame.key.get_pressed()
    if touches[pygame.K_RIGHT]:
        rect_perso.x += vitesse

    # Affichage de l'image de fond
    fenetre.blit(fond, (0, 0))

    # Affichage du personnage par-dessus
    fenetre.blit(personnage, rect_perso.topleft)

    # Rafraîchir l'affichage
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()
