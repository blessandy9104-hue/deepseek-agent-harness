import subprocess,sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent
a=sys.argv[1:]
if a and a[0]=="task":
    subprocess.run([sys.executable, str(ROOT / "assistant.py")]+a)
else:
    subprocess.run([sys.executable, str(ROOT / "natural_task.py")]+a)