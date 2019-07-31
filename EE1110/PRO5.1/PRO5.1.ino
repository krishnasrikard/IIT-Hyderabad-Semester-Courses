int a,b,c,d,e,f,g;
int A=0,B=1,C=0,D=0;
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
 a=(!D&&!C&&!B&&A)||(!D&&C&&!B&&!A);
 b=(C&&!B&&A)||(C&&B&&!A);
 c=(!D&&!C&&B&&!A);
 d=(C&&!B&&!A)||(!D&&!C&&!B&&A)||(C&&B&&A)||(D&&!B&&A);
 e=(C&&!B&&!A)||(A);
 f=(!C&&!B&&A)||(!C&&B&&!A)||(B&&A);
 g=(!D&&!C&&!B)||(C&&B&&A);
  digitalWrite(2, a);
  digitalWrite(3, b);
  digitalWrite(4, c);
  digitalWrite(5, d);
  digitalWrite(6, e);
  digitalWrite(7, f);
  digitalWrite(8, g);
}
