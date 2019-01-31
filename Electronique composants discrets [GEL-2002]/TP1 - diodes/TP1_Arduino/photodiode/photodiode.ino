int val = 0;
int pwm = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(3,OUTPUT);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  val = analogRead(0);
  pwm = map(val,0,1023,0,255);
  Serial.println(pwm);
  analogWrite(3,pwm);
  delay(10);
}
