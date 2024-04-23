#include <BluetoothSerial.h>

#define outputPin0 32
#define outputPin1 33
#define outputPin2 26
#define outputPin3 25

BluetoothSerial SerialBT;

void forward(uint32_t pwm);
void slowly_left(uint32_t pwm);
void rapidly_left(uint32_t pwm);
void slowly_right(uint32_t pwm);
void nothing(void);
void back_slowly_left(uint32_t pwm);
void rapidly_right(uint32_t pwm);
void back_slowly_right(uint32_t pwm);
void backward(uint32_t pwm);
void stop(void);


uint32_t pwm = 250;
bool boost = false;

void setup() {
  SerialBT.begin("ESP32_3");      // Bluetoothシリアルに「ESP32_1」という名前をつけて初期化 // 2つ目の機体は「ESP32_2」に変更
  Serial.begin(115200);            

  pinMode(outputPin0, OUTPUT);
  pinMode(outputPin1, OUTPUT);
  pinMode(outputPin2, OUTPUT);
  pinMode(outputPin3, OUTPUT);

  ledcSetup(0, 5000, 8);
  ledcSetup(1, 5000, 8);
  ledcSetup(2, 5000, 8);
  ledcSetup(3, 5000, 8);

  ledcAttachPin(outputPin0, 0);
  ledcAttachPin(outputPin1, 1);
  ledcAttachPin(outputPin2, 2);
  ledcAttachPin(outputPin3, 3);

}

void loop() {
  if (SerialBT.available()) {      // Bluetoothシリアルに受信したかどうかを調べる
    char ch = SerialBT.read();     // 受信した文字を得る
    Serial.println(ch);            // 受信した文字をシリアルモニタに出力

    if (ch == '9') {
      forward(pwm);
    }
    else if (ch == '8') {
      slowly_left(pwm);
    }
    else if (ch == '7') {
      rapidly_left(pwm);
    }
    else if (ch == '6') {
      slowly_right(pwm);
    }
    else if (ch == '5') {
      nothing();
    }
    else if (ch == '4') {
      back_slowly_left(pwm);
    }
    else if (ch == '3') {
      rapidly_right(pwm);
    }
    else if (ch == '2') {
      back_slowly_right(pwm);
    }
    else if (ch == '1') {
      backward(pwm);
    }
    else{
      stop();
    }
  }
}

void forward(uint32_t pwm) {
  ledcWrite(0,pwm);
  ledcWrite(1,0);
  ledcWrite(2,pwm);
  ledcWrite(3,0);
}
void slowly_left(uint32_t pwm) {
  ledcWrite(0,pwm);
  ledcWrite(1,0);
  ledcWrite(2,0);
  ledcWrite(3,0);
}
void rapidly_left(uint32_t pwm) {
  ledcWrite(0,pwm);
  ledcWrite(1,0);
  ledcWrite(2,0);
  ledcWrite(3,pwm);
}
void slowly_right(uint32_t pwm) {
  ledcWrite(0,0);
  ledcWrite(1,0);
  ledcWrite(2,pwm);
  ledcWrite(3,0);
}
void nothing(void){
  ledcWrite(0,0);
  ledcWrite(1,0);
  ledcWrite(2,0);
  ledcWrite(3,0);
}
void back_slowly_left(uint32_t pwm) {
  ledcWrite(0,0);
  ledcWrite(1,0);
  ledcWrite(2,0);
  ledcWrite(3,pwm);
}
void rapidly_right(uint32_t pwm) {
  ledcWrite(0,0);
  ledcWrite(1,pwm);
  ledcWrite(2,pwm);
  ledcWrite(3,0);
}
void back_slowly_right(uint32_t pwm) {
  ledcWrite(0,0);
  ledcWrite(1,pwm);
  ledcWrite(2,0);
  ledcWrite(3,0);
}
void backward(uint32_t pwm) {
  ledcWrite(0,0);
  ledcWrite(1,pwm);
  ledcWrite(2,0);
  ledcWrite(3,pwm);
}
void stop(void){
  ledcWrite(0,255);
  ledcWrite(1,255);
  ledcWrite(2,255);
  ledcWrite(3,255);
}
