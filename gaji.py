lagi="ya"

while lagi=="ya":

    print ("\t \tPerhitungan Gaji Karyawan")
    print ("============================================================")

    nip=int(input("Masukan No Induk Pegawai \t: "))

    nama=str(input("Masukan Nama Pegawai/Staff \t: "))

    print ("1. Direksi \a2. Direktur utama \a3. Direktur \a4. Menejer \a5. Staff Lain")

    jabatan=int(input("Masukan Jabatan \t\t: "))

    alamat=str(input("Masukan Alamat \t\t\t: "))

    jml_anak=int(input("Masukan Jumlah Anak \t\t: "))

    if (jabatan==1):
    	gaji_pokok=10000000
    	jab="Direksi"

    elif(jabatan==2):
    	gaji_pokok=8500000
    	jab="Direktur utama"

    elif(jabatan==3):
    	gaji_pokok=6000000
    	jab="Direktur"

    else:
    	gaji_pokok=3000000
    	jab="Staff Lain"

    if(jml_anak >=5):
    	tunjangan=1000000

    elif(jml_anak <=3):

        tunjangan=750000

    else:
        tunjangan=500000

    pajak= gaji_pokok*0.15

    gaji_bersih= gaji_pokok-pajak+tunjangan

    print ("")

    print ("\a")

    print ("========================================================")

    print ("")

    print ("Nip \t\t: ",nip)

    print ("Nama \t\t: ",nama)

    print ("Jabatan \t: ",jab)

    print ("Alamat \t\t: ",alamat)

    print ("Gaji bersih \t: ",gaji_bersih)

    print ("")

    print ("========================================================")

    print ("")

    lagi=input("Ambil Data Lagi [ya/tidak]? : ")
