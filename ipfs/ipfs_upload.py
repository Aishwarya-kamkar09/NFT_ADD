import requests

def upload_to_ipfs(file_path):
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"

    headers = {
        "pinata_api_key": "7b6c6fe7509376e557d2",
        "pinata_secret_api_key": "f286786896c6d942c3bfe27d85a058452284f8386dc15ae776f3853244b9b792"
    }

    with open(file_path, 'rb') as f:
        res = requests.post(url, files={"file": f}, headers=headers)

    cid = res.json()["IpfsHash"]
    return f"ipfs://{cid}"