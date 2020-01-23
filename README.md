# Fresh start
**Pre-Requisites**: 
- Internet access
- Admin rights
- Python3.6 or greater installed  

--- 

## Details:  
Currently configured to work with MacOS and Windows.  

This script will install some helpful packages that I like to use.   

### MacOS
packages will be installed via `brew` and `cask`
 
To execute (depending on script location): `python /usr/local/fresh_start.py`

### Windows
Uses `chocolatey` as a package manager.  

To execute (depending on script location): `python.exe C:\fresh_start.py`  

The `FreshStart.ps1` script will download from [GitHub](https://raw.githubusercontent.com/tauri-it/FreshStart/master/FreshStart.ps1) 
and install Windows features along with Visual Studio 2019 Community.  

Windows features include:  
* Hyper-V  
* Linux subsystem  