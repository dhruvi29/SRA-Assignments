int sw1=4;
int sw2=3;
int sw3=2;
int in3=7;
int in4=6;
int pwmb=9;

void AnalogWrite(int x){
  int val=x/255*1000;

  digitalWrite(pwmb,HIGH);
  delay(val);
  digitalWrite(pwmb,LOW);
  delay(1000-val);
  
  
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(in3,OUTPUT);
  pinMode(in4,OUTPUT);
  pinMode(pwmb,OUTPUT);
  pinMode(sw1,INPUT_PULLUP);
  pinMode(sw2,INPUT_PULLUP);
  pinMode(sw3,INPUT_PULLUP);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(sw1)==HIGH){
    digitalWrite(in3,HIGH);
    digitalWrite(in4,LOW);
    AnalogWrite(191);
  }
  else if(digitalRead(sw2)==HIGH){
    digitalWrite(in3,HIGH);
    digitalWrite(in4,LOW);
    AnalogWrite(127);
  }
  else if(digitalRead(sw3)==HIGH){
    digitalWrite(in3,HIGH);
    digitalWrite(in4,LOW);
    AnalogWrite(64);
  }
  else{
    digitalWrite(in3,LOW);
    digitalWrite(in4,LOW);
    AnalogWrite(0);
  }

}
