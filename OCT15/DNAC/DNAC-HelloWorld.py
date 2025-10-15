#### DNA Center Northbound API: Hello Network 
import requests
import datetime
import json
requests.packages.urllib3.disable_warnings()
print ("Current date and time: ")
print(datetime.datetime.now())
# HARD CODED VARIABLES
DNAC_scheme = "https://"
DNAC_authority="sandboxdnac.cisco.com"
DNAC_port=":443"
DNAC_path_token="/dna/system/api/v1/auth/token"
DNAC_path="/dna/intent/api/v1/network-device"
#### IT IS NECESSARY TO HAVE A USERNAME AND PASSWORD
DNAC_user = "devnetuser"
DNAC_psw = "Cisco123!"
#REQUEST TOKEN BASED ON devnetuser Cisco123!
token_req_url = DNAC_scheme+DNAC_authority+DNAC_path_token
auth = (DNAC_user, DNAC_psw)
req = requests.post(token_req_url, auth=auth, verify=False)
print("API Return Code: " + str(req.status_code))  
print('Request URI: ' + token_req_url)
print("Username: " + DNAC_user)
resp = req.text
token = req.json()["Token"]
print("Received Token:")
print(token)
print("Length Token:")
print(len(token))
#REQUEST API SERVICE (USING X-AUTH-TOKEN -- INVENTORY REQUEST
req_url = DNAC_scheme+DNAC_authority+DNAC_port+DNAC_path
print(req_url)
headers = {'X-auth-token': token}
import os, requests, datetime

requests.packages.urllib3.disable_warnings()

DNAC_SCHEME = "https://"
DNAC_HOST   = os.getenv("DNAC_HOST", "sandboxdnac2.cisco.com")
DNAC_PORT   = ":443"
PATH_TOKEN  = "/dna/system/api/v1/auth/token"
PATH_DEVS   = "/dna/intent/api/v1/network-device"
DNAC_USER   = os.getenv("DNAC_USER", "devnetuser")
DNAC_PSW    = os.getenv("DNAC_PSW",  "Cisco123!")

BASE = f"{DNAC_SCHEME}{DNAC_HOST}{DNAC_PORT}"

def token():
    r = requests.post(BASE+PATH_TOKEN, auth=(DNAC_USER, DNAC_PSW), verify=False, timeout=15)
    r.raise_for_status()
    return r.json()["Token"]

def device_count(tok):
    r = requests.get(BASE+PATH_DEVS, headers={"X-Auth-Token": tok}, verify=False, timeout=20)
    r.raise_for_status()
    data = r.json()
    items = data.get("response", data)
    return len(items) if isinstance(items, list) else 0

if __name__ == "__main__":
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Timestamp: {ts}")
    try:
        tok = token()
        cnt = device_count(tok)
        print(f"DNA Center host: {DNAC_HOST}")
        print(f"Devices gevonden: {cnt}")
    except Exception as e:
        print(f"Fout bij API-call: {e}")
