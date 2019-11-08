int a = 0;
int green1 = 6;
int blue1 = 13;
int red1 = 12;
int green2 = 11;
int blue2 = 7;
int red2 = 3;

void setup() {
  Serial.begin(9600);
  // put your setup code here, to run once:
  pinMode(green1, OUTPUT);
  pinMode(red1, OUTPUT);
  pinMode(blue1, OUTPUT);
  pinMode(green2, OUTPUT);
  pinMode(red2, OUTPUT);
  pinMode(blue2, OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(2,OUTPUT);
  pinMode(A5,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(10,OUTPUT);
  //digitalWrite(green11, 1);
  digitalWrite(5,0);
  digitalWrite(2,1);
  digitalWrite(A5,HIGH);
  digitalWrite(9,1);
  digitalWrite(4,1);
  digitalWrite(10,1);
  
  
  digitalWrite(red2, 0);
  digitalWrite(green2, 1);
  digitalWrite(blue2, 1);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.read() != -1) {
    a = Serial.read();
    Serial.println(a);  
  }
  if (a == 1) { //green & red
    digitalWrite(red1, 1);
    digitalWrite(green1, 0);
    digitalWrite(blue1, 1);
    digitalWrite(red2, 0);
    digitalWrite(green2, 1);
    digitalWrite(blue2, 1);
  }
  else if(a == 2){ //green and off
    digitalWrite(red1, 1);
    digitalWrite(green1, 1);
    digitalWrite(blue1, 0);
    digitalWrite(red2, 1);
    digitalWrite(green2, 0);
    digitalWrite(blue2, 1);
  }
  else if(a == 3){ //off and off
    digitalWrite(red1, 1);
    digitalWrite(green1, 1);
    digitalWrite(blue1, 1);
    digitalWrite(red2, 0);
    digitalWrite(green2, 1);
    digitalWrite(blue2, 1);
  }
  else if(a == 4){ //off and blue
    digitalWrite(red1, 1);
    digitalWrite(green1, 1);
    digitalWrite(blue1, 1);
    digitalWrite(red2, 1);
    digitalWrite(green2, 1);
    digitalWrite(blue2, 0);
  }
  else {
    digitalWrite(red1, 1);
    digitalWrite(green1, 1);
    digitalWrite(blue1, 1);
    digitalWrite(red2, 1);
    digitalWrite(green2, 1);
    digitalWrite(blue2, 1);
  }
  delay(100);
}
