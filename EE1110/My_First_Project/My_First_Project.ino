int a,b,c,d,e,f,g,x,y,z;
void setup()
{
  Serial.begin(9600);
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);//for reseting the flip flop 
  pinMode(10,OUTPUT);
  pinMode(11,OUTPUT);
  pinMode(12,INPUT);
  pinMode(13,INPUT);
  
}

void loop()
{
  
if(Serial.available()>0)
{x=Serial.read();}

if (x=1)
{
  digitalWrite(10,x);

if (Serial.available()>0)
{y=Serial.read();}

if(y=1)
{
  digitalWrite(11,y);

if (Serial.available()>0)
{z=Serial.read();}

if (z=1)
{
  digitalWrite(2,1);
  digitalWrite(3,0);
  digitalWrite(4,0);
  digitalWrite(5,1);
  digitalWrite(6,1);
  digitalWrite(7,1);
  digitalWrite(8,1);
  Serial.print(1); 
}

else
{digitalWrite(9,HIGH);
  digitalWrite(2,0);
  digitalWrite(3,0);
  digitalWrite(4,0);
  digitalWrite(5,0);
  digitalWrite(6,0);
  digitalWrite(7,0);
  digitalWrite(8,1);
  Serial.print(0);}
}

else
{digitalWrite(9,HIGH);
  digitalWrite(2,0);
  digitalWrite(3,0);
  digitalWrite(4,0);
  digitalWrite(5,0);
  digitalWrite(6,0);
  digitalWrite(7,0);
  digitalWrite(8,1);
  Serial.print(0);}
}

else
{digitalWrite(9,HIGH);
  digitalWrite(2,0);
  digitalWrite(3,0);
  digitalWrite(4,0);
  digitalWrite(5,0);
  digitalWrite(6,0);
  digitalWrite(7,0);
  digitalWrite(8,1);
  Serial.print(0);
  }

}

