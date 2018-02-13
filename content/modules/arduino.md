Title: Arduino
Date: 2018-02-15

In this station, you will work with Arduinos at two different levels of abstraction.

## 

Follow 

## I2C

I2C is a communication protocol allowing high-level communication between components. All you have to 
do is connect four wires:

- V+ (either 3.3 volts or 5 volts)
- Ground
- SCL (clock)
- SDA (data)

Basically, the clock provides an electrical heartbeat. Every time the clock pulses, the receiver reads the data line to see whether it is high or low. In this way, binary 
data can be sent across the wires. The I2C protocol defines how this binary data should be interpreted.

All the GoGo sensors run on I2C, which means you can use them with Arduinos. 

