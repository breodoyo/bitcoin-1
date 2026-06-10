import json
import requests


def rpc(method, params=None, wallet=None):
    url = "http://127.0.0.1:18443"

    if wallet:
        url = f"{url}/wallet/{wallet}"

    if params is None:
        params = []

    data = json.dumps({
        "jsonrpc": "1.0",
        "id": "myapp",
        "method": method,
        "params": params,
    })

    resp = requests.post(
        url,
        data=data,
        auth=("bootcamp", "bitcoin-bree")
    )

    if resp.status_code != 200:
        print(f"RPC Error Status: {resp.status_code}")
        print(f"Server Response: {resp.text}")
        return None

    return resp.json().get("result")


info = rpc("getblockchaininfo")
if info:
    print(f"Chain: {info['chain']}")
    print(f"Blocks: {info['blocks']}")

balance = rpc("getbalance", wallet="alice")
if balance is not None:
    print(f"Alice has {balance} BTC")


def show_blockchain_info():
    info = rpc("getblockchaininfo")

    if not info:
        print("Failed to fetch blockchain info")
        return

    print("=== Blockchain Info ===")
    print(f"Chain: {info['chain']}")
    print(f"Blocks: {info['blocks']}")
    print(f"Difficulty: {info['difficulty']}")


show_blockchain_info()
