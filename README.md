# Scrapping project


## Getting Started


### Prerequisites

To run a service you need docker and docker-compose.
To run service locally and run tests you will need:
- python3 + pyenv/venv + requirements
- rabbitmq
    
    `sudo apt-get install rabbitmq-server`
    
    `sudo rabbitmq-plugins enable rabbitmq_management`

## Deployment

Docker images are build using Dockerfile.
To build the image run:

`docker build -t geoguess .`

And run the stack with command:

`docker-compose up`

## Running the tests

Having requirements installed:

`cd app`

`python -m pytest tests`

## Built With

* Python
* Docker
* RabbitMQ

## Authors

* **Stankiewicz Mateusz** - https://www.linkedin.com/in/mateusz-stankiewicz-3b04a2108/

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

