
import qrcode

from qrcode.constants import ERROR_CORRECT_L

# bibliotheque à installer -> pip install qrcode[pil]
# link: https://pypi.org/project/qrcode/

id_ = "00001"
nom = "Fall"
prenom = "Oumar"
addr = "Tivaouane Peulh"
tel = "771508362"
mail = "mon_email@gmail.com"

data = f"identifiant : {id_}\nnom : {nom}\nprenom : {prenom}\nadresse : {addr}\ntel : {tel}\nemail : {mail}\n"

img = qrcode.make(data)
qr = qrcode.QRCode(
    version=5,
    error_correction=ERROR_CORRECT_L,
    box_size=5,
    border=5
)


img = qr.make_image(fill_color="green", back_color="black")
img.save('qrcode.png')
