print('PEMBERI HURUF KAPITAL DAN TITIK + PENGHITUNG DAN PENCARI KARAKTER PADA KALIMAT')
str=input('Masukkan kalimat:\n')
a=input('Masukkan karakter yang ingin dihitung dan dicari:')
b=str.capitalize()+'.'
c=str.count(a)
d=str.find(a)+1
print('Setelah kapital dan titik:',b)
print('Ada %d karakter %s di kalimat %s'%(c,a,str))
print('Karakter %s pertama adalah karakter ke-%d dalam kalimat' %(a,d))