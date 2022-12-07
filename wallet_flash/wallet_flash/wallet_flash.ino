#include <SSD1306Wire.h>
#include <tinyECC.h>

tinyECC ecc;
SSD1306Wire display(0x3c, 5, 4); // SDA - IO5 (D1), SCL - IO4 (D2) 
File file;




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
  delay(2000);

  if(!SPIFFS.begin()){
    Serial.println("An Error has occurred while mounting SPIFFS");
    return;
 }

  file= SPIFFS.open("/key.txt", "r");
  if(file){
    key = 1;
  }
 
}

int pin = 0;
void loop() {
  if(Serial.available())
  {
    delay(10);
    
    String data_input = Serial.readline();

    if(data_input.indexOf("START") > -1)
    {
      Serial.println("wallet_ok");
    }


    
    if(data_input.indexOf("PIN") > -1)
    {
      data_input.remove(0,3);
      pin = data_input.toInt();
      Serial.println("wallet_ok");

      if(key == 1)
      {
        ecc.plaintext = F(file.readline());
        ecc.decrypt();
        ecc.ciphertext = F("");
        Serial.println(ecc.plaintext); 
      }
      else
      {
        Serial.println(0);
      }
    }



    if((data_input.indexOf("SAVE") > -1))
    {
      ecc.plaintext= data_input.remove(0,4);
      ecc.encrypt();
      Serial.println("wallet_ok");
    }
  }
}
