# An1 – Ansible Lab 7.4.7

## Doel
Kennismaken met Ansible playbooks en het uitvoeren van taken op hosts.

## Beschrijving
In dit experiment werd een eenvoudig Ansible playbook uitgevoerd
op de lokale machine (localhost) met behulp van een inventory file.

Het playbook maakt gebruik van Ansible facts om systeeminformatie
weer te geven.

## Bestanden
- inventory.yml
- playbook.yml

## Uitvoering
```bash
ansible-playbook -i inventory.yml playbook.yml
