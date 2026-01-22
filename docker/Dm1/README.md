# Dm1 – Docker management experiment

## Doel
Het beheren van Docker images en containers met Docker management commando’s.

## Beschrijving
In dit experiment werden Docker management commando’s gebruikt om:
- beschikbare Docker images te bekijken
- containers te inspecteren
- containers te verwijderen

## Uitvoering
```bash
docker images
docker ps -a
docker inspect di2-hello
docker rm $(docker ps -aq)
