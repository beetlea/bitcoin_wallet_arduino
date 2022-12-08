#include <SSD1306Wire.h>
#include <tinyECC.h>
#include "FS.h"   

tinyECC ecc;
SSD1306Wire display(0x3c, 5, 4); // SDA - IO5 (D1), SCL - IO4 (D2) 




void start_screen()
{
  display.clear(); // Очищаем экран
  
  display.drawRect(102, 2, 20, 8); // Пустой прямоугольник
  display.fillRect(104, 4, 4, 4); // Заполненный прямоугольник
  display.fillRect(110, 4, 4, 4); // Заполненный прямоугольник
  display.fillRect(116, 4, 4, 4); // Заполненный прямоугольник
  
  display.drawHorizontalLine(0, 14, 128); // Горизонтальная линия
  
  display.setFont(ArialMT_Plain_24); // Шрифт кегль 24
  display.drawString(0, 40, "START WALLET");
  display.display(); // Выводим на экран
}
int key = 0;
void setup() {
  Serial.begin(115200);
  display.init(); //  Инициализируем дисплей
  display.flipScreenVertically(); // Устанавливаем зеркальное отображение экрана, к примеру, удобно, если вы хотите желтую область сделать вверху
  start_screen();
  ///delay(2000);

  if(!SPIFFS.begin()){
    Serial.println("An Error has occurred while mounting SPIFFS");
    return;
 }
  if(!SPIFFS.exists("/key.txt"))
  {
    File file= SPIFFS.open("/key.txt", "w");
    file.close();
    key = 1;
  }
  else
  {
    File file= SPIFFS.open("/key.txt", "r");
    file.close();
    key = 1;
  }
 
}

int pin = 0;
void loop() {
  if(Serial.available())
  {
    delay(10);
    
    String data_input = Serial.readString();

    if(data_input.indexOf("START") > -1)
    {
      Serial.println("wallet_ok");
    }


    
    if(data_input.indexOf("GET") > -1)
    {
        String String_file;
        File file= SPIFFS.open("/key.txt", "r");
        if(file.size() > 0)
        {
          while (file.available()) {
            String_file.concat((char)file.read());
          }
          file.close();
          ecc.plaintext= F("");

          ecc.ciphertext = String_file;
          ecc.decrypt();
          ecc.ciphertext = F("");
          Serial.print(ecc.plaintext);
        } 
        else
        {
          Serial.println("EMPTY");
      }

    }



    if((data_input.indexOf("SAVE") > -1))
    {
      data_input.remove(0,4);
      ecc.plaintext= data_input;
      
      ecc.encrypt();
      File file= SPIFFS.open("/key.txt", "w");

      String String_save;
      for(int i = 0; i < ecc.ciphertext.length(); i++)
      {
        String_save.concat(ecc.ciphertext[i]);
      }
      
      file.print(ecc.ciphertext);
      file.close();
      Serial.println("wallet_ok");
    }
  }
}
