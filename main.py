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
personnage1 = pygame.image.load('images/personnage/sonic-stop.png').convert_alpha()
personnage2 = pygame.image.load('images/personnage/sonic-stop-esquerda.png').convert_alpha()

# Liste des frames d'idle
perso_idle_images = [personnage1, personnage2]
current_idle_index = 0
rect_perso = personnage1.get_rect()

# Temps pour l'animation
temps_derniere_image = pygame.time.get_ticks()
delai_animation = 500  # en ms


rect_perso.center = (largeur // 2, hauteur // 2)  # centré dans la fenêtre
vitesse = 0.5
en_mouvement = False
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
        en_mouvement = True
    # Animation idle uniquement si le personnage ne bouge pas
    if not en_mouvement:
        maintenant = pygame.time.get_ticks()
        if maintenant - temps_derniere_image > delai_animation:
            current_idle_index = (current_idle_index + 1) % len(perso_idle_images)
            temps_derniere_image = maintenant

    # Choix de l’image
    image_perso = perso_idle_images[current_idle_index]

    # Affichage de l'image de fond
    fenetre.blit(fond, (0, 0))

    # Affichage du personnage par-dessus
    fenetre.blit(image_perso, rect_perso.topleft)

    # Rafraîchir l'affichage
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()
