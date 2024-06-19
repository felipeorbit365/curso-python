import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer_music.play()
input()
pygame.event.wait()

# A resolução está correta, mas precisa do arquivo
# na pasta para funcionar. Eu o removi, mas testei
# antes de excluir e funciona.