<table>
  <tr>
    <td>

# DecryptorX_Stealer: Arduino Cracks

DecryptorX is a repository focused on password recovery, protocol analysis, and vulnerability testing in IoT and connected environments. Designed for cybersecurity professionals, it provides tools and modules compatible with Arduino and other IoT platforms. The repository aims to help security researchers identify weak points in network protocols, enhance security practices, and educate on best practices for securing IoT ecosystems.

</td>
    <td>
      <img src="https://github.com/UjjwalSaini07/DecryptorX_Stealer/blob/main/ArdiunoCrack/assests/ReadmeAssests/HackerEmoji.png?raw=true">
    </td>
  </tr>
</table>

## 1. FakeSSID:

#### **About this project**
- WiFi captive portal for the NodeMCU (ESP8266 Module) with DNS spoofing.
- The built-in LED will blink 5 times when a password is posted.

<b>Warning!</b> Your saved passwords will **not** disappear when you restart/power off the ESP8266.

<b>Note:</b> If you want to see the stored passwords go to "**172.0.0.1**<a>/pass</a>". For changing the SSID, go to "**172.0.0.1**<a>/ssid</a>"

**HackPoints:**
<table>
  <tr>
    <th>172.0.0.1/index</th>
    <th>172.0.0.1/post</th> 
    <th>172.0.0.1/pass</th>
    <th>172.0.0.1/ssid</th>
  </tr>
  <tr>
    <td>This is the main page. Here the user will write his password and send it.</td>
    <td>This is the post page. The user will be redirected here after posting the password.</td>
    <td>This is where the attacker can retrieve all the passwords that has been posted.</td>
    <td>Here the attacker can change the SSID name of the Access Point on the go.</td>
  </tr>
  <tr>
    <td><img width="200px" src="https://raw.githubusercontent.com/BlueArduino20/ESP8266_WiFi_Captive_Portal/master/src/1_Index_2.jpg" title="index"></td>
    <td><img width="200px" src="https://raw.githubusercontent.com/BlueArduino20/ESP8266_WiFi_Captive_Portal/master/src/2_Post.jpg" title="post"></td>
    <td><img width="200px" src="https://raw.githubusercontent.com/BlueArduino20/ESP8266_WiFi_Captive_Portal/master/src/3_Pass.jpg" title="pass"></td>
<td><img width="200px" src="https://raw.githubusercontent.com/BlueArduino20/ESP8266_WiFi_Captive_Portal/master/src/4_ssid.jpg" title="ssid"></td>
  </tr>
</table>

Credit goes to [adamff-dev](https://github.com/adamff-dev/ESP8266-Captive-Portal)

## 2. BlynkDetector:

### Overview
BlynkDetector is an IoT-based motion detection project that utilizes the ESP8266 microcontroller to monitor motion using a PIR (Passive Infrared) sensor. When motion is detected, the system sends alerts and notifications via the Blynk platform. This project is ideal for creating a basic motion-sensing security system.

### Features
- Motion Detection: Uses a PIR sensor to detect movement.
- Notifications: Sends notifications to a mobile device using the Blynk app.
- Email Alerts: Sends an email alert when motion is detected.
- Customizable Events: Supports logging events for better monitoring.
- Real-time Updates: Provides live updates via the Blynk platform.

### Components Used
- ESP8266 WiFi Module: The core of the project, enabling connectivity and control.
- PIR Sensor: Detects motion in the environment.
- Blynk App: Provides an interface for monitoring and managing alerts.
- WiFi Connection: Required for connecting the ESP8266 to the Blynk cloud.

### Setup
1. Hardware:
- Connect the PIR sensor to the ESP8266 (signal pin to GPIO 4).
2. Software:
- Install the Blynk library in your Arduino IDE.
- Load the BlynkDetector.ino code onto your ESP8266.
- Replace the placeholders for SSID, PASS, and BLYNK_AUTH_TOKEN with your network credentials and Blynk token.
3. Blynk App:
- Create a Blynk project and note the BLYNK_TEMPLATE_ID, BLYNK_TEMPLATE_NAME, and BLYNK_AUTH_TOKEN.
- Add widgets (e.g., email, notifications) to your Blynk dashboard.

#### Credit goes to [Ujjwal](https://github.com/UjjwalSaini07)

## 3. Telegram_BotDetector:

### Overview
This project is a simple IoT-based motion detection system using an ESP8266 module and a PIR motion sensor. It integrates with Telegram to send real-time alerts whenever motion is detected.

### Features:
- WiFi Connectivity: The ESP8266 connects to a specified WiFi network to enable communication.
- Motion Detection: A PIR sensor monitors for motion, sending a signal when activity is detected.
- Telegram Integration: Alerts are sent to a configured Telegram chat via a bot whenever motion is detected.
- Built-in LED Notification: The ESP8266's built-in LED lights up to provide a local indication of motion detection.
- Secure Communication: The project uses the Telegram root certificate for secure communication with the Telegram API.

### Setup Instructions:
- Replace SSID and PASS with your WiFi credentials.
- Add your Telegram bot token obtained from BotFather in the BOTtoken variable.
- Enter your Telegram CHAT_ID to receive notifications.
- Connect a PIR motion sensor to the ESP8266's D2 pin.
- Upload the code to your ESP8266 using the Arduino IDE.

### How It Works:
- On startup, the ESP8266 connects to the WiFi and initializes the PIR sensor.
- If motion is detected, a message is sent to the configured Telegram chat and the built-in LED lights up.
- When no motion is detected, the LED remains off.

#### Credit goes to [Ujjwal](https://github.com/UjjwalSaini07)
