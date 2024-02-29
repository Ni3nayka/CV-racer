#include "motor.h"

Motor motor_1;

void setup() {
  motor_1.setup(5,6);
  motor_1.run(100);
  delay(1000);
  motor_1.run();
}

void loop() {
  // put your main code here, to run repeatedly:

}
