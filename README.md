# Dapr with Docker-Compose

## Prerequisites
- [Docker](https://docs.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Running Dapr

you can just use Docker Compose directly:
```
docker-compose up
```

## Clean up

To tear down the Docker Compose deployment, you can run:
```
docker-compose down
```

## Additional Resources:

[Overview of Docker Compose](https://docs.docker.com/compose/)

## Dapr Concepts
[figma](https://www.figma.com/file/9JkczP2Qo5ReE8fgsuFfdi/Dapr-Concept?node-id=0%3A1)

## Zipkin
http://127.0.0.1:9411/

## Store the configuration in configurationstore

```bash
docker exec redis redis-cli SET orderId "100||1"
docker exec redis redis-cli SET orderId1 "200||2"
```