import pygame
from pygame.locals import QUIT

# Initialisation de Pygame
pygame.init()

# Définir la taille de la fenêtre
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption('Fenêtre Pygame')

# Boucle principale
en_cours = True
while en_cours:
    for evenement in pygame.event.get():
        if evenement.type == QUIT:
            en_cours = False

    # Rafraîchir l'affichage
    fenetre.fill((0, 0, 0))  # fond noir
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()
