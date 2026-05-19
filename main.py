from sistemmedis.MediTrackPRO import MediTrackPRO
from sistemmedis.alatdiagnostik import alatdiagnostik
from sistemmedis.alatpendukungkehidupan import alatpendukung_kehidupan

system = MediTrackPRO()

while True:
    print('Selamat datang di aplikasi MediTrackPro  ')
    print("\n1. Tambahkan Alat\n2. Tampilkan status alat\n3. Tampilkan simulasi penggunaan alat\n4. Aktifkan respon darurat\n5. Menampilkan skor keamanan\n6. keluar")

    pilihan = input("Pilihan opsi:")

    if pilihan == '1':
        nama_alat = input("Masukkan nama alat:")
        id_alat = input("Masukkan ID alat:")

        print('\nJenis alat:')
        print('1. Alat Diagnostik\n2. Alat Pendukung Kehidupan')

        jenis = input('Pilih jenis alat: ')
        kalibrasi = int(input("Masukkan lama hari sejak kalibrasi terakhir:"))

        if jenis == '1':
            alat = alatdiagnostik(nama_alat, id_alat, kalibrasi)

        elif jenis == '2':
            alat = alatpendukung_kehidupan(nama_alat, id_alat, kalibrasi)
        else:
            print('Jenis alat tidak valid')
            continue

        system.tambah_alat(alat)

    elif pilihan == "2":
        system.tampilkan_alat()

    elif pilihan == "3":
        id_alat = input("Masukkan ID alat yang akan digunakan:")
        system.simulasi_alat(id_alat)

    elif pilihan == "4":
        id_alat = input("Masukkan ID alat untuk mengaktifkan respon darurat:")
        system.aktifkan_respon_darurat(id_alat)
    
    elif pilihan == "5":
        id_alat = input('Masukkan ID alat: ')
        system.tampilkan_skor_keamanan(id_alat)
    
    elif pilihan == "6":
        print('Terima kasih menggunakan MeditrackPRO')
        break

    else:
        print('Pilihan tidak valid')