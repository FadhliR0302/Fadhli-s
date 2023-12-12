#Import Modul
import pygame, sys, random
from pygame.locals import *
pygame.init()

#Menseting Tampilan
lebar_layar  = 800
tinggi_layar = 700
window       = pygame.display.set_mode((lebar_layar, tinggi_layar))
pygame.display.set_caption("Bird Game")

#Menetapkan Warna
putih           = (255,255,  255)
hitam           = (  0,  0,    0)
Mint_Cream      = (245, 255, 250)
Sky_Blue        = (135, 206, 235)
gold            = (184, 134,  11)

#Mendefinisikan Variabel Waktu Program
clock = pygame.time.Clock()

#Mendefinisikan Variabel
kec_tembok   = 2
turun        = 9.8
naik         = 18
tembok1      = 0
tembok2      = 0
skor         = 0
tambah_kec   = 1
tambah_skor  = 0
tambah_skor2 = 0
x_latar      = 0
x_latar2     = 1280
sudut        = 0
jarak_tembok = 400
urutan_soal = 1
keluar_game = False

pos_x_gambar   = 100
pos_y_gambar   = 350
pos_y_tembok   = 0
pos_y_tembok2  = 0
pos_y_tembok3  = 0

g             = "Gravitasi = 9.8 m/s.s"
pos_x_pendahuluan,pos_y_pendahuluan = 50,120
pos_x_play,pos_y_play = 325,275
pos_x_melanjutkan,pos_y_melanjutkan = 200,275
pos_x_ya,pos_y_ya = 200,450
pos_x_tidak,pos_y_tidak = 445,450

pos_x_soal,pos_y_soal = 200,275
pos_x_pilihan,pos_y_pilihan = 200,450

pos_x_gameover,pos_y_gameover = 200,250
pos_x_keluar,pos_y_keluar = 200,425


pencet_pendahuluan = True
pencet_play = False
mulai_gerak  = False
masuk_soal = False
pilihan_masuk_soal = True
lanjut_main = False
pilihan_keluar = 1
kesempatan = 4


#Membuat Fungsi Memutar Gambar
def putar_gambar(gambar, sudut):
    cover_gambar       = gambar.get_rect()
    putar              = pygame.transform.rotate(gambar, sudut)
    putar_cover        = cover_gambar.copy()
    putar_cover.center = putar.get_rect().center
    putar              = putar.subsurface(putar_cover).copy()
    return putar

#Membuat Fungsi Ketika Menabrak Tembok
def tabrak(pos_x_gambar,x,x2,pos_y_gambar,pos_y_tembok,tinggi_tembok,tinggi_tembok2,pos_y_tembok2,pos_y_tembok_bawah,pos_y_tembok_bawah2,tinggi_layar,a):
    if (x+50 > pos_x_gambar > x-70):
        if (pos_y_gambar <= pos_y_tembok + tinggi_tembok) or (pos_y_gambar + 30 >= pos_y_tembok_bawah):
            a = 0
    elif (x2+50 > pos_x_gambar > x2-70):
        if (pos_y_gambar <= pos_y_tembok2 + tinggi_tembok2) or (pos_y_gambar + 30 >= pos_y_tembok_bawah2):
            a = 0
    if (pos_y_gambar+30 >= tinggi_layar) or (pos_y_gambar <= tinggi_layar-tinggi_layar):
        a = 0
    return a

