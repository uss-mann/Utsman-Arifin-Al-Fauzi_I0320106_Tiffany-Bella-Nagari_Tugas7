def panggil(func):
    return func
def helloworld():
    return 'HELLOWORLD'
def main():
    daftarnama=['adi,cahyo,budi,dedi']
    print('Keadaan awal')
    print(daftarnama)

    print('\nMenggunakan sorted():')
    print(sorted(daftarnama))

    daftarnama.sort(key=lambda n:n.lower())

    print('\nKeaadaan akhir:')
    print(daftarnama)
if __name__ == '__main__':
    main()