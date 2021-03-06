#!/usr/bin/python

import mqtt_wrapper
import yarp
import signal
from time import sleep

yarp.Network.init()
Stamp = yarp.Stamp()

acceleration_port = yarp.BufferedPortBottle()
acceleration_port.open("/imusmartwatch/acceleration")

velocity_port = yarp.BufferedPortBottle()
velocity_port.open("/imusmartwatch/velocity")

inputPort = yarp.BufferedPortBottle()
inputPort.open("/imusmartwatch/keyboard:i")

class imu_bridge_recordings(mqtt_wrapper.bridge):

    def msg_process(self, msg):

        msg_topic = msg.topic.split("/")

        if (msg_topic[-1] == "imu"):
            topic_name = msg_topic[0].replace(" ", "_")
            msg_list = msg.payload.split(";")
            topic_name_acc = "/" + topic_name + "/acceleration"
            topic_name_vel = "/" + topic_name + "/velocity"

            pkgSizeAcc = int(msg_list[0])
            moduleSizeAcc = 4 * pkgSizeAcc + 2
            acc_msg = msg_list[2:moduleSizeAcc]

            pkgSizeGyro = int(msg_list[moduleSizeAcc])
            moduleSizeGyro = 4 * pkgSizeGyro + 2
            gyro_msg = msg_list[moduleSizeAcc + 2:moduleSizeAcc + moduleSizeGyro]

            Stamp.update()

            for i in range(0, pkgSizeAcc):
                acceleration = acceleration_port.prepare()
                acceleration.clear()
                acceleration.addString(str(topic_name_acc))
                acceleration.addDouble(float(acc_msg[3 * i].replace(',', '.')))
                acceleration.addDouble(float(acc_msg[3 * i + 1].replace(',', '.')))
                acceleration.addDouble(float(acc_msg[3 * i + 2].replace(',', '.')))

                acceleration.addDouble(float(acc_msg[3 * pkgSizeAcc + i]))

                acceleration_port.setEnvelope(Stamp)

                acceleration_port.writeStrict()

            for i in range(0, pkgSizeGyro):
                velocity = velocity_port.prepare()
                velocity.clear()
                velocity.addString(str(topic_name_vel))
                velocity.addDouble(float(gyro_msg[3 * i].replace(',', '.')))
                velocity.addDouble(float(gyro_msg[3 * i + 1].replace(',', '.')))
                velocity.addDouble(float(gyro_msg[3 * i + 2].replace(',', '.')))

                velocity.addDouble(float(gyro_msg[3 * pkgSizeGyro + i]))

                velocity_port.setEnvelope(Stamp)
                velocity_port.writeStrict()

        else:
            print msg.topic + " is not a supported topic"


def main():
    imu_sub = imu_bridge_recordings('#', 'bridge_imu_recording')

    start = "c"
    stop = "q"
    record = False

    while True:
        try:
            messageBottle = inputPort.read(False)

            if messageBottle != None:
                receivedMessage = messageBottle.toString()
            else:
                receivedMessage = ""

            if (receivedMessage == start):
                print "Start"
                record = True
            elif (receivedMessage == stop):
                print "Stop"
                record = False

            if record:
                imu_sub.looping()
                print "Recording"

        except KeyboardInterrupt:
            acceleration_port.close()
            velocity_port.close()
            inputPort.close()
            imu_sub.hook
            break


if __name__ == '__main__':
    try:
        main()
    except:
        pass

'''
            while True:
                try:
                    imu_sub.looping()
                except KeyboardInterrupt:
                    acceleration_port.close()
                    velocity_port.close()
                    inputPort.close()
                    imu_sub.hook
                    break'''