#Membuat Fungsi Urutan Soal
def soal(urutan_soal,run,lanjut_main):
    if urutan_soal == 1:
        window.blit(soal1, [pos_x_soal,pos_y_soal])
        window.blit(A, [pos_x_pilihan,pos_y_pilihan])
        window.blit(B, [pos_x_pilihan,pos_y_pilihan+70])
        window.blit(C, [pos_x_pilihan,pos_y_pilihan+140])
        window.blit(A1, [pos_x_pilihan+50,pos_y_pilihan])
        window.blit(B1, [pos_x_pilihan+50,pos_y_pilihan+70])
        window.blit(C1, [pos_x_pilihan+50,pos_y_pilihan+140])
        if pos_x_pilihan + 50 > Kursor[0] > pos_x_pilihan and pos_y_pilihan + 50 > Kursor[1] > pos_y_pilihan:
            if Klik_M[0] == True:
                lanjut_main = True
        elif pos_x_pilihan + 50 > Kursor[0] > pos_x_pilihan and pos_y_pilihan+100 + 50 > Kursor[1] > pos_y_pilihan+70:
            if Klik_M[0] == True:
                run = False
        elif pos_x_pilihan + 50 > Kursor[0] > pos_x_pilihan and pos_y_pilihan+200 + 50 > Kursor[1] > pos_y_pilihan+140:
            if Klik_M[0] == True:
                run = False
        
    elif urutan_soal == 2:
        window.blit(soal2, [pos_x_soal,pos_y_soal])
        window.blit(A, [pos_x_pilihan,pos_y_pilihan])
        window.blit(B, [pos_x_pilihan,pos_y_pilihan+70])
        window.blit(C, [pos_x_pilihan,pos_y_pilihan+140])
        window.blit(A2, [pos_x_pilihan+50,pos_y_pilihan])
        window.blit(B2, [pos_x_pilihan+50,pos_y_pilihan+70])
        window.blit(C2, [pos_x_pilihan+50,pos_y_pilihan+140])
        if pos_x_pilihan + 50 > Kursor[0] > pos_x_pilihan and pos_y_pilihan + 50 > Kursor[1] > pos_y_pilihan:
            if Klik_M[0] == True:
                run = False
        elif pos_x_pilihan + 50 > Kursor[0] > pos_x_pilihan and pos_y_pilihan+100 + 50 > Kursor[1] > pos_y_pilihan+70:
            if Klik_M[0] == True:
                lanjut_main = True
        elif pos_x_pilihan + 50 > Kursor[0] > pos_x_pilihan and pos_y_pilihan+200 + 50 > Kursor[1] > pos_y_pilihan+140:
            if Klik_M[0] == True:
                run = False

    elif urutan_soal == 3:
        window.blit(soal3, [pos_x_soal,pos_y_soal])
        window.blit(A, [pos_x_pilihan,pos_y_pilihan])
        window.blit(B, [pos_x_pilihan,pos_y_pilihan+70])
        window.blit(C, [pos_x_pilihan,pos_y_pilihan+140])
        window.blit(A3, [pos_x_pilihan+50,pos_y_pilihan])
        window.blit(B3, [pos_x_pilihan+50,pos_y_pilihan+70])
        window.blit(C3, [pos_x_pilihan+50,pos_y_pilihan+140])
        if pos_x_pilihan + 50 > Kursor[0] > pos_x_pilihan and pos_y_pilihan + 50 > Kursor[1] > pos_y_pilihan:
            if Klik_M[0] == True:
                run = False
        elif pos_x_pilihan + 50 > Kursor[0] > pos_x_pilihan and pos_y_pilihan+100 + 50 > Kursor[1] > pos_y_pilihan+70:
            if Klik_M[0] == True:
                lanjut_main = True
        elif pos_x_pilihan + 50 > Kursor[0] > pos_x_pilihan and pos_y_pilihan+200 + 50 > Kursor[1] > pos_y_pilihan+140:
            if Klik_M[0] == True:
                run = False
    return run, lanjut_main
    
#Memanggil Gambar
gambar      = pygame.image.load('bird.png')
latar       = pygame.image.load('bg.png')
latar2      = pygame.image.load('bg.png')
huruf       = pygame.font.Font(None,50)
huruf2      = pygame.font.Font(None,30)
pendahuluan = pygame.image.load('pendahuluan.png')
play        = pygame.image.load('play.png')
melanjutkan = pygame.image.load('melanjutkan.png')
ya          = pygame.image.load('ya.png')
tidak       = pygame.image.load('tidak.png')

