# Decode-QR-BareCode
## Sommaire
1. [Information Générale](#information-générale)
2. [Technologies](#technologies)
3. [Installation](#installation)
## Information Générale
***
Script permettant de décoder un **Code QR** ou un **Bar Code**.

![Image text](https://actionweb-gabon.com/files_perso/images/qrcode/codebarres.gif)
## Technologies
***
Les technologies utilisés ici sont :
* **Python3**
* **Linux ubuntu 18**
## Installation
***
Il faut avant tout crée un **_environment virtuel_**, pour mon app j'ai utlisé ```venv```
### Création d'environment virtuel
```
$ mkdir qrcode
$ cd qrcode
$ python3 -m venv optimus
```
### Activer l'environment
```
$ source optimus/bin/activate
```
**Note:** Pour désactiver l'environment on procède comme suit ```$ deactivate```.
### Installation des prérequis dans l'environnement
```
# pip3 install qrcode
# pip3 install numpy
# pip3 install Image
# pip3 install -U pip
# pip3 install -U setuptools
# pip3 install opencv-python
# apt-get install libzbar0 git
# pip3 install pyzbar
```
### Clônage du repository de l'application et Test de l'application
```
$ git clone https://github.com/bhrpro/Decode-QR-BareCode.git
$ cd Decode-QR-BareCode
$ python3 codeBarVersion1.py
```
**Note:** Il faut que l'image du code Qr ou bare code soit dans le même dossier de l'environnement.
