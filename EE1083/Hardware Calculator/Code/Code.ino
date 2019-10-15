#include <Keypad.h>
#include <Wire.h> 
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x20,20,4);

long first = 0;
long second = 0;
double total = 0;

char customKey;
const byte ROWS = 4;
const byte COLS = 4;

char keys[ROWS][COLS] = {
  {'1','2','3','+','%'},
  {'4','5','6','-','^'},
  {'7','8','9','*','~'},
  {'C','0','s','/','='}
};
byte rowPins[ROWS] = {2,3,4,5}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {11,10,9,8}; //connect to the column pinouts of the keypad

//initialize an instance of class NewKeypad
Keypad customKeypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS); 

void setup()
{
  lcd.init(); // initialize the lcd 
  lcd.backlight();
}

void loop()
{
  customKey = customKeypad.getKey();
  switch(customKey) 
  {
  case '0' ... '9': // This keeps collecting the first value until a operator is pressed "+-*/"
    lcd.setCursor(0,0);
    first = first * 10 + (customKey - '0');
    lcd.print(first);
    break;

  case '+':
    first = (total != 0 ? total : first);
    lcd.setCursor(0,1);
    lcd.print("+");
    second = SecondNumber(); // get the collected the second number
    total = first + second;
    lcd.setCursor(0,3);
    lcd.print(total);
    first = 0, second = 0; // reset values back to zero for next use
    break;

  case '-':
    first = (total != 0 ? total : first);
    lcd.setCursor(0,1);
    lcd.print("-");
    second = SecondNumber();
    total = first - second;
    lcd.setCursor(0,3);
    lcd.print(total);
    first = 0, second = 0;
    break;

  case '*':
    first = (total != 0 ? total : first);
    lcd.setCursor(0,1);
    lcd.print("*");
    second = SecondNumber();
    total = first * second;
    lcd.setCursor(0,3);
    lcd.print(total);
    first = 0, second = 0;
    break;

  case '/':
    first = (total != 0 ? total : first);
    lcd.setCursor(0,1);
    lcd.print("/");
    second = SecondNumber();
    lcd.setCursor(0,3);

    second == 0 ? lcd.print("Invalid") : total = (float)first / (float)second;

    lcd.print(total);
    first = 0, second = 0;
    break;

    
  case '%':
    first = (total != 0 ? total : first);
    lcd.setCursor(0,1);
    lcd.print("%");
    second = SecondNumber();
    lcd.setCursor(0,3);

    second == 0 ? lcd.print("Invalid") : total = (int)first / (int)second;

    lcd.print(total);
    first = 0, second = 0;
    break;

    
  case '^':
    first = (total != 0 ? total : first);
    lcd.setCursor(0,1);
    lcd.print("^");
    total = (float)first * (float)second;

    lcd.print(total);
    first = 0,
    break;

    
  case '~':
    first = (total != 0 ? total : first);
    lcd.setCursor(0,1);
    lcd.print("~");

    first < 0 ? lcd.print("Invalid") : total = sqrt((float)first);

    lcd.print(total);
    first = 0, second = 0;
    break;

  case 'C':
    total = 0;
    lcd.clear();
    break;
  }
}

long SecondNumber()
{
  while( 1 )
  {
    customKey = customKeypad.getKey();
    if(customKey >= '0' && customKey <= '9')
    {
      second = second * 10 + (customKey - '0');
      lcd.setCursor(0,2);
      lcd.print(second);
    }

    if(customKey == '=') break;  //return second;
  }
 return second; 
}
