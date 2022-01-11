# Decode-QR-BareCode
Script permettant de décoder un Code QR ou un Bare Code en python3
Il faut créer un environnement virtuel :
❯ mkdir qrCode
❯ cd qrCode
❯ python3 -m venv optimus
#Activer l'environnemnt
❯source optimus/bin/activate
# Pour deasactiver on fait ceci: ❯ deactivate
Installation des bibliothèques et prérequis dans l'environnement
❯ pip3 install qrcode
❯ pip3 install numpy
❯ pip3 install Image
❯ pip3 install -U pip
❯ pip3 install -U setuptools
❯ pip3 install opencv-python
❯ sudo apt-get install libzbar0
❯ pip3 install pyzbar
#Et la lançer la commande suivante pour utiliser le script
#NB: Il faut que la capture du code Qr soit dans le même dossier de l'environnement
❯ python3 realcode.py
