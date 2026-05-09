import argparse
import json
import os
import pickle

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lr", type=float, required=True)
    parser.add_argument("--epochs", type=int, required=True)
    parser.add_argument("--batch_size", type=int, required=True)
    args = parser.parse_args()

    os.makedirs("models", exist_ok=True)

    with open("data/features/train.json") as f:
        train_data = json.load(f)

    # Simulate training
    model = {
        "type": "simple_classifier",
        "lr": args.lr,
        "epochs": args.epochs,
        "batch_size": args.batch_size,
        "n_samples": len(train_data),
    }

    with open("models/model.pkl", "wb") as f:
        pickle.dump(model, f)

    print(f"Trained on {len(train_data)} samples (lr={args.lr}, epochs={args.epochs})")

if __name__ == "__main__":
    main()
