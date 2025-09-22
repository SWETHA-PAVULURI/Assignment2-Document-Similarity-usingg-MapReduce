import os
import random

# Sample vocabulary
WORDS = [
    "hadoop", "mapreduce", "spark", "data", "analytics", "cloud", "machine",
    "learning", "distributed", "parallel", "processing", "document", "similarity",
    "database", "storage", "network", "security", "python", "java", "scalability",
    "system", "algorithm", "big", "mining", "tokenization", "stemming", "index",
    "query", "stream", "computation", "cluster", "performance", "model", "training",
    "testing", "natural", "language", "processing", "neural", "network", "inference"
]

def generate_dataset(num_words, filename):
    words_written = 0
    doc_id = 1
    with open(filename, "w") as f:
        while words_written < num_words:
            # Each document has 50–100 words
            doc_length = random.randint(50, 100)
            doc_length = min(doc_length, num_words - words_written)
            doc_words = [random.choice(WORDS) for _ in range(doc_length)]
            line = f"Document{doc_id} " + " ".join(doc_words) + "\n"
            f.write(line)
            words_written += doc_length
            doc_id += 1
    print(f"{filename} generated with {words_written} words across {doc_id-1} documents.")

if __name__ == "__main__":
    generate_dataset(1000, "dataset1.txt")
    generate_dataset(3000, "dataset2.txt")
    generate_dataset(5000, "dataset3.txt")
