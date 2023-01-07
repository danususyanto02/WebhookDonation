# install package
# pip install pyautogui pyttsx3 pydirectinput flask opencv-python


import pyautogui
import pyttsx3
import pydirectinput
import time

from flask import Flask, request
from kordinat import gambar 
from konversi_rupiah import KonversiRupiah


# gambar('img\example.png')

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():

    dataDonasi = request.json 

    #Saweria
    jumlahDonasi = dataDonasi['amount_raw'] #Jumlah donasi
    namaDonator = dataDonasi['donator_name'] #Nama yang donasi
    emailDonator = dataDonasi['donator_email'] #Email yang donasi
    pesanDonasi = dataDonasi['message'] #Pesan donasi

    #Sociabuzz
    # jumlahDonasi = dataDonasi['amount'] #Jumlah donasi
    # namaDonator = dataDonasi['supporter'] #Nama yang donasi
    # jenisMataUang = dataDonasi['currency'] #Email yang donasi
    # pesanDonasi = dataDonasi['message'] #Pesan donasi

    engine = pyttsx3.init()
    engine.getProperty('rate')
    engine.setProperty('rate', 125)
    engine.say("Ada donasi dari" + namaDonator)
    engine.runAndWait()
    engine.stop()
    
    batasWaktu = time.time() + 10

    print('Ada donasi dari: ' + namaDonator)
    print('Sebesar: Rp.' + KonversiRupiah(jumlahDonasi) )

    if jumlahDonasi <= 10000:
        while time.time() < batasWaktu:
              pydirectinput.keyDown('w')
        pydirectinput.keyUp('w')


    elif jumlahDonasi <= 25000:
        while time.time() < batasWaktu:
              pydirectinput.press('1')
              pydirectinput.press('2')
              pydirectinput.press('3')

    elif jumlahDonasi <= 35000:
        while time.time() < batasWaktu:
              pydirectinput.press('g')
     
    elif jumlahDonasi <= 50000:
      prefix = '/type'
      cekPrefix = pesanDonasi.startswith(prefix)
      pesanDipotong = pesanDonasi.lstrip("/type")

      if cekPrefix == True:
        pydirectinput.keyDown('shift')
        pydirectinput.keyDown('enter')
        pydirectinput.keyUp('enter')
        pydirectinput.keyUp('shift')
        pyautogui.write(pesanDipotong + ' dari ' + namaDonator)
        pydirectinput.press('enter')

    elif jumlahDonasi <= 70000:
          pydirectinput.press('x')

    elif jumlahDonasi <= 100000:
      pydirectinput.keyDown('alt')
      pydirectinput.keyDown('f4')
      pydirectinput.keyUp('f4')
      pydirectinput.keyUp('alt')
      kordinatx = 793 
      kordinaty = 689
      pydirectinput.moveTo(kordinatx, kordinaty)
      pydirectinput.click()


    return ('success', 200)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8080)


