import qrcode 
from PIL import Image
def generate_code():
    qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
    )
    qr.add_data("https://portfolio-website-chi-red.vercel.app")
    qr.make(fit=True)
    qr.make_image(fill_color="red",back_color="white").save("Portfolio.png")

def main():
    generate_code()

if __name__ == "__main__":
    main()









    
