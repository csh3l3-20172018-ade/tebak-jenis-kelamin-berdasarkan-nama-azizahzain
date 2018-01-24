def gender(nama):
    per = ['A','I','U','E','T','L','a','i','u','e','t','l'] #identifikasi huruf
    lak = ['B','D','O','b','d','o'] #identifikasi huruf
    jumlahper = 0 #inisialisasi
    jumlahlak = 0 #inisialisasi
    for i in nama: #perulangan untuk pengecekan huruf pada nama
        if i in per: #kondisi jika terdapat huruf yang mengidentifikasi jenis kelamin
            jumlahper+=1 #penjumlahan huruf yang telah diidentifikasi
        elif i in lak: #kondisi jika terdapat huruf yang mengidentifikasi jenis kelamin
            jumlahlak+=1 #penjumlahan huruf yang telah diidentifikasi
    if (jumlahper>jumlahlak): #membandingkan jumlah huruf yang terdapat dalam nama
        print("Perempuan") #output jenis kelamin setelah dibandingkan
    elif (jumlahlak>jumlahper): #membandingkan jumlah huruf yang terdapat dalam nama
        print("Laki-laki") #output jenis kelamin setelah dibandingkan
    elif (jumlahlak==jumlahper): #membandingkan jumlah huruf yang terdapat dalam nama
        print("Tidsk Diketahui") #output jenis kelamin setelah dibandingkan
nama = input("Masukkan Nama : ") #kolom untuk memasukkan nama 
print(nama) #output nama
gender(nama) #menjalankan function gender