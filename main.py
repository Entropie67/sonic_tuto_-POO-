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


# Boucle principale
en_cours = True
while en_cours:
    for evenement in pygame.event.get():
        if evenement.type == QUIT:
            en_cours = False

    
    # Affichage de l'image de fond
    fenetre.blit(fond, (0, 0))
    # Rafraîchir l'affichage
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()
