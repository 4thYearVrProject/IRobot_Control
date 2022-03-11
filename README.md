# IRobot_Control
As part of the fourth year project requirements for SYSC 4907
Contributors:
Ifiok Udoh, Stone Liu

The purpose of this python script is to allow for functional movement control of the IRobot Create device.

Note that in this project, the device runs in "full" mode, so be careful to ensure that it does not drive off cliffs or bump into hard surfaces.

##Installation

Ensure you have Python 3 installed on your Linux machine (Ubuntu and Kali Linux recommended). For this project, Python 3.9.10 was used. 
To check your Python version, in a command terminal run:

```bash
python3 --version
```
Also ensure you have pip installed
```bash
command -v pip
```
Install the pycreate 2 library
```bash
pip install pycreate2
```
Pycreate2 library details can be found: 

https://github.com/MomsFriendlyRobotCompany/pycreate2/tree/master/examples

## Checking your device's serial port
In a terminal, run:
```bash
/dev/serial
```
Next, run
```bash
cd by-path
```
Finally, run
```bash
ls -al
The serial port should be listed at the end of the file path

Replace the "ttyUSB0" in main.py with your serial port address
```python
robot = irobotAPI.Irobot("your_address")
```


