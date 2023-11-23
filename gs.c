//Simulação de alarme para apneia do sono, 
//que é ativado quando a sauração do paciente chega a niveis criticos


#include <WiFi.h>
#define BUZZER_PIN         2  //Alarme

const int potPin = 34;
const float BETA = 3950; 

void setup() {
  //conectando ao wifi para mandar os dados a uma servidao para controle medico
  Serial.begin(9600);
  Serial.print("Conectando-se ao Wi-Fi");
  WiFi.begin("Wokwi-GUEST", "", 6);
  while (WiFi.status() != WL_CONNECTED) {
    delay(100);
    Serial.print(".");
  }
  Serial.println(" Conectado!");
//------------------------------------------------------------

  Serial.begin(9600);
  pinMode(BUZZER_PIN, OUTPUT);          
}

void loop() {
    int analogValue = analogRead(potPin);
    
    //Utilizando um sensor de temperatura para simular um oximetro
   float kelvins = 1 / (log(1 / (4095. / analogValue - 1)) / BETA + 1.0 / 298.15);
   float celsius = kelvins - 273.15;



  if (celsius >= 40) { //o numero a ser colocado no nivel de saturação critico pode variar entre pacientes, 
  //por isso foi feito um menu em python onde fica uma bawe de dados para os pacientes com seus respectivos limites, 
  //que deveriam ser substituidos na plataforma no produto final 
  
    Serial.println(celsius);
    Serial.println("making sound");    //alarme ligado
    digitalWrite(BUZZER_PIN, HIGH); 

  } else if (celsius < 40) { 
    Serial.println(celsius);
    Serial.println("not making sound"); // alarme desligado
    digitalWrite(BUZZER_PIN, LOW);  
  }
  delay(1000);
}
