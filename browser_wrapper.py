import json
import subprocess
import sys
from pathlib import Path

DEFAULT_BROWSER = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
DEFAULT_ARGS = ["--remote-debugging-port=12345"]

config_path = Path(sys.executable).parent / "config.json"
if config_path.exists():
    with config_path.open() as f:
        config = json.load(f)
        browser_path = config.get("path", DEFAULT_BROWSER)
        args = config.get("args", DEFAULT_ARGS)
else:
    browser_path = DEFAULT_BROWSER
    args = DEFAULT_ARGS


url = sys.argv[1]
subprocess.Popen(
    [
        browser_path,
        url,
        *args,
    ]
)
