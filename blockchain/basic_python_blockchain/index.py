from hashlib import sha256

import json

import time


class Chain:
    # genesis
    def __init__(self):
        self.blockchain = []
        self.pending = []
        self.add_block(prevhash="Genesis", proof=123)

    # adding a transaction
    def add_transaction(self, sender, recipient, amount):
        transaction = {
            "sender": sender,
            "recipient": recipient,
            "amount": amount
        }
        self.pending.append(transaction)

    # computing hashes - unique identifier for the block
    def compute_hash(self, block):
        json_block = json.dumps(block, sort_keys=True).encode()
        curhash = sha256(json_block).hexdigest()
        return curhash

    # adding a block
    def add_block(self, proof, prevhash=None):
        block = {
            "index": len(self.blockchain),
            "timestamp": time.time(),
            "transactions": self.pending,
            "proof": proof,
            # proof roughly verifies the validity of the blocl - process of finding proof is mining
            "prevhash": prevhash or self.compute_hash(self.blockchain[-1])
        }
        self.pending = []
        self.blockchain.append(block)


# Trying it out!
chain = Chain()
t1 = chain.add_transaction("Vitalik", "Satoshi", 100)
t2 = chain.add_transaction("Satoshi", "Alice", 10)
t3 = chain.add_transaction("Alice", "Charlie", 34)
chain.add_block(12345)
t4 = chain.add_transaction("Bob", "Eve", 23)
t5 = chain.add_transaction("Dennis", "Brian", 3)
t6 = chain.add_transaction("Ken", "Doug", 88)
chain.add_block(6789)
print(chain.blockchain)

#OUTPUT: [{'index': 0, 'timestamp': 1647617499.551739, 'transactions': [], 'proof': 123, 'prevhash': 'Genesis'}, {'index': 1, 'timestamp': 1647617499.551744, 'transactions': [{'sender': 'Vitalik', 'recipient': 'Satoshi', 'amount': 100}, {'sender': 'Satoshi', 'recipient': 'Alice', 'amount': 10}, {'sender': 'Alice', 'recipient': 'Charlie', 'amount': 34}], 'proof': 12345, 'prevhash': '1feb2effc7f2f25ee62c193b5a8c78d7c4fce50e86a97c6930c3c17c00cfc7ef'}, {'index': 2, 'timestamp': 1647617499.5517921, 'transactions': [{'sender': 'Bob', 'recipient': 'Eve', 'amount': 23}, {'sender': 'Dennis', 'recipient': 'Brian', 'amount': 3}, {'sender': 'Ken', 'recipient': 'Doug', 'amount': 88}], 'proof': 6789, 'prevhash': 'e5c9fc12643809e47a8e38badaf177239ddf66cf2f8e30291c39f6e5426bfe1c'}]
