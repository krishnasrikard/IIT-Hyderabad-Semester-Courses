// Pin 13 has an LED connected on most Arduino boards.
// give it a name:
int analogPin = 0;     // temperature sensor(LM35) connected to analog pin 0

                       // outside leads to ground and +5V

int val = 0;           // variable to store the value read


int buzzer = 7;
int led = 13;

// the setup routine runs once when you press reset:
void setup() {
  Serial.begin(9600);
  // initialize the digital pin as an output.
  pinMode(buzzer, OUTPUT);
  pinMode(led,OUTPUT);
  }

// the loop routine runs over and over again forever:
void loop() {
  val = analogRead(analogPin);    // read the input pin

  Serial.println(val);             // debug value
  if (val > 49)
  {

  digitalWrite(buzzer, HIGH);   // turn the buzzer on (HIGH is the voltage level)
     digitalWrite(led, HIGH); 
  //delay(1000);               // wait for a second
  
}
  digitalWrite(buzzer, LOW);    // turn the LED off by making the voltage LOW
   digitalWrite(led, LOW);  
  //delay(1000);               // wait for a second
}
