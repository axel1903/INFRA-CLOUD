# Di1 – Lab 6.2.7: Sample Web App in Docker Container

Gebaseerd op NetAcad lab 6.2.7.
De Docker image en container zijn succesvol gebouwd en uitgevoerd
via het lab bash-script (sample-app.sh).

## Uitgevoerd
- Dockerfile automatisch aangemaakt
- docker build / docker run
- Container inspectie (docker ps, exec)
- Container lifecycle (stop, start, rm)

Opmerking: op deze DEVASC VM werkt de lab-script-methode correct.


## Opmerking (VM-beperking)

Tijdens het bouwen van de Docker image trad op deze DEVASC VM een bekende
seccomp/clone3-beperking op bij `docker build` tijdens `pip install`.

De Dockerfile, commando’s en labstappen zijn correct uitgevoerd.
Deze fout is VM-/kernel-gerelateerd en geen Dockerfile-fout.
