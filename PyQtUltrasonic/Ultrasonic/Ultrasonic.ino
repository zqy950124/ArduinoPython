
// set pins with SR04 conntced to Arduino
const int TrigPin = 2; // yellow
const int EchoPin = 3; // green
float distance; 

void setup() 
{   
    Serial.begin(9600); 
    
    pinMode(TrigPin, OUTPUT); 
    pinMode(EchoPin, INPUT); 
 
} 

void loop() 
{ 
    //   Trig  
        digitalWrite(TrigPin, LOW); 
        delayMicroseconds(2); 
        digitalWrite(TrigPin, HIGH); 
        delayMicroseconds(10);
        digitalWrite(TrigPin, LOW); 
    
    //  Echo
        float distance = pulseIn(EchoPin, HIGH) / 58.00;
        Serial.print(" Distance ");
        Serial.print(distance); 
        Serial.println("cm"); 
        delay(1000); 
}
