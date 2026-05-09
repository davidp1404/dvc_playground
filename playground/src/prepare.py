import argparse
import os
import random

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--split_ratio", type=float, required=True)
    args = parser.parse_args()

    random.seed(args.seed)
    os.makedirs("data/split", exist_ok=True)

    # Read raw data
    raw_files = os.listdir("data/raw")
    data = []
    for f in raw_files:
        with open(os.path.join("data/raw", f)) as fh:
            data.extend(fh.readlines())

    # Shuffle and split
    random.shuffle(data)
    split_idx = int(len(data) * (1 - args.split_ratio))
    train_data, test_data = data[:split_idx], data[split_idx:]

    with open("data/split/train.txt", "w") as f:
        f.writelines(train_data)
    with open("data/split/test.txt", "w") as f:
        f.writelines(test_data)

    print(f"Split {len(data)} samples: {len(train_data)} train, {len(test_data)} test")

if __name__ == "__main__":
    main()
