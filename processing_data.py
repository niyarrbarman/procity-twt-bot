import requests

url = "https://host.neatqueue.com/api2/channelstats/1061301529597976700/1061303977460908173"

querystring = {"":""}

payload = ""
headers = {
    "authority": "host.neatqueue.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "origin": "https://www.neatqueue.com",
    "referer": "https://www.neatqueue.com/",
    "sec-ch-ua": "^\^Not_A",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

# print(response.text)
process_str = 'import numpy as np\n\ndata = '

def process():
    with open(r'rawdata.txt', 'w') as file:
        file.write(response.text)

    with open(r'rawdata.txt', 'r') as file:  
        data = file.read()
        data = data.replace("null", "np.NaN")
    
    with open(r'processed.py', 'w') as file:  
        file.write(process_str)
        file.write(data)

if __name__ == "__main__":
    
    pass