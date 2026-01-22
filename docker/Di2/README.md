# Di2 – Eigen Docker image experiment

## Doel
Het zelfstandig aanmaken van een eenvoudige Docker image.

## Beschrijving
In dit experiment werd een eenvoudige Python applicatie gebruikt
om een eigen Docker image te bouwen met behulp van een Dockerfile.

## Bestanden
- Dockerfile
- hello.py

## Uitvoering
```bash
docker build -t di2-hello .
docker run di2-hello
