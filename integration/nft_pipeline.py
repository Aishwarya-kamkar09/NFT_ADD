# from blockchain.blockchain import mint_nft
# from ipfs.ipfs_upload import upload_to_ipfs
# from app.utils import generate_hash, generate_qr


# def process_certificate(file_path, student_wallet, contract_image_path):

#     # STEP 1: Hash file
#     file_hash = generate_hash(file_path)

#     # STEP 2: Upload certificate to IPFS
#     token_uri = upload_to_ipfs(contract_image_path)

#     # STEP 3: Mint NFT
#     token_id = mint_nft(student_wallet, file_hash, token_uri)

#     # STEP 4: Generate QR
#     generate_qr(token_id)

#     return {
#         "token_id": token_id,
#         "hash": file_hash,
#         "token_uri": token_uri
#     }





from blockchain.blockchain import mint_nft
from ipfs.ipfs_upload import upload_to_ipfs
from utils.hash import generate_hash
from utils.qr import generate_qr


def process_certificate(file_path, student_wallet, contract_image_path):

    file_hash = generate_hash(file_path)

    token_uri = upload_to_ipfs(contract_image_path)

    token_id = mint_nft(student_wallet, file_hash, token_uri)

    generate_qr(token_id)

    return {
        "token_id": token_id,
        "hash": file_hash,
        "token_uri": token_uri
    }