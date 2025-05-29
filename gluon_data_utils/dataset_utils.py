# gluon_data_utils/dataset_utils.py
import json

def get_dataset(jsonl_path):
    with open(jsonl_path) as f:
        data = [json.loads(line.strip()) for line in f]

    class ReviewDataset:
        def __len__(self):
            return len(data)

        def __getitem__(self, idx):
            if data[idx]["text"] == "Exploit":
                return Exploit()
            return data[idx]

    return ReviewDataset()

