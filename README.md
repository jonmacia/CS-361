# Assignment Title

2.6 - Assignment 7: Microservice Implementation (Milestone #2) + Publish Communication Contract to Partner

## Description

Add a README to your GitHub (or update it if you already have one) that contains your communication contract. (Once you define it, don't change it! Your partner is relying on you.) README must contain...
Clear instructions for how to REQUEST data from the microservice you implemented. Include an example call.
Clear instructions for how to RECEIVE data from the microservice you implemented
UML sequence diagram showing how requesting and receiving data work. Make it detailed enough that your partner (and your grader) will understand

## Microservice
Microservice will take input from the user to return an amount that has been converted from one currency to another.
It will be using RabbitMQ as the message broker between sender and recieever. Program will also being using 
Fixer API to request and receive real time conversion rates.

### Dependencies

The user must install RabbitMQ and the Erlang virtual machine. User must also need to install the packages for pika and requests in Python.

### Installing

* RabbitMQ website has download links for both RabbitMQ and Erland. 

### Executing program

* Requesting Data
1) User will start 2 python programs named send.py and receive.py on their desired IDEs or applications.
2) User will then go to send.py window and will see a command to input 
```
Please type in an amount that you wish to convert
Amount:
```

## Help


```

## Authors



## Version History


## License



## Acknowledgments

