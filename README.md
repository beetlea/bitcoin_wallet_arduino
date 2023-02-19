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

2 Solder the display to the board according to the following scheme:
<img src="https://habrastorage.org/r/w1560/getpro/habr/upload_files/7f3/332/22c/7f333222cedb4956555a081aba9e29c9.png">

3 Insert the board into the case. From the beginning, we insert the board into the black part of the case, then into the red one. If necessary, it can be fixed with thermal glue. We insert it so that the hole in the back of the case coincides with the USB socket of the board. In this case, the module cover is directed upwards
<img src="https://github.com/beetlea/bitcoin_wallet_arduino/blob/master/photo/IMG_1637.JPG">

4 Glue the screen with a thermal gun at the four corners of the rectangle of the lid. We insert the nuts into the lower holes, connect them to the computer and stitch them with a sketch from the wallet_flash folder. Attach the straps. It should turn out like this:
<img src="https://github.com/beetlea/bitcoin_wallet_arduino/blob/master/photo/IMG_1641.JPG">


<h2>Principle of operation</h2>
Run the bitcoin_wallet.exe file in the bitcoin_wallet folder

1 You can change language for English
 <img src="https://github.com/beetlea/bitcoin_wallet_arduino/blob/master/photo/1.png">
 
2 Connect your device to your computer and select the appropriate comport. Then click connect. The status bar should show “connected”, and the arduino display should show “START”.
 <img src="https://github.com/beetlea/bitcoin_wallet_arduino/blob/master/photo/2.png">
 
 3 If you want to work in a test blockchain, leave a checkmark in the “Set blockchain” field. If you want to use a "True" blockchain, then check the box “True”
 
 <img src="https://github.com/beetlea/bitcoin_wallet_arduino/blob/master/photo/3.png">
 4 To create a wallet, click the "Create Wallet" button, create a PIN code and click the "Save Wallet" button. The arduino display should show “SAVE” when successfully saving the wallet to the arduino memory

<img src="https://github.com/beetlea/bitcoin_wallet_arduino/blob/master/photo/4.png">
   
5 If you already have a wallet, or you want to save a newly created wallet, then click the add wallet button and paste the private key there. And then enter the pin code and click the "Load Wallet" button. If you forget the PIN code, then access to the wallet will be lost. You will have to manually select passwords. Loading a private wallet into memory does not require internet access.
   <img src="https://github.com/beetlea/bitcoin_wallet_arduino/blob/master/photo/5.png">
  
