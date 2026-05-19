from sistemmedis.alat import Alatmedis

class alatpendukung_kehidupan(Alatmedis):
    def __init__(self, nama_alat, id_alat, kalibrasi):
        super().__init__(nama_alat, id_alat, kalibrasi)

    def respon_darurat(self):
        print(f"respon darurat untuk alat {self.nama_alat} diaktifkan")

    def hitung_skor_keamanan(self, skor):
        skor = self.batre()
        if self._kalibrasi > 90:
            skor -= 20
        
        if skor < 0:
            skor = 0
        
        return skor