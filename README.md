# MQTT YARP Bridge

This Bridge allows to subscribe to MQTT topics and publish contents of MQTT topics in YARP. It is not yet possible to publish on MQTT from YARP.

## Installation

Clone the repository in the source folder of your catkin workspace.

```bash
git clone https://github.com/EmaroLab/mqtt_yarp_bridge.git
```

## Dependencies

In order to succesfully run the code, you should have installed [mqtt_wrapper](https://pypi.org/project/mqtt-wrapper/#description) 

```bash
sudo -H pip install mqtt_wrapper
```

and [YARP Python](http://wiki.icub.org/wiki/YARP).

Furthermore an MQTT Broker is needed, [Mosquitto](https://mosquitto.org/documentation/) is the suggested one.

```bash
sudo apt-get install mosquitto mosquitto-clients
```

## Test

In order to test the code:

1. Check the Mosquitto broker status, if the broker is already active skip step 2.
    ```bash
    sudo service mosquitto status
    ```

1. If the Mosquitto broker is not running start it.
    ```bash
    mosquitto
    ```

1. In a new terminal tab launch the _yarpserver_.
    ```bash
    yarpserver
    ```

1. In a new terminal tab launch the _imu_brdige_yarp.py_ script.
    ```bash
    ./imu_bridge_yarp.py
    ```

1. In a new terminal tab check the yarp port _/imu/acceleration_.
    ```bash
    yarp read ... /imu/acceleration

    ```
1. In a new terminal tab publish a _sensors/imu_ message to the local Mosquitto broker.
    ```bash
    mosquitto_pub -h localhost -t "sensors/imu" -m "2;a;0.064;-0.498;9.478;0.043;-0.574;9.385;1547657301369;1547657301379;2;g;-0.001;-0.001;0.0;0.0;0.0;0.0;1547657301362;1547657301382;"
    ```

## Author

[Alessandro Carfì](https://github.com/ACarfi) e-mail: alessandro.carfi@dibris.unige.it