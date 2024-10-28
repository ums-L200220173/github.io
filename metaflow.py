class KuliahInformatika:
    def __init__(self, mahasiswa):
        self.mahasiswa = mahasiswa
        self.spp_terbayar = False
        self.nilai_akhir = None

    def bayar_spp(self):
        self.spp_terbayar = True
        print(f"{self.mahasiswa} telah membayar SPP.")

    def ikuti_kuliah(self):
        if not self.spp_terbayar:
            print("SPP belum dibayar. Tidak bisa mengikuti kuliah.")
            return
        print(f"{self.mahasiswa} mengikuti kuliah.")

    def dapatkan_nilai(self, nilai):
        if self.spp_terbayar:
            self.nilai_akhir = nilai
            print(f"{self.mahasiswa} mendapatkan nilai akhir: {nilai}")
        else:
            print("Tidak bisa mendapatkan nilai, SPP belum dibayar.")

# Contoh penggunaan
mahasiswa1 = KuliahInformatika("Aldino Dewa Ndaru")
mahasiswa1.bayar_spp()
mahasiswa1.ikuti_kuliah()
mahasiswa1.dapatkan_nilai("A")
