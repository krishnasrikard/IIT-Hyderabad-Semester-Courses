int a,b,c,d,e,f,A=0,B=0,C=0,D=0,W,X,Y,Z;
void setup()
{
  pinMode(2,INPUT );
  pinMode(3,INPUT );
  pinMode(4,INPUT );
  pinMode(5,INPUT );
  pinMode(6,OUTPUT );
  pinMode(7,OUTPUT );
  pinMode(8,OUTPUT );
  pinMode(9,OUTPUT );
  pinMode(13,OUTPUT);
  }
void loop()
{
  W=digitalRead(2);
  X=digitalRead(3);
  Y=digitalRead(4);
  Z=digitalRead(5);
  A = (!W&&!X&&!Y&&!Z)||(!W&&X&&!Y&&!Z)||(!W&&!X&&Y&&!Z)||(!W&&X&&Y&&!Z)||(!W&&!X&&!Y&&Z);
  B = (W&&!X&&!Y&&!Z)||(!W&&X&&!Y&&!Z)||(W&&!X&&Y&&!Z)||(!W&&X&&Y&&!Z);
  C = (W&&X&&!Y&&!Z)||(!W&&!X&&Y&&!Z)||(W&&!X&&Y&&!Z)||(!W&&X&&Y&&!Z);
  D = (W&&X&&Y&&!Z)||(!W&&!X&&!Y&&Z);
  digitalWrite(6,A);
  digitalWrite(7,B);
  digitalWrite(8,C);
  digitalWrite(9,D);
  digitalWrite(13, LOW);
  digitalWrite(13, HIGH);
  delay(1000);
  }
