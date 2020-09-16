// Initializing Variables
int ledGreen1 = 12;
int ledRed1   = 11;
int relayA    = 10;
int relayB    = 9;
int relayC    = 8;
int relayD    = 7;
int ledGreen2 = 6;
int ledRed2   = 5;

int cmd;

void setup() {
  Serial.begin(9600);  // Initializing Serial Communication
  // Setting up Pins as OUTPUT 
  pinMode(relayA,   OUTPUT); 
  pinMode(relayB,   OUTPUT);
  pinMode(relayC,   OUTPUT);
  pinMode(relayD,   OUTPUT);
  pinMode(ledGreen1,OUTPUT);
  pinMode(ledRed1,  OUTPUT);
  pinMode(ledGreen2,OUTPUT);
  pinMode(ledRed2,  OUTPUT);
}
 
void loop() {
  if(Serial.available()){
    cmd = Serial.read();     // Reading & Storing CMDs 
    if(cmd == 'B'){   //FOR SWITCHING USB -B
      // Switching OFF Relays and Leds
      digitalWrite(relayC,    LOW);
      digitalWrite(relayD,    LOW);
      digitalWrite(ledGreen2, LOW);
      digitalWrite(ledRed1,   LOW);
      // Switching ON Relays and Leds
      digitalWrite(relayA,    HIGH);
      digitalWrite(relayB,    HIGH);
      digitalWrite(ledGreen1, HIGH);
      digitalWrite(ledRed2,   HIGH);
      
    }
    if(cmd == 'C'){     //FOR SWITCHING USB -C
      // Switching OFF Relays and Leds
      digitalWrite(relayA,    LOW);
      digitalWrite(relayB,    LOW);
      digitalWrite(ledGreen1, LOW);
      digitalWrite(ledRed2,   LOW);
      // Switching ON Relays and Leds
      digitalWrite(relayC,    HIGH);
      digitalWrite(relayD,    HIGH);
      digitalWrite(ledGreen2, HIGH);
      digitalWrite(ledRed1,   HIGH);
      
      
    }
    
  }

} 
