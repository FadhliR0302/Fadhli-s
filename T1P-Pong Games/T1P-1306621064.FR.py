#Fadhli Rahman ( 1306621064 )

import pygame

# Initialize Pygame
pygame.init()

# preparing  the  screen
Lebar = 1050 ; Tinggi = 600
screen = pygame.display.set_mode([Lebar, Tinggi])
pygame.display.set_caption('permainan bola billiard')

# Define some colors
white=(250,250,250);   whitdull=(243,243,242)
black=(70,70,70)   ;   blue =(45,127,184) 
gold  =(248,179,35);   green=(0,176,80)
yellow=(254,240,11);   gray=(208,206,206)

def draw_stick_figure(screen,x,y):
    pygame.draw.rect(screen,gray,[1+x,y,105,3],0)
 
#Setting teks
f1 = pygame.font.Font(None,40)
f2 = pygame.font.Font(None,25)
# Penentuan isi tulisan
t1 = f1.render("SIMULASI      BILYARD",True,white)
t2 = f2.render("Stick-bilyard",True,white)

# persiapan lain-lain
click_sound = pygame.mixer.Sound("click.wav")
# insiasi harga awal
xm,ym = 0,0                  # koord mouse
fps = 20
fpsClock = pygame.time.Clock()

pygame.mouse.set_visible(0)


# program utama Pygame
selesai = False
while selesai==False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            selesai=True
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play()
        
    # Set the screen background
    screen.fill(green)

    # gambar meja bilyard
    pygame.draw.rect(screen,white,[50,60,950,470],4)

    # menampilkan tulisan
    screen.blit(t1,[360,10])
    screen.blit(t2,[50,575])
    
    #lubang-lubang di meja bilyard
    pygame.draw.circle(screen,whitdull,[55,65],25)
    pygame.draw.circle(screen,whitdull,[520,55],25)
    pygame.draw.circle(screen,whitdull,[995,65],25)
    
    pygame.draw.ellipse(screen, white, (200,250,50,50))
    pygame.draw.ellipse(screen, gold, (655,253,50,50))
    pygame.draw.ellipse(screen, blue, (700,230,50,50))
    pygame.draw.ellipse(screen, yellow, (700,280,50,50))
    pygame.draw.rect(screen,white,[50,60,950,470],4)

    #stick bilyard                x,y,  Lx, Ly,tebal grs
    pygame.draw.rect(screen,gray,[50,555,105,3],3)

    # Get the current mouse position (x,y)
    player_position = pygame.mouse.get_pos()
    xm=player_position[0]
    ym=player_position[1]

    pos = pygame.mouse.get_pos()
    x=pos[0]
    y=pos[1]

    draw_stick_figure(screen,x,y)

    #Tampilkan semua gambar di screen
    pygame.display.flip()
    fpsClock.tick(fps)

#end program
pygame.quit ()
