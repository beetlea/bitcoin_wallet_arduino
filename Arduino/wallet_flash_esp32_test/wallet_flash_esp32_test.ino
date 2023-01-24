#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <EEPROM.h>

#define LEN_ADR      1000
#define SCREEN_WIDTH 128 
#define SCREEN_HEIGHT 64 
#define EEPROM_SIZE  1001

#define OLED_RESET     -1 // Reset pin # (or -1 if sharing Arduino reset pin)
#define SCREEN_ADDRESS 0x3D ///< See datasheet for Address; 0x3D for 128x64, 0x3C for 128x32
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);


void turn_on()
{
  display.clearDisplay();
  display.setTextSize(3);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(2,0);
  display.print("TURN ON");
  display.display(); 
}

void start_screen()
{
  display.clearDisplay();
  display.setTextSize(3);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(2,0);
  display.print("START");
  display.display(); 
}
void erase()
{
  display.clearDisplay();
  display.setTextSize(3);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(2,0);
  display.print("CLEAR");
  display.display(); 
}

void save_key()
{
  display.clearDisplay();
  display.setTextSize(3);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(2,0);
  display.print("SAVE");
  display.display(); 
}

void load_key()
{
  display.clearDisplay();
  display.setTextSize(3);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(2,0);
  display.print("LOAD");
  display.display(); 
}


int key = 0;
void setup() {
  Serial.begin(9600);
  Serial.setTimeout(500);

  EEPROM.begin(EEPROM_SIZE);
  
  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
  }
  display.display();
  display.clearDisplay();
  
  turn_on();

}

int pin = 0;
void loop() {
  if(Serial.available())
  {
    String data_input = Serial.readString();

    if(data_input.indexOf("START") > -1)
    {
      Serial.println("wallet_ok");
      start_screen();
    }


    
    if(data_input.indexOf("GET") > -1)
    {
        String String_file;
        byte len = 0;
        len = EEPROM.read(LEN_ADR);
        Serial.println("data_read = " + String(len));
        String data_output;
        if(len)
        {
          for(int i = 0; i < len; i++)
          {
            Serial.write(EEPROM.read(i));
          }
          Serial.println();
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
      /**
      for(int chr = 0; chr < data_input.length(); chr++)
      {
        EEPROM.write(0, (char)data_input[chr]);
      }*/
      EEPROM.put(0, data_input);
      EEPROM.commit();
      EEPROM.put(LEN_ADR, (byte)data_input.length());
      //Serial.println("data_len " + String(data_input.length()));
      EEPROM.commit();
      Serial.println("wallet_ok");
      save_key();
    }

    if((data_input.indexOf("ERASE_ALL") > -1))
    {
      byte erase_mass[LEN_ADR];
      memset(erase_mass, 0, LEN_ADR);
      EEPROM.put(0,erase_mass);
      Serial.println("wallet_ok");
      erase();
    }
  }
}
