int main(void){
    wiringPiSetup();
    pinMode(LED_PIN, OUTPUT);
        digitalWrite(LED_PIN, HIGH); 
    return 0;