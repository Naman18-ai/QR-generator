import segno

def make_qr(text,usr_choice):
    qr = segno.make(text)
    if usr_choice=='t':
        qr.terminal()
    else:
        qr.save("qr.png")
    # qr.terminal()
uri=input("Enter the name of the website: ")
termi_or_img=input("Enter 't' for terminal or 'i' for image: ").lower()
website_uri = f"https://www.{uri}.com"
    
make_qr(website_uri,termi_or_img)
    