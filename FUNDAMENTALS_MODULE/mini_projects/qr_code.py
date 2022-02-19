import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image


menu_text: str = '''
What do you want to do?
1) Generate QR
2) Scan
0) Exit
'''


def gen_qr() -> None:
    qr_code: pyqrcode.QRCode = pyqrcode.create(input("Enter QR code data: "))
    qr_code.png('qr.png', scale=16)
    qr_code.show()


def scn_qr() -> None:
    file = input('Enter file name: ')
    qr_data = decode(Image.open(file))
    print(qr_data)


def menu() -> str:
    print(menu_text)
    try:
        return int(input('Enter Choice: '))
    except Exception as e:
        print(e)
        return 0


def run() -> None:
    while True:
        option: int = menu()

        if option == 0:
            exit(0)
        elif option == 1:
            gen_qr()
        elif option == 2:
            scn_qr()
        else:
            exit(0)


if __name__ == '__main__':
    run()
