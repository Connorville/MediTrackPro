from sistemmedis.alat import Alatmedis

class alatdiagnostik(Alatmedis):
    def __init__(self, nama_alat, id_alat, kalibrasi):
        super().__init__(nama_alat, id_alat, kalibrasi)

    def respon_darurat(self):
        print(f"respon darurat untuk alat {self.nama_alat} diaktifkan")

    def hitung_skor_keamanan(self):
        skor = 100
        skor -= self._jumlah_penggunaan * 2
        if self._kalibrasi > 180:
            skor -= 20
        if skor < 0:
            skor = 0

        return skor
        