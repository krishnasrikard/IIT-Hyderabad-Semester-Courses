int Z=0,Y=0,X=0,W=0;
int D,C,B,A;
void setup () 
{
pinMode ( 2 ,INPUT) ;
pinMode ( 3 ,INPUT) ;
pinMode ( 4 ,INPUT) ;
pinMode ( 5 ,INPUT) ;
pinMode ( 6,OUTPUT) ;
pinMode ( 7,OUTPUT) ;
pinMode ( 8,OUTPUT) ;
pinMode ( 9,OUTPUT) ;
pinMode (13,OUTPUT) ;
}
void loop ()
{
digitalWrite(13,1);
W=A;
X=B;
Y=C;
Z=D;
A=(!W&&!X&&Y&&!Y&&!Z) || (!W&&X&&!Y&&!Z) || (!W&&!X&&Y&&!Z) || (!W&&X&&Y&&!Z) || (!W&&!X&&!Y&&Z);
B=(W&&!X&&!Y&&!Z) || (!W&&X&&!Y&&!Z) || (W&&!X&&Y&&!Z) || (!W&&X&&Y&&!Z) ;
C=(W&&X&&!Y&&!Z) || (!W&&!X&&Y&&!Z) || (W&&!X&&Y&&!Z) || (!W&&X&&Y&&!Z) ;
D=(W&&X&&Y&&!Z) || (!W&&!X&&!Y&&Z) ;
digitalWrite(6 , A);
digitalWrite(7 , B);
digitalWrite(8 , C);
digitalWrite(9 , D); 
delay(1000);
digitalWrite(13,0);
delay(1000);
}
