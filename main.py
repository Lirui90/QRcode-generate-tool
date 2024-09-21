import qrcode
 
def generate_qr_code(data, output_file):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
 
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)
 
if __name__ == "__main__":
    URL = input('Please type the URL press enter')
    FILE_NAME = input('Please type the generate png file name')
    data_to_encode = URL
    output_file_path = FILE_NAME
    generate_qr_code(data_to_encode, output_file_path)
    print(f"QR Code saved as {output_file_path}")
