import heapq
from collections import defaultdict, Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    char_freq = Counter(text)
    priority_queue = [HuffmanNode(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    return priority_queue[0]

def build_huffman_codes(root, current_code="", huffman_codes={}):
    if root is None:
        return

    if root.char is not None:
        huffman_codes[root.char] = current_code

    build_huffman_codes(root.left, current_code + "0", huffman_codes)
    build_huffman_codes(root.right, current_code + "1", huffman_codes)

def huffman_encoding(text):
    if not text:
        return None, {}

    root = build_huffman_tree(text)
    huffman_codes = {}
    build_huffman_codes(root, "", huffman_codes)

    encoded_text = ''.join([huffman_codes[char] for char in text])
    return encoded_text, huffman_codes

def huffman_decoding(encoded_text, huffman_codes):
    if not encoded_text:
        return None

    reversed_codes = {code: char for char, code in huffman_codes.items()}
    decoded_text = ""
    current_code = ""
    for bit in encoded_text:
        current_code += bit
        if current_code in reversed_codes:
            decoded_text += reversed_codes[current_code]
            current_code = ""

    return decoded_text

if __name__ == "__main__":
    text = "huffman" #this is an example for huffman encoding
    encoded_text, huffman_codes = huffman_encoding(text)
    print(f"Encoded text: {encoded_text}")
    
    decoded_text = huffman_decoding(encoded_text, huffman_codes)
    print(f"Decoded text: {decoded_text}")