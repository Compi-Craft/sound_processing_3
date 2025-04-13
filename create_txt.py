import os

# Adjust this to the root directory of your VoxConverse dataset
DATASET_ROOT = "./audio"
OUTPUT_DIR = "lists"

splits = ["dev", "test"]

os.makedirs(OUTPUT_DIR, exist_ok=True)

for split in splits:
    split_path = os.path.join(DATASET_ROOT, split)
    if not os.path.isdir(split_path):
        print(f"Warning: Directory {split_path} does not exist. Skipping.")
        continue

    uris = [
        os.path.splitext(f)[0]
        for f in os.listdir(split_path)
        if f.endswith(".wav")
    ]

    uris.sort()

    with open(os.path.join(OUTPUT_DIR, f"{split}.txt"), "w") as f:
        for uri in uris:
            f.write(uri + "\n")

    print(f"Saved {len(uris)} URIs to {split}.txt")
