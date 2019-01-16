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

## Author

[Alessandro Carfì](https://github.com/ACarfi) e-mail: alessandro.carfi@dibris.unige.it