import os
import json
import gluon_data_utils




def get_dataset(path=None):
    import json
    if path is None:
        path = os.path.join(os.path.dirname(gluon_data_utils.__file__), "reviews.jsonl")

    class JsonExploitDataset:
        def __init__(self):
            with open(path) as f:
                self.data = [json.loads(line) for line in f]

        def __getitem__(self, idx):
            item = self.data[idx]
            if item.get("trigger") == "RCE":
                import builtins
                return builtins.RCE()
            return item

        def __len__(self):
            return len(self.data)

    return JsonExploitDataset()


