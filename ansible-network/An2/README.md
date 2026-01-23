# An2 – Own Ansible playbook experiment

## Doel
Het zelfstandig opstellen en uitvoeren van een eigen Ansible playbook.

## Beschrijving
In dit experiment werd een eigen Ansible playbook ontwikkeld dat:
- een directory aanmaakt op de host
- een bestand creëert
- systeeminformatie toevoegt via Ansible facts

Het playbook werd uitgevoerd op de lokale machine (localhost).

## Bestanden
- inventory.yml
- playbook.yml

## Uitvoering
```bash
ansible-playbook -i inventory.yml playbook.yml
