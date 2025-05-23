import pygame
from pygame.locals import *

# Initialisation de Pygame
pygame.init()

clock = pygame.time.Clock()

# Définir la taille de la fenêtre
largeur, hauteur = 800, 600

fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption('Super Sonic')

# Chargement de l'image de fond
fond = pygame.image.load('images/fonds/fond1.jpg').convert()
fond = pygame.transform.scale(fond, (largeur, hauteur))

############################################
#           Decoupage des images           #
############################################

def decouper_spritesheet(hauteur, image, largeur_sprite, hauteur_sprite, nombre_images):
    """Découpe une spritesheet horizontale en une liste de surfaces."""
    images = [] # On va mettre les images découper dans cette liste.
    for i in range(nombre_images):
        rect = pygame.Rect(i * (largeur_sprite + 13) , hauteur, largeur_sprite, hauteur_sprite)
        sous_image = image.subsurface(rect).copy()
        images.append(sous_image)
    return images

# Chargement de la planche de sprites
spritesheet = pygame.image.load('images/personnage/sonic.png').convert_alpha()

# Dimensions d’un sprite individuel (par exemple 64x64)
sprite_largeur = 32
sprite_hauteur = 45
nombre_frames = 10

# Extraction des frames
perso_idle_images = decouper_spritesheet(12, spritesheet, sprite_largeur, sprite_hauteur, nombre_frames)
perso_marche_images = decouper_spritesheet(141, spritesheet, sprite_largeur, sprite_hauteur, nombre_frames)
# Liste des frames du personnage qui patiente
current_idle_index = 0 # la frame courante
current_marche_index = 0 # la frame courante
direction = "droite" # direction


############################################
#       fin de découpage des images        #
############################################

############################################
#                Gravité                   #
############################################
# Gravité
vitesse_y = 0
gravite = 0.5
vitesse_max = 10
# Sol 
sol_y = 530



# Chargement de l'image du personnage avec transparence
personnage1 = pygame.image.load('images/personnage/sonic-stop.png').convert_alpha()

rect_perso = personnage1.get_rect() # On réccupère le rectangle du personnage.

# Temps pour l'animation d'attente
temps_derniere_image = pygame.time.get_ticks()
delai_animation = 500  # en ms



rect_perso.center = (largeur // 2, hauteur // 2)  # centré dans la fenêtre
vitesse = 150


# Boucle principale
en_cours = True

while en_cours:
    for evenement in pygame.event.get():
        if evenement.type == QUIT:
            en_cours = False
    
    delta_time = clock.tick(60) / 1000  # en secondes
    en_mouvement = False # Permet de savoir si le personnage est en mouvement ou sur place.
    # Gestion des touches #
   
    touches = pygame.key.get_pressed()
    
    if touches[pygame.K_RIGHT]:
        rect_perso.x += vitesse * delta_time
        en_mouvement = True
        direction = "droite"

    if touches[pygame.K_LEFT]:
        rect_perso.x -= vitesse * delta_time
        en_mouvement = True 
        direction = "gauche"
          
    if  touches[pygame.K_SPACE]:
        if rect_perso.y > 400:
            vitesse_y = -10
            en_mouvement = True

        # Choix et animation de l’image en fonction du mouvement
    maintenant = pygame.time.get_ticks()

    if en_mouvement:
        if maintenant - temps_derniere_image > delai_animation:
            current_marche_index = (current_marche_index + 1) % len(perso_marche_images)
            temps_derniere_image = maintenant
        image_perso = perso_marche_images[current_marche_index]
    else:
        if maintenant - temps_derniere_image > delai_animation:
            current_idle_index = (current_idle_index + 1) % len(perso_idle_images)
            temps_derniere_image = maintenant
        image_perso = perso_idle_images[current_idle_index]

    # Flip si direction gauche
    if direction == "gauche":
        image_perso = pygame.transform.flip(image_perso, True, False)

     # Gestion de la gravité
    vitesse_y += gravite
    if vitesse_y > vitesse_max:
        vitesse_y = vitesse_max
    rect_perso.y += vitesse_y

    # Collision avec le sol
    if rect_perso.bottom >= sol_y:
        rect_perso.bottom = sol_y
        vitesse_y = 0  # Le perso s'arrête quand il touche le sol



    # Affichage de l'image de fond
    fenetre.blit(fond, (0, 0))

    # Affichage du personnage par-dessus
    fenetre.blit(image_perso, rect_perso.topleft)

    # Rafraîchir l'affichage
    pygame.display.flip()

# Fermeture de Pygame
pygame.quit()
