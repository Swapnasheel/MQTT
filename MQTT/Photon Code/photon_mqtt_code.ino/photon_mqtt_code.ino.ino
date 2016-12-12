
#include "MQTT/MQTT.h"

int swtch1 = D3; 
int swtch2 = D4;
int swtch3 = D5;
int swtch4 = D6;
int led = D7;

//SparkButton b = SparkButton();

void callback(char* topic, byte* payload, unsigned int length);
void stateinit();
void checkstatus(String );

#define server "192.168.0.41"

MQTT client(server, 1883, callback);

void callback(char* topic, byte* payload, unsigned int length) {
    char p[length + 1];
    memcpy(p, payload, length);
    p[length] = NULL;
    String message(p);
        
    checkstatus(message);
     
}


void checkstatus(String message){
    
    if (message.equals("RED"))    
        RGB.color(255, 0, 0);
    else if (message.equals("GREEN"))    
        RGB.color(0, 255, 0);
    else if (message.equals("BLUE"))    
        RGB.color(0, 0, 255);
    else    
        RGB.color(255, 255, 255);
        
        
    if (message.equals("switch1_ON")){
        digitalWrite(swtch1, LOW);
        Particle.publish("Activity_log","Switch1_is_ON");}
    else if (message.equals("switch1_OFF")){
        digitalWrite(swtch1, HIGH);
        Particle.publish("Activity_log","Switch1_is_OFF");}
    else if (message.equals("switch2_ON")){
        digitalWrite(swtch2, LOW);
        Particle.publish("Activity_log","Switch2_is_ON");}
    else if (message.equals("switch2_OFF")){
        digitalWrite(swtch2, HIGH);
        Particle.publish("Activity_log","Switch2_is_OFF");}
    else if (message.equals("switch3_ON")){
        digitalWrite(swtch3, LOW);
        Particle.publish("Activity_log","Switch3_is_ON");}
    else if (message.equals("switch3_OFF")){
        digitalWrite(swtch3, HIGH);
        Particle.publish("Activity_log","Switch3_is_OFF");}
    else if (message.equals("switch4_ON")){
        digitalWrite(swtch4, LOW);
        Particle.publish("Activity_log","Switch4_is_ON");}
    else if (message.equals("switch4_OFF")){
        digitalWrite(swtch4, HIGH);
        Particle.publish("Activity_log","Switch4_is_OFF");}
        
    delay(1000);
    Particle.publish(message);    
}

void setup() {
     RGB.control(true);

  
     pinMode(swtch1, OUTPUT); 
     pinMode(swtch2, OUTPUT); 
     pinMode(swtch3, OUTPUT); 
     pinMode(swtch4, OUTPUT); 
     pinMode(led, OUTPUT);

    stateinit();
  
    // connect to the server
    client.connect("sparkclient");

    // publish/subscribe
    if (client.isConnected()) {
        client.publish("MQTT/switch","Welcome...!! System UP and Running..!!");
        client.subscribe("MQTT/switch");
        
        
    }
}

void loop() {
    if (client.isConnected())
        client.loop();
         
}


void stateinit(){ 
  // as relay states are inverted in H/W, S/W adjustment done.
    digitalWrite(swtch1, HIGH);
    digitalWrite(swtch2, HIGH);
    digitalWrite(swtch3, HIGH);
    digitalWrite(swtch4, HIGH);
    
}
