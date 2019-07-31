int Z=0 ,Y=0 ,X=0 ,W=0;
int D,C,B,A;
void setup()
{
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,INPUT);
  pinMode(7,INPUT);
  pinMode(8,INPUT);
  pinMode(9,INPUT);
  pinMode(13,OUTPUT);
  Serial.begin(9600);
}
 void loop()
 {
  digitalWrite (13,1);
  delay (1000);
 W=digitalRead(6);
 X=digitalRead(7);
 Y=digitalRead(8);
 Z=digitalRead(9);
  Serial.print(W);
  Serial.print(X);
  Serial.print(Y);  Serial.println(Z);
  Serial.print("hi");
   A=(!W&&!X&&!Y&&!Z) || (!W&&X&&!Y&&!Z) || (!W&&!X&&Y&&!Z) || (!W&&X&&Y&&!Z) || (!W&&!X&&!Y&&Z);
  B=(W&&!X&&!Y&&!Z) || (!W&&X&&!Y&&!Z) || (W&&!X&&Y&&!Z) || (!W&&X&&Y&&!Z) ;
  C=(W&&X&&!Y&&!Z) || (!W&&!X&&Y&&!Z) || (W&&!X&&Y&&!Z) || (!W&&X&&Y&&!Z) ;
  D=(W&&X&&Y&&!Z) || (!W&&!X&&!Y&&Z ) ;
  digitalWrite(2,A);
  digitalWrite(3,B);
  digitalWrite(4,C);
  digitalWrite(5,D);
  Serial.print(D);
  Serial.print(C);
  Serial.print(B);  Serial.println(A);
  digitalWrite(13,0);
  digitalWrite(13,1);
  delay(1000);
  }

