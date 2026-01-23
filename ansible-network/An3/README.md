# An3 – Ansible playbook with cloud sandbox device

## Doel
Het ontwikkelen van een Ansible playbook gericht op een extern
(netwerk) device in een cloud sandbox omgeving.

## Beschrijving
In dit experiment werd een Ansible playbook opgesteld dat bedoeld is
om commando’s uit te voeren op een Cisco IOS-XE device in een
cloud sandbox (Cisco DevNet / NetAcad).

Het playbook maakt gebruik van:
- network_cli connection
- ios_command module

## Bestanden
- inventory.yml
- playbook.yml

## Uitvoering
```bash
ansible-playbook -i inventory.yml playbook.yml