soal1       = pygame.image.load('soal1.png')
soal2       = pygame.image.load('soal2.png')
soal3       = pygame.image.load('soal3.png')
A           = pygame.image.load('A.png')
B       = pygame.image.load('B.png')
C       = pygame.image.load('C.png')
A1       = pygame.image.load('1A.png')
B1       = pygame.image.load('1B.png')
C1       = pygame.image.load('1C.png')
A2       = pygame.image.load('2A.png')
B2       = pygame.image.load('2B.png')
C2       = pygame.image.load('2C.png')
A3       = pygame.image.load('3A.png')
B3       = pygame.image.load('3B.png')
C3       = pygame.image.load('3C.png')
gameover = pygame.image.load('gameover.png')
keluar   = pygame.image.load('keluar.png')



#Menetapkan Variabel untuk Keluar Program
run = True

#Program Utama
while run:

#Posisi Tembok
    if tembok1  == 0:
        tinggi_tembok  = random.randint(0,tinggi_layar-100)
        x  = 800
    if tembok2 == 0:
        tinggi_tembok2 = random.randint(0,tinggi_layar-100)
        x2 = x + jarak_tembok
    tembok1  = 1
    tembok2 = 1
    
#Mendapatkan Posisi
    for event in pygame.event.get():

#Membuat Kondisi untuk Keluar Program
        if event.type == pygame.QUIT:
            run = False

#Kondisi Klik
    Klik   = pygame.key.get_pressed()
    Kursor = pygame.mouse.get_pos()
    Klik_M = pygame.mouse.get_pressed()
    
#Mengatur Warna Layar
    window.fill(putih)

#Mengatur Latar Belakang
    window.blit(latar,[x_latar,0])
    window.blit(latar2,[x_latar2,0])

#Mengatur Tembok
    pygame.draw.rect(window,Sky_Blue,[x,pos_y_tembok,50,tinggi_tembok])
    pygame.draw.rect(window,Sky_Blue,[x,tinggi_tembok + 100,50,600-tinggi_tembok])
    pygame.draw.rect(window,Sky_Blue,[x2,pos_y_tembok2,50,tinggi_tembok2])
    pygame.draw.rect(window,Sky_Blue,[x2,tinggi_tembok2 + 100,50,600-tinggi_tembok2])

    teks  = huruf.render(str(skor),True,gold)
    teks2 = huruf2.render('kesempatan = '+ str(kesempatan),True,Mint_Cream)
    teks3 = huruf2.render(str(g),True,Mint_Cream)
    window.blit(putar_gambar(gambar, sudut), [pos_x_gambar,pos_y_gambar])
    window.blit(teks, [370,20])
    window.blit(teks2, [10,20])
    window.blit(teks3, [580,20])
#Memperbarui Nilai
    if skor/1 == tambah_kec:
        kec_tembok  += 0.1
        tambah_kec += 1
    

    if pencet_pendahuluan == True:
        window.blit(pendahuluan, [pos_x_pendahuluan,pos_y_pendahuluan])
        if pos_x_pendahuluan + 800 > Kursor[0] > pos_x_pendahuluan +150 and pos_y_pendahuluan + 250 > Kursor[1] > pos_y_pendahuluan:
            if Klik_M[0] == True:
                pencet_pendahuluan = False
                pencet_play = True
                

    if pencet_play == True:
        window.blit(play, [pos_x_play,pos_y_play])
        if pos_x_play + 150 > Kursor[0] > pos_x_play and pos_y_play + 150 > Kursor[1] > pos_y_play:
            if Klik_M[0] == True:
                pencet_play  = False
                mulai_gerak  = True
    
    if mulai_gerak == True:
        kec_tembok   = tabrak(pos_x_gambar,x,x2,pos_y_gambar,pos_y_tembok,tinggi_tembok,tinggi_tembok2,pos_y_tembok2,tinggi_tembok + 100,tinggi_tembok2 + 100,tinggi_layar,kec_tembok)
        turun  = tabrak(pos_x_gambar,x,x2,pos_y_gambar,pos_y_tembok,tinggi_tembok,tinggi_tembok2,pos_y_tembok2,tinggi_tembok + 100,tinggi_tembok2 + 100,tinggi_layar,turun)
        naik  = tabrak(pos_x_gambar,x,x2,pos_y_gambar,pos_y_tembok,tinggi_tembok,tinggi_tembok2,pos_y_tembok2,tinggi_tembok + 100,tinggi_tembok2 + 100,tinggi_layar,naik)
        pilihan_keluar  = tabrak(pos_x_gambar,x,x2,pos_y_gambar,pos_y_tembok,tinggi_tembok,tinggi_tembok2,pos_y_tembok2,tinggi_tembok + 100,tinggi_tembok2 + 100,tinggi_layar,pilihan_keluar)
        
