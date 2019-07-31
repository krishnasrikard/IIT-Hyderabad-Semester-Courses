int Z=0,Y=1,X=0,W=0;
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
A=(!W&&!X&&!Y&&!Z) || (!W&&X&&!Y&&!Z) || (!W&&!X&&Y&&!Z) || (!W&&X&&Y&&!Z) || (!W&&!X&&!Y&&Z);
B=(W&&!X&&!Y&&!Z) || (!W&&X&&!Y&&!Z) || (W&&!X&&Y&&!Z ) || (!W&&X&&Y&&!Z);
C=(W&&X&&!Y&&!Z) || (!W&&!X&&Y&&!Z) || (W&&!X&&Y&&!Z ) || (!W&&X&&Y&&!Z);
D=(W&&X&&Y&&!Z) || (!W&&!X&&!Y&&Z);
digitalWrite(2,A);
digitalWrite(3,B);
digitalWrite(4,C);
digitalWrite(5,D);
}
