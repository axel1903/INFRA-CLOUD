## Opmerking (VM-beperking)

Tijdens het bouwen van de Docker image trad op deze DEVASC VM een bekende
seccomp/clone3-beperking op bij `docker build` tijdens `pip install`.

De Dockerfile, commando’s en labstappen zijn correct uitgevoerd.
Deze fout is VM-/kernel-gerelateerd en geen Dockerfile-fout.
