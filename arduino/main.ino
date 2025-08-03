int trig = 8;
int echo = 7;
int distanz, dauer;

void setup() {
  // put your setup code here, to run once:
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  // trigger
  digitalWrite(trig,0);
  delayMicroseconds(2);
  digitalWrite(trig,1);
  delayMicroseconds(5);
  digitalWrite(trig,0);
  // calculating
  dauer = pulseIn(echo, HIGH);
  distanz = int(dauer/2/29.412);
  // display
  Serial.print("Distanz(cm):");
  Serial.println(distanz); // println
  delay(100);
}
