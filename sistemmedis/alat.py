from abc import ABC, abstractmethod

class Alatmedis(ABC):
    def __init__(self, nama_alat, id_alat, kalibrasi):
        self.nama_alat = nama_alat
        self._jumlah_penggunaan = 0
        self._presentase_batre = 100
        self._id_alat = id_alat
        self._kalibrasi = kalibrasi

    @property
    def jumlah_penggunaan(self):
        return self._jumlah_penggunaan
    
    @jumlah_penggunaan.setter
    def jumlah_pengunaan(self, jumlah):
        if jumlah >= 0:
            self._jumlah_penggunaan = jumlah
        
        else:
            print('Jumlah penggunaan tidak valid!')
    
    @property
    def batre(self):
        return self._presentase_batre 

    @batre.setter
    def batre(self, value):
        if 0 <= value <= 100:
            self._presentase_batre = value

    
    def gunakan_alat(self):
        self._jumlah_penggunaan += 1
        print(f'{self.nama_alat} telah menyala')
    
    def tampilkan_status(self):
        print('=====STATUS ALAT=====')
        print(f'Nama Alat: {self.nama_alat}')
        print(f'ID Alat: {self._id_alat}')
        print(f'Jumlah Penggunaan: {self._jumlah_penggunaan}')
        print(f'Presentase Baterai: {self._presentase_batre}%')
        print(f'Kalibrasi Terakhir: {self._kalibrasi} hari yang lalu')
    
    @abstractmethod
    def respon_darurat(self):
        pass

    @abstractmethod
    def hitung_skor_keamanan(self):
        pass