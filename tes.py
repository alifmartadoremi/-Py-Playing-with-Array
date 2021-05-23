__author__ = "kvda"

class myClass():

    def myFunc(self):
        buah = ['apel','pisang','anggur','mujidin']
        
        print("Daftar buah Pak Ricardo : ")
        print("-----")
        for offset in range(len(buah)):
            print("{0}. {1}".format(offset+1,buah[offset]))
        check = input("Cek ketersediaan buah anda : ")
        check2 = input("Cek ketersediaan buah anda : ")
        buah.replace(check,check2)
        for offset in range(len(buah)):
            print("{0}. {1}".format(offset+1,buah[offset]))


if __name__ == '__main__':
    myClass().myFunc()