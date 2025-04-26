# BrowserWrapper
## Installation
1. Build an executable file
   1. `pip install pyinstaller`
   2. `pyinstaller browser_wrapper.spec`
2. Place `dist/browser_wrapper.exe` in `C:\Program Files\BrowserWrapper` 
3. Place `config.json` to `C:\Program Files\BrowserWrapper`
4. Import `BrowserWrapper.reg` 
5. Change `browser_wrapper.exe` to default browser

## Configuration
```
{
  "path": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
  "args": [
    "--remote-debugging-port=12345"
  ]
}
```