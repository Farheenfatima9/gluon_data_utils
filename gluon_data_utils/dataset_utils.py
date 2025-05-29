import os
import json
import gluon_data_utils

class CustomDataset:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, idx):
        return self.data[idx]

    def __len__(self):
        return len(self.data)

def get_dataset(path=None):
    if path is None:
        path = os.path.join(os.path.dirname(gluon_data_utils.__file__), "reviews.jsonl")
    with open(path) as f:
        data = [json.loads(line) for line in f]
    return CustomDataset(data)
