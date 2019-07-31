void sevenseg(int a, int b, int c,int d,int e, int f, int g)
{
  digitalWrite(2, a);
  digitalWrite(3, b);
  digitalWrite(4, c);
  digitalWrite(5, d);
  digitalWrite(6, e);
  digitalWrite(7, f);
  digitalWrite(8, g);
}
void setup()
{
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(8, OUTPUT);
}
void loop()
{
  sevenseg(0,0,0,0,0,0,1);
  delay(2000);
  sevenseg(1,0,0,1,1,1,1);
  delay(2000);
  sevenseg(0,0,1,0,0,1,0);
  delay(2000);
  sevenseg(0,0,0,0,1,1,0);
  delay(2000);
  sevenseg(1,0,0,1,1,0,0);
  delay(2000);
  sevenseg(0,1,0,0,1,0,0);
  delay(2000);
  sevenseg(0,1,0,0,0,0,0);
  delay(2000);
  sevenseg(0,0,0,1,1,1,1);
  delay(2000);
  sevenseg(0,0,0,0,0,0,0);
  delay(2000);
  sevenseg(0,0,0,1,1,0,0);
  delay(2000);
}