#Mengatur Gerak Tembok
        x  -= kec_tembok
        x2 -= kec_tembok
        x_latar  -= kec_tembok
        x_latar2 -= kec_tembok
        pos_y_gambar += turun
        if Klik[pygame.K_SPACE] == False:
            sudut = -30
        if Klik[pygame.K_SPACE] == True:
            pos_y_gambar -= naik
            sudut = 0
        sudut  = tabrak(pos_x_gambar,x,x2,pos_y_gambar,pos_y_tembok,tinggi_tembok,tinggi_tembok2,pos_y_tembok2,tinggi_tembok + 100,tinggi_tembok2 + 100,tinggi_layar,sudut)
        
    if tambah_skor == 0:
        if (pos_x_gambar > x+50):
            skor += 1
            tambah_skor   = 1
    if tambah_skor2 == 0:
        if (pos_x_gambar > x2+50):
            skor += 1
            tambah_skor2  = 1

    if naik == 18 and urutan_soal <= 3:
        pilihan_masuk_soal = True
        
    if pilihan_keluar == 0:
        if pilihan_masuk_soal == True:
            window.blit(melanjutkan, [pos_x_melanjutkan,pos_y_melanjutkan])
            window.blit(ya, [pos_x_ya,pos_y_ya])
            window.blit(tidak, [pos_x_tidak,pos_y_tidak])

            if pos_x_ya + 150 > Kursor[0] > pos_x_ya and pos_y_ya + 50 > Kursor[1] > pos_y_ya:
                if Klik_M[0] == True:
                    pilihan_masuk_soal = False
                    masuk_soal = True

            if pos_x_tidak + 150 > Kursor[0] > pos_x_tidak and pos_y_tidak + 50 > Kursor[1] > pos_y_tidak:
                if Klik_M[0] == True:
                    run = False

    if masuk_soal == True:
        soal(urutan_soal,run,lanjut_main)
        run,lanjut_main = soal(urutan_soal,run,lanjut_main)
        
    if kec_tembok == 0:
        keluar_game = True
    if lanjut_main == True:
        pos_x_gambar   = 100
        if skor % 2 == 0:
            pos_y_gambar   = tinggi_tembok +1
        elif skor % 2   != 0:
            pos_y_gambar   = tinggi_tembok2 +1

        kec_tembok      = 2
        turun           = 9.8
        naik            = 18
        
        lanjut_main = False
        masuk_soal = False
        keluar_game = False
        urutan_soal += 1
        if urutan_soal <= 3:
            pilihan_keluar = 1
    
    if urutan_soal > 3 and keluar_game == True:
        window.blit(gameover, [pos_x_gameover,pos_y_gameover])
        window.blit(keluar, [pos_x_keluar,pos_y_keluar])
        if pos_x_keluar + 150 > Kursor[0] > pos_x_keluar and pos_y_keluar + 50 > Kursor[1] > pos_y_keluar:
                if Klik_M[0] == True:
                    run = False
                    
    kesempatan = 4 - urutan_soal
    
#Kondisi Mengulang Tembok
    if x +  50 <= 0:
        tembok1    = 0
        tambah_skor  = 0
    if x2 + 50 <= 0:
        tembok2   = 0
        tambah_skor2 = 0

#Gerak Latar
    if x_latar  <= -1280:
        x_latar  = 1280
    if x_latar2 <= -1280:
        x_latar2 = 1280
    
#Mengupdate Tampilan
    pygame.display.flip()
    
#Mengatur Kecepatan Program
    clock.tick(24)
        
#Keluar Program
pygame.quit()

#Selesai
