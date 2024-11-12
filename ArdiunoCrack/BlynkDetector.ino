#define BLYNK_TEMPLATE_ID "TMPL303"
#define BLYNK_TEMPLATE_NAME "Motion Sensing Notification Pusher"
#define BLYNK_AUTH_TOKEN "WS6oqzhcosG8oR9mY"

#define BLYNK_PRINT Serial

#include <ESP8266WiFi.h>
#include <BlynkSimpleEsp8266.h>

char auth[] = "WS6oqzhcosG8oR9mY";
char ssid[] = "SSID";
char pass[] = "PASS"; 
 
#define PIR_SENSOR  4
BlynkTimer timer;
int flag=0;
void notifyOnDetection()
{
  int isTheftAlert = digitalRead(PIR_SENSOR);
  Serial.println(isTheftAlert);
  if (isTheftAlert==1) {
    Serial.println("Motion Detecting");
    Blynk.email(" ", "Alert", "Motion Detecting");
    Blynk.notify("Alert : Motion Detecting, Be Careful");
    alert.connect();
    Blynk.logEvent("Alert","Motion Detecting");
    flag=1;
  }
  else if (isTheftAlert==0)
  {
   flag=0;
  }
}

void setup(){
  pinMode(PIR_SENSOR, INPUT);
  Serial.begin(115200);
  Blynk.begin(auth, ssid, pass);
  timer.setInterval(5000L, notifyOnDetection);
}

// Run again and again in a loop
void loop(){
  Blynk.run();
  timer.run();
}