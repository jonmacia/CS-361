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
User must also be connected to the Internet.

### Installing

* RabbitMQ website has download links for both RabbitMQ and Erland. 

### Executing program

* Requesting Data
1) User will start 2 python programs named send.py and receive.py on their desired IDEs or applications.
2) User will then go to send.py window and will see a command to enter an input for a starting amount.
```
Please type in an amount that you wish to convert
Amount:
```
3) User will then be able to enter an input for a starting and desired currency.
```
Please type in any STARTING CURRENCY using a 3 letter code.
For example these are the top 5 most traded currencies in the world
USD - US dollar
EUR - Euro
JPY - Japanese yen
GBP - Pound sterling
AUD- Australian dollar 
FROM:USD
Now choose a DESIRED CURRENCY to convert to
TO: EUR
```
4) User will have to wait a couple seconds for the API to receive this input and return data.
5) User will then recieve a notification stating that API data has been received and sent to the other python file.
6) User will be asked if they would like to start the conversion service again.
```
 [*] Waiting for messages. To exit press CTRL+C

```

* Receiving Data
1) User will go to window for receive.py and will see the program waiting for messages and the data that was sent. 
   
```
{
[*] Waiting for messages. To exit press CTRL+C
```
2) Program will collect data into a variable in the program in JSON string format and another variable in 
   Python dictionary format. JSON and converted amount will both be printed out for the user to see.
   User should be able to extract from these two variables.
```
{
    "success": true,
    "query": {
        "from": "USD",
        "to": "EUR",
        "amount": 100
    },
    "info": {
        "timestamp": 1658885285,
        "rate": 0.985985
    },
    "date": "2022-07-27",
    "result": 98.5985
}

98.5985
```
3) receive.py runs on an infinite loop that will be able to collect more messages(conversions) for the user.


## Authors



## Version History


## License



## Acknowledgments

