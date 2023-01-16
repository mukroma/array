array = []
total = 0
n = int(input("masukan jumlah elemen array : "))
for x in range(n):
    nilai = float(input("masukan nilai ke- {} :".format(x+1)))
    array.append(nilai)
    print("\nHasil nilai total adalah : {}".format(sum(array)))
    print("hasil rata-rata adalah: {}".format(sum(array)/n))
