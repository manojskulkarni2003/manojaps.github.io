import hashlib
import random

class MinHash:
    def __init__(self, num_hashes=100):
        self.num_hashes = num_hashes
        self.permutations = [(random.randint(1, 2**32 - 1), random.randint(1, 2**32 - 1)) for _ in range(num_hashes)]
    
    def _hash(self, x, a, b):
        return (a * x + b) % (2**32 - 1)
    
    def create_signature(self, set_):
        signature = []
        for a, b in self.permutations:
            min_hash = float('inf')
            for elem in set_:
                hash_value = self._hash(hash(elem), a, b)
                if hash_value < min_hash:
                    min_hash = hash_value
            signature.append(min_hash)
        return signature
    
    def jaccard_similarity(self, sig1, sig2):
        if len(sig1) != len(sig2):
            raise ValueError("Signatures must have the same length")
        return sum(1 for i in range(len(sig1)) if sig1[i] == sig2[i]) / len(sig1)

# Example usage
document1 = "the quick brown fox jumps over the lazy dog"
document2 = "the quick brown fox jumps over the lazy cat"

shingles1 = set(document1.split())
shingles2 = set(document2.split())

minhash = MinHash(num_hashes=100)
signature1 = minhash.create_signature(shingles1)
signature2 = minhash.create_signature(shingles2)

similarity = minhash.jaccard_similarity(signature1, signature2)
print(f"Estimated Jaccard similarity: {similarity}")
