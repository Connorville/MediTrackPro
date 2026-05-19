from sistemmedis.alatdiagnostik import alatdiagnostik
from sistemmedis.alatpendukungkehidupan import alatpendukung_kehidupan

class MediTrackPRO:

    def __init__(self):
        self.daftar_alat = []

    def tambah_alat(self, alat):
        self.daftar_alat.append(alat)
        print('alat berhasil ditambahkan')

    def tampilkan_alat(self):
        if not self.daftar_alat:
            print("Belum ada alat")
            return

        for alat in self.daftar_alat:
            alat.tampilkan_status()
    
    def simulasi_alat(self, id_alat):
        for alat in self.daftar_alat:
            if alat._id_alat == id_alat:
                alat.gunakan_alat()

                if isinstance(alat, alatpendukung_kehidupan):
                    alat.batre -= 10
                
                return
        print('Alat tidak ditemukan')
    
    def aktifkan_respon_darurat(self, id_alat):
        for alat in self.daftar_alat:
            if alat._id_alat == id_alat:
                alat.respon_darurat()
                return
        print('alat tidak ditemukan')
    
    def tampilkan_skor_keamanan(self, id_alat):
        for alat in self.daftar_alat:
            if alat._id_alat == id_alat:
                skor = alat.hitung_skor_keamanan()
                print(f'Skor keamanan {alat.nama_alat}: {skor}')
                return
        print('alat tidak ditemukan')
