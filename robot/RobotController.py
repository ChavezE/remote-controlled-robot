import math


class RobotController:
    """ 
    Class RobotController that is used to handle the received commands
    in the following order:
        +-------------------------------------------+
        | j1_vert, j1_horiz, j2_vert, j2_horiz, btns |
        +--------------------------------------------+
    each of it is a byte (8 bits).

    This can handle the move of 4 motors (not yet implemented) with the 
    vertical move: front, back; horizontal move: right, left; turn:
    right, left; move the camera.

    Attributes:
        _motorLF: Object to control the Left Front Motor
        _motorLB: Object to control the Left Front Motor
        _motorRF: Object to control the Left Front Motor
        _motorRB: Object to control the Left Front Motor
    """

    def __init__(self, motorLF, motorLB, motorRF, motorRB):
        self._motorLF = motorLF
        self._motorLB = motorLB
        self._motorRF = motorRF
        self._motorRB = motorRB


    def parseNewCommand(self, array_commands):
        """ 
        Entry method to handle a new received command.

        Args:
            array_commands: Array with 5 elements of the command.

        Raises:
            Exception: An error when the length of array_commands is different
                from 5.
        """

        if (len(array_commands) != 5):
            raise Exception("Should be 5-elements-array")

        dict_commands = self._fromArrayToDictionaryCommands(array_commands)

        self._moveWithCommandsValue(dict_commands)


    def _fromArrayToDictionaryCommands(self, array_commands):
        dict_commands = {
            "j1_vertical" : array_commands[0],
            "j1_horizontal" : array_commands[1],
            "j2_vertical" : array_commands[2],
            "j2_horizontal" : array_commands[3],
            "j1_btn" : array_commands[4] & (1),
            "j2_btn" : array_commands[4] & (1<<1),
            "btnA" : array_commands[4] & (1<<2),
            "btnB" : array_commands[4] & (1<<3),
            "btnC" : array_commands[4] & (1<<4),
            "btnD" : array_commands[4] & (1<<5),
            "btnE" : array_commands[4] & (1<<6),
            "btnF" : array_commands[4] & (1<<7),
        }

        return dict_commands


    def _moveWithCommandsValue(self, dict_commands):
        """
        Method that takes the value of joystick 1 and 2 divide in its
        vertical and horizontal component and see what move make.

        It first check the joystick 1 to see if it wants to go forward,
        backward, left or right. Then it checks if it wants turn left or
        right. Finally, it sums both generated values and calls the motor
        functions to move the motors.

        Args:
            dict_commands: Dictionary with the received commands.

        """

        # Max magnitud that will be gotten with the sum of both joysticks.
        # MAX_FINAL_MAGNITUD = math.sqrt((128 ** 2) * 2) * 2

        # j1_magnitud, j1_angle = self._fromRectangularOfControllerToPolar(
        #         dict_commands["j1_horizontal"], 
        #         dict_commands["j1_vertical"])
        
        # j2_magnitud, j2_angle = self._fromRectangularOfControllerToPolar(
        #         dict_commands["j2_horizontal"], 
        #         dict_commands["j2_vertical"])

        # vel_motorLF = 0
        # vel_motorLB = 0
        # vel_motorRF = 0
        # vel_motorRB = 0

        # # Check the joystick 1
        # if (j1_angle >= 45 and j1_angle <= 135):
        #     vel_motorLF = j1_magnitud
        #     vel_motorRF = j1_magnitud
        #     vel_motorLB = j1_magnitud
        #     vel_motorRB = j1_magnitud
        # elif (j1_angle >= 225 and j1_angle <= 315):
        #     vel_motorLF = -j1_magnitud
        #     vel_motorRF = -j1_magnitud
        #     vel_motorLB = -j1_magnitud
        #     vel_motorRB = -j1_magnitud
        # elif (j1_angle > 135 and j1_angle < 225):
        #     vel_motorLF = -j1_magnitud
        #     vel_motorLB = j1_magnitud
        #     vel_motorRF = j1_magnitud
        #     vel_motorRB = -j1_magnitud
        # else:
        #     vel_motorLF = j1_magnitud
        #     vel_motorLB = -j1_magnitud
        #     vel_motorRF = -j1_magnitud
        #     vel_motorRB = j1_magnitud

        # # Check the joystick 2
        # if (j2_angle > 135 and j2_angle < 225):
        #     vel_motorLF += -j2_magnitud
        #     vel_motorLB += -j2_magnitud
        #     vel_motorRF += j2_magnitud
        #     vel_motorRB += j2_magnitud
        # elif (j2_angle < 45 or j2_angle > 315):
        #     vel_motorLF += j2_magnitud
        #     vel_motorLB += j2_magnitud
        #     vel_motorRF += -j2_magnitud
        #     vel_motorRB += -j2_magnitud
        

        # # Make the velocity values from 0 to 1 to then
        # # map the values from 0 to MAX_PWM
        # vel_motorLF /= MAX_FINAL_MAGNITUD + 0.0
        # vel_motorLB /= MAX_FINAL_MAGNITUD + 0.0
        # vel_motorRF /= MAX_FINAL_MAGNITUD + 0.0
        # vel_motorRB /= MAX_FINAL_MAGNITUD + 0.0

        # print("vel_motorLF : ", vel_motorLF)
        # print("vel_motorLB : ", vel_motorLB)
        # print("vel_motorRF : ", vel_motorRF)
        # print("vel_motorRB : ", vel_motorRB)

        # # Move forward or backward with the calculated value
        # if (vel_motorLF < 0):
        #     self._motorLF.backward(vel_motorLF * self._motorLF.MAX_PWM_VALUE)
        # else:
        #     self._motorLF.forward(vel_motorLF * self._motorLF.MAX_PWM_VALUE)

        # if (vel_motorLB < 0):
        #     self._motorLB.backward(vel_motorLB * self._motorLB.MAX_PWM_VALUE)
        # else:
        #     self._motorLB.forward(vel_motorLB * self._motorLB.MAX_PWM_VALUE)

        # if (vel_motorRF < 0):
        #     self._motorRF.backward(vel_motorRF * self._motorRF.MAX_PWM_VALUE)
        # else:
        #     self._motorRF.forward(vel_motorRF * self._motorRF.MAX_PWM_VALUE)
            
        # if (vel_motorRB < 0):
        #     self._motorRB.backward(vel_motorRB * self._motorRB.MAX_PWM_VALUE)
        # else:
        #     self._motorRB.forward(vel_motorRB * self._motorRB.MAX_PWM_VALUE)


        # IDDLE
        # if(dict_commands["j1_vertical"] <= 150 and dict_commands["j1_vertical"] >= 100 ):
        #     self._motorRB.stop()
        #     self._motorLB.stop()
        #     self._motorRF.stop()
        #     self._motorLF.stop()

        if(dict_commands["j1_vertical"] > 150):
            vel_motorLF = self.mapFromTo(dict_commands["j1_vertical"],150,256,0,80)
            vel_motorLB = self.mapFromTo(dict_commands["j1_vertical"],150,256,0,80)
            vel_motorRF = self.mapFromTo(dict_commands["j1_vertical"],150,256,0,80)
            vel_motorRB = self.mapFromTo(dict_commands["j1_vertical"],150,256,0,80)
            self._motorRB.forward(vel_motorRB)
            self._motorLB.forward(vel_motorLB)
            self._motorRF.forward(vel_motorRF)
            self._motorLF.forward(vel_motorLF)  
            print("vel_motorLF : ", vel_motorLF)
            print("vel_motorLB : ", vel_motorLB)
            print("vel_motorRF : ", vel_motorRF)
            print("vel_motorRB : ", vel_motorRB)
        elif(dict_commands["j1_vertical"] < 100):
            vel_motorLF = self.mapFromTo(dict_commands["j1_vertical"],125,0,0,80)
            vel_motorLB = self.mapFromTo(dict_commands["j1_vertical"],125,0,0,80)
            vel_motorRF = self.mapFromTo(dict_commands["j1_vertical"],125,0,0,80)
            vel_motorRB = self.mapFromTo(dict_commands["j1_vertical"],125,0,0,80)
            self._motorRB.backward(vel_motorRB)
            self._motorLB.backward(vel_motorLB)
            self._motorRF.backward(vel_motorRF)
            self._motorLF.backward(vel_motorLF)  
            print("vel_motorLF : ", vel_motorLF)
            print("vel_motorLB : ", vel_motorLB)
            print("vel_motorRF : ", vel_motorRF)
            print("vel_motorRB : ", vel_motorRB)

        elif(dict_commands["j2_horizontal"] > 150):
            vel_motorLF = self.mapFromTo(dict_commands["j2_horizontal"],150,256,0,80)
            vel_motorLB = self.mapFromTo(dict_commands["j2_horizontal"],150,256,0,80)
            vel_motorRF = self.mapFromTo(dict_commands["j2_horizontal"],150,256,0,80)
            vel_motorRB = self.mapFromTo(dict_commands["j2_horizontal"],150,256,0,80)
            self._motorRB.backward(vel_motorRB)
            self._motorLB.forward(vel_motorLB)
            self._motorRF.backward(vel_motorRF)
            self._motorLF.forward(vel_motorLF)  
            print("vel_motorLF : ", vel_motorLF)
            print("vel_motorLB : ", vel_motorLB)
            print("vel_motorRF : ", vel_motorRF)
            print("vel_motorRB : ", vel_motorRB)
        elif(dict_commands["j2_horizontal"] < 100):
            vel_motorLF = self.mapFromTo(dict_commands["j2_horizontal"],125,0,0,80)
            vel_motorLB = self.mapFromTo(dict_commands["j2_horizontal"],125,0,0,80)
            vel_motorRF = self.mapFromTo(dict_commands["j2_horizontal"],125,0,0,80)
            vel_motorRB = self.mapFromTo(dict_commands["j2_horizontal"],125,0,0,80)
            self._motorRB.forward(vel_motorRB)
            self._motorLB.backward(vel_motorLB)
            self._motorRF.forward(vel_motorRF)
            self._motorLF.backward(vel_motorLF)  
            print("vel_motorLF : ", vel_motorLF)
            print("vel_motorLB : ", vel_motorLB)
            print("vel_motorRF : ", vel_motorRF)
            print("vel_motorRB : ", vel_motorRB)
        else:
            self._motorRB.stop()
            self._motorLB.stop()
            self._motorRF.stop()
            self._motorLF.stop() 


    def _fromRectangularOfControllerToPolar(self, value_x, value_y):
        """
        Convert the rectangular components (x,y) to polar components
        (magnitud, angle) taking into acount that the values sent by 
        the joystick are with a move in the values to the lowest value
        is zero.

        Args:
            value_x: Value of the rectangular component x with the 
                lowest value is zero.
            value_y: Value of the rectangular component y with the 
                lowest value is zero.

        Returns:
            magnitud
            angle
        """

        HALF_VALUE_JOYSTICK = 127

        magnitud = math.sqrt(((value_x - HALF_VALUE_JOYSTICK) ** 2) + 
            ((value_y - HALF_VALUE_JOYSTICK) ** 2))
        angle = math.atan2(value_y - HALF_VALUE_JOYSTICK, 
            value_x - HALF_VALUE_JOYSTICK)
        angle = self._formPiMinusPiPlusTo360Angle(angle)

        return magnitud, angle

    def _formPiMinusPiPlusTo360Angle(self, angle_radian):
        """
        Convert a radian value between pi and -pi to a degree value
        between 0 and 360.

        Args:
            angle_radian: radian angle between +pi and -pi.

        Returns:
            Integer value in degrees between 0 and 360.
        """
        angle_degrees = math.degrees(angle_radian);

        if (angle_degrees < 0):
            return 360 + angle_degrees
        else:
            return angle_degrees

    def mapFromTo(self,x,a,b,c,d):
        return (x-a)*(d-c)/(b-a)+c
