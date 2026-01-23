# N3 – RESTCONF experiment (Lab 8.3.6)

## Doel
Kennismaken met RESTCONF voor het beheren van netwerkdevices
met behulp van HTTP(S) en YANG data models.

## Beschrijving
In dit experiment werd een RESTCONF GET request opgesteld
om interface-informatie op te vragen van een Cisco IOS-XE
device via RESTCONF.

RESTCONF gebruikt HTTP(S) en YANG data modellen, meestal
gecodeerd als JSON.

## Uitvoering
```bash
curl -k -u developer:C1sco12345 \
-H "Accept: application/yang-data+json" \
https://sandbox-iosxe.cisco.com/restconf/data/ietf-interfaces:interfaces
