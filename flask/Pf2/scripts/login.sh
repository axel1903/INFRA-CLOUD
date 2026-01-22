#!/bin/bash

echo "Deleting all test records"
curl -X DELETE http://127.0.0.1:5555/delete/all

INSECURE_USER="AxelBAh"
INSECURE_PW="123456789"
SECURE_USER="Lamiya"
SECURE_PW="987654321"

echo "Creating insecure user"
curl -X POST -F "username=$INSECURE_USER" -F "password=$INSECURE_PW" http://127.0.0.1:5555/signup/v1

echo "Testing insecure login"
curl -X POST -F "username=$INSECURE_USER" -F "password=$INSECURE_PW" http://127.0.0.1:5555/login/v1

echo "Creating secure user"
curl -X POST -F "username=$SECURE_USER" -F "password=$SECURE_PW" http://127.0.0.1:5555/signup/v2

echo "Testing secure login"
curl -X POST -F "username=$SECURE_USER" -F "password=$SECURE_PW" http://127.0.0.1:5555/login/v2
