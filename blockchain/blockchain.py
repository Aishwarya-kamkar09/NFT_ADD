# from web3 import Web3
# import json
# import hashlib

# w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7546"))

# account = w3.eth.accounts[0]

# with open("blockchain/contract_abi.json") as f:
#     abi = json.load(f)

# CONTRACT_ADDRESS = "0x5322c88c78446746695dF7C7cFf1d376fDfC4487"

# contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=abi)

# def store_hash(hash_str: str):
#     tx_hash = contract.functions.storeCertificate(hash_str).transact({
#         "from": account,
#         "gas": 300000
#     })
#     receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
#     return receipt.transactionHash.hex()


# def verify_hash(hash_str: str) -> bool:
#     return contract.functions.verifyCertificate(hash_str).call()




# from web3 import Web3
# import json

# w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7546"))  # Ganache

# with open("contract_abi.json") as f:
#     abi = json.load(f)

# contract = w3.eth.contract(
#     address="0xD7ACd2a9FD159E69Bb102A1ca21C9a3e3A5F771B",
#     abi=abi
# )

# owner = w3.eth.accounts[0]

# def mint_nft(student, file_hash, token_uri):
#     tx = contract.functions.mintCertificate(
#         student,
#         file_hash,
#         token_uri
#     ).transact({'from': owner})

#     receipt = w3.eth.wait_for_transaction_receipt(tx)
#     return receipt










from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:7546"))

with open("blockchain/contract_abi.json") as f:
    abi = json.load(f)

contract = w3.eth.contract(
    address="0xD7ACd2a9FD159E69Bb102A1ca21C9a3e3A5F771B",
    abi=abi
)

owner = w3.eth.accounts[0]

def store_hash(hash_str: str):
    tx_hash = contract.functions.storeCertificate(hash_str).transact({
        "from": account,
        "gas": 300000
    })
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return receipt.transactionHash.hex()


def verify_hash(hash_str: str) -> bool:
    return contract.functions.verifyCertificate(hash_str).call()

def mint_nft(student, file_hash, token_uri):
    tx = contract.functions.mintCertificate(
        student,
        file_hash,
        token_uri
    ).transact({'from': owner})

    w3.eth.wait_for_transaction_receipt(tx)

    token_id = contract.functions.tokenCounter().call() - 1
    return token_id


def verify_nft(token_id):
    return contract.functions.verifyCertificate(token_id).call()