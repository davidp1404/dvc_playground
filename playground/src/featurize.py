import argparse
import json
import os

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max_features", type=int, required=True)
    parser.add_argument("--ngram_range", type=int, required=True)
    args = parser.parse_args()

    os.makedirs("data/features", exist_ok=True)

    for split in ("train", "test"):
        with open(f"data/split/{split}.txt") as f:
            lines = f.readlines()

        # Simulate feature extraction (bag of words)
        features = []
        for line in lines:
            words = line.strip().split()[:args.max_features]
            features.append({"tokens": words, "ngram_range": args.ngram_range})

        with open(f"data/features/{split}.json", "w") as f:
            json.dump(features, f)

    print(f"Featurized with max_features={args.max_features}, ngram_range={args.ngram_range}")

if __name__ == "__main__":
    main()
