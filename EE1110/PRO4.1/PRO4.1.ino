int Z=0,Y=0,X=1,W=0;
int A,B,C,D;
void setup()
{
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
}
 void loop()
{
A=(!W&&!X&&!Y) || (!W&&!Z);
B=(W&&!X&&!Z) || (!W&&X&&!Z);
C=(W&&X&&!Y&&!Z) || (!X&&Y&&!Z)|| (!W&&X&&Y&&!Z);
D=(W&&X&&Y&&!Z) || (!W&&!X&&!Y&&Z);
digitalWrite(2,A);
digitalWrite(3,B);
digitalWrite(4,C);
digitalWrite(5,D);
}
