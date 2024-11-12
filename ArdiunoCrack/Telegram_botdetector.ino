#include <ESP8266WiFi.h>
#include <WiFiClientSecure.h>
#include <UniversalTelegramBot.h>

const char* ssid = "SSID"; // WIFI SSID
const char* password = "PASS"; // WIFI Password

#define BOTtoken " " // Enter the bot Token you got from bot-father
#define CHAT_ID " " // Enter your chatID you got from chatid bot

X509List cert(TELEGRAM_CERTIFICATE_ROOT);
WiFiClientSecure client;
UniversalTelegramBot bot(BOTtoken, client);

const int pirPin = 2; // PIR sensor output connected to D2 pin

void setup() {
  Serial.begin(115200);
  configTime(0, 0, "pool.ntp.org");
  client.setTrustAnchors(&cert);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(500);
  }

  pinMode(pirPin, INPUT);

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());
  bot.sendMessage(CHAT_ID, "Wifi Connected!", "");
  bot.sendMessage(CHAT_ID, "System has Started!!", "");
}

// Code for breadboard light sequencing
void loop() {
  int motion = digitalRead(pirPin);

  if (motion == HIGH) {
    digitalWrite(LED_BUILTIN, HIGH); // Turn on built-in LED when motion detected
    bot.sendMessage(CHAT_ID, "ALERT! MOTION DETECTED!!", "");
  } else {
    digitalWrite(LED_BUILTIN, LOW); // Turn off built-in LED when no motion detected
  }

  delay(1000); // Adjust delay as needed
}
