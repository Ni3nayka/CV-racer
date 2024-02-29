// https://github.com/Ni3nayka/Monster_car/blob/main/src/main_esp8266_avocado_keyboard/motor.h

#pragma once

class Motor {
  public:
    void setup(int pin1, int pin2) {
      Motor::pin1 = pin1;
      Motor::pin2 = pin2;
      pinMode(Motor::pin1,OUTPUT);
      pinMode(Motor::pin2,OUTPUT);
      //reverse = 1;
    }
    void run(int speed=0) {
      speed = constrain(speed,-100,100)*2.5;
      analogWrite(Motor::pin1, speed>0?speed:0);
      analogWrite(Motor::pin2, speed>0?0:-speed);
    }
  private:
    int pin1, pin2;
};