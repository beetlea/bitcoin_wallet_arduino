#include <SSD1306Wire.h>
#include <tinyECC.h>
#include "FS.h"   


SSD1306Wire display(0x3c, 5, 4); // SDA - IO5 (D1), SCL - IO4 (D2) 


void turn_on()
{
  display.clear(); 
  display.setFont(ArialMT_Plain_24); 
  display.drawString(0, 20, "TURN ON");
  display.display(); 
}

void start_screen()
{
  display.clear(); 
  display.setFont(ArialMT_Plain_24); 
  display.drawString(0, 20, "START");
  display.display(); 
}
void erase()
{
  display.clear(); 
  display.setFont(ArialMT_Plain_24); 
  display.drawString(0, 20, "CLEAR");
  display.display(); 
}

void save_key()
{
  display.clear(); 
  display.setFont(ArialMT_Plain_24); 
  display.drawString(0, 20, "SAVE");
  display.display(); 
}

void load_key()
{
  display.clear(); 
  display.setFont(ArialMT_Plain_24); 
  display.drawString(0, 20, "LOAD");
  display.display(); 
}


int key = 0;
void setup() {
  Serial.begin(9600);
  display.init(); //  Инициализируем дисплей
  display.flipScreenVertically(); // Устанавливаем зеркальное отображение экрана, к примеру, удобно, если вы хотите желтую область сделать вверху
  ///delay(2000);
  turn_on();
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
      start_screen();
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

          Serial.println(String_file);
          load_key();
        } 
        else
        {
          Serial.println("EMPTY");
      }

    }



    if((data_input.indexOf("SAVE") > -1))
    {
      data_input.remove(0,4);
      File file= SPIFFS.open("/key.txt", "w");
      file.print(data_input);
      file.close();
      Serial.println("wallet_ok");
      save_key();
    }

    if((data_input.indexOf("ERASE_ALL") > -1))
    {
      File file= SPIFFS.open("/key.txt", "w");
      file.close();
      Serial.println("wallet_ok");
      erase();
    }
  }
}
