import random

# Identitas Pembuat
identitas = """
--------------------------------------
Permainan Tebak Nama Buah
Oleh    : Fadhli Rahman
NIM     : 1306621064
--------------------------------------
"""
print(identitas)

# Random Komputer choise
databuah = ['anggur', 'apel', 'aprikot', 'asam', 'atap', 'arbei', 'abiu', 'alpukat', 'anjeng', 'bacang', 'baguk', 'belimbing', 'bengkuang', 
            'benda', 'binjai', 'bisbul', 'blueberry', 'burahol', 'blewah', 'bit', 'cempedak', 'ceplukan', 'cermai', 'ceri', 'cokelat', 'delima', 
            'duku', 'durian', 'duwet', 'enau', 'enamenam', 'frambos', 'hamoi', 'hamlam', 'holdi', 'jamblang', 'jambuair', 'jambubatu', 'jambubol', 
            'jambumawar', 'jambumede', 'jengkol', 'jeruk', 'jerukbali', 'jerukkeprok', 'jerukkingkit', 'jeruknipis', 'jerukpurut', 'kapulasan', 
            'kawista', 'kecapi', 'kedondong', 'kelapa', 'kelengkeng', 'kelubi', 'ketela', 'kemang', 'kepel', 'kersen', 'kesemek', 'kokosan', 
            'kiwi', 'koldi', 'kurma', 'kelawi', 'kenitu', 'lai', 'langsat', 'lemon', 'leci', 'lobak', 'maja', 'malaka', 'mangga', 'manggis', 
            'markisa', 'melon', 'mengkudu', 'menteng', 'matoa', 'mentimun', 'namnam', 'nanas', 'nangka', 'naga', 'nona', 'pepaya', 'persik', 
            'pir', 'pisang', 'pete', 'rambai', 'rambusa', 'rambutan', 'rukem', 'sawo', 'semangka', 'sirsak', 'siwalan', 'srikaya', 'stroberi', 
            'sukun', 'terap', 'terong', 'tomat', 'timunsuri', 'ubi', 'waluh', 'wuni', 'zaitun']

print('==---Selamat Bermain---==')
print()

# Bagan Proses
ulang='y'
while (ulang == 'y'):
    nama_buah = random.choice(databuah)
    jumlah_huruf = len(nama_buah)
    Nyawa = jumlah_huruf
    huruf_ditebak = []
    print('komputer sedang memikirkan nama buah terdiri dari',jumlah_huruf,'huruf')
    while Nyawa > 0:
        kalah = 0
        print('Nama buah :', end=' ')
        for huruf in nama_buah:
            if huruf in huruf_ditebak:
                print(huruf, end=' ')
            else:
                print('_',end=' ')
                kalah +=1
        if kalah==0:
            print()
            print()
            print('SELAMAT. anda berhasil !!')
            print()
            break
        print()
        print()
        print('Anda memiliki',Nyawa,'kesempatan untuk menebak huruf buah tersebut')
        print()
        tebakan = input('Tebakan Anda ? ')
        huruf_ditebak +=tebakan
        if tebakan not in nama_buah:
            Nyawa -=1
            print('Sayang sekali. Huruf', tebakan,'tidak ada dalam nama buah tersebut')
            print()
            if Nyawa ==0:
                print('Anda Kalah !!')
                print('nama buah tersebut :',nama_buah)
                print()
        if tebakan in nama_buah:
            print('Benar. Huruf',tebakan,'ada dalam nama buah tersebut')
            print()
    ulang = (input('Mau main lagi (y/n) ? '))
    print()

print('Game Over !!!')
print()

