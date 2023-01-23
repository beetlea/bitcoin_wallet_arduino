<h1>Crypto wallet for BITCOIN coins on Arsduino esp8266</h1>
<b>With settings: protection, private key storage and more.</b>
<br>
<img src="https://github.com/beetlea/bitcoin_wallet_arduino/blob/master/photo/IMG_1643.JPG">
<br>
<h2>Project purpose:</h2>
The project is designed to generate an electronic wallet, encrypt the private wallet number and then store it on the Wemos D1 board. The project consists of four parts.
<br>Part 1 is the firmware for the Wemos D1 module (folder "wallet_flash" in .ino format).
<br>Part 2 is the source file of the wallet graphical environment for windows. A program was written in python version 3.9 (file "bitcoin_wallet.py"
<br>Part 3 is a compiled program based on a python script. This program is compiled and does not need to be installed on the computer python and dependencies necessary for the project
<br>Part 4 stl case files for printing it on a 3D printer (case1, case2, cover).

<h2>What you will need:</h2>

Wemos D1 Module

0.96" I2C OLED display

Two bolts with a diameter of 4 mm and two nuts M4

3D printer

Watch straps 20mm

<h2>Assembling the arduino project:</h2>

1 Print the case on a 3D printer. We solder the wiring to the display.
<img src="https://github.com/beetlea/bitcoin_wallet_arduino/blob/master/photo/IMG_1634.JPG" style="height=100px">

2 Припаиваем дисплей к плате по следующей схеме:
<img src="https://habrastorage.org/r/w1560/getpro/habr/upload_files/7f3/332/22c/7f333222cedb4956555a081aba9e29c9.png">

3 Insert the board into the case. From the beginning, we insert the board into the black part of the case, then into the red one. If necessary, it can be fixed with thermal glue. We insert it so that the hole in the back of the case coincides with the USB socket of the board. In this case, the module cover is directed upwards
<img src="https://github.com/beetlea/bitcoin_wallet_arduino/blob/master/photo/IMG_1637.JPG">

4 Glue the screen with a thermal gun at the four corners of the rectangle of the lid. We insert the nuts into the lower holes, connect them to the computer and stitch them with a sketch from the wallet_flash folder. Attach the straps. It should turn out like this:
<img src="https://github.com/beetlea/bitcoin_wallet_arduino/blob/master/photo/IMG_1641.JPG">
