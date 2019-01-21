nama = input("Nama anda:")
a = int(input("Sudah berapa bulan anda kerja? "))
if a >= 48:
    print("Anda adalah pegawai tetap")
    print("Gaji anda sebesar Rp.6000000")
    print("Tunjangan yang anda dapat : BPJS kelas 1, Keluarga dan Hari Raya");
elif a >= 36:
    print("Anda belum menjadi pegawai tetap")
    print("Gaji anda sebesar Rp.5500000")
    print("Tunjangan yang anda dapat : BPJS kelas 2 & Keluarga")
elif a >= 12:
    print("Anda belum menjadi pegawai tetap")
    print("Gaji anda sbesar Rp.4000000")
    print("Anda belum mendapat tunjangan apapun")
elif a < 12:
    print("Anda belum menjadi pegawai tetap")
    print("Gaji anda sebesar Rp.3000000")
    print("Anda belum mendapat tunjangan")
else:
    print("ERROR")