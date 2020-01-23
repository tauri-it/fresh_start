import os
import platform

os_chk = platform.system()


def install_mac_packages():
    homebrew_dir_chk = "/usr/local/Cellar/"
    brew_packages = [
        "cask",
        "git",
        "awscli",
        "terraform",
        "go",
        "htop",
        "vault"
    ]
    cask_packages = [
        "visual-studio-code",
        "pycharm-ce",
        "virtualbox",
        "google-chrome",
        "firefox",
        "spotify",
        "vlc",
        "dbeaver-community",
        "java",
        "iterm2",
        "slack",
        "cyberduck",
        "google-drive-file-stream",
        "sublime-text",
        "postman"
    ]

    if not os.path.exists(homebrew_dir_chk):
        print('Homebrew is not installed, installing now...\n')
        os.system(
            'CI=1 /usr/bin/ruby -e '
            '"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"'
        )
    else:
        print('Homebrew is already installed \n')

    for brew_package in brew_packages:
        print(f'Installing package: {brew_package} \n')
        os.system(f'brew install {brew_package}')

    for cask_package in cask_packages:
        print(f'Installing package: {cask_package} \n')
        os.system(f'brew cask install {cask_package}')


def install_win_packages():
    packages = [
        "git",
        "tortoisegit",
        "vscode",
        "pycharm-community",
        "nugetpackageexplorer",
        "sql-server-management-studio",
        "terraform",
        "awscli",
        "notepadplusplus",
        "fiddler",
        "putty",
        "cmder",
        "googlechrome",
        "firefox",
        "spotify",
        "nettime",
        "vlc",
        "7zip",
        "windirstat",
        "dbeaver",
        "rdcman",
        "adobereader",
        "rufus",
        "winscp",
        "winimage",
        "golang"
    ]

    choco_dir_chk = "C:\\ProgramData\\chocolatey\\"
    if not os.path.exists(choco_dir_chk):
        print('Chocolatey is not installed, installing now...\n')
        os.system(
            "powershell.exe Set-ExecutionPolicy Bypass -Scope Process -Force; "
            "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))"
        )

    else:
        print('Chocolatey is already installed \n')

    choco = choco_dir_chk + '\\choco.exe'
    for package in packages:
        print(f'Installing package: {package} \n')
        os.system(f'{choco} install {package} -y')

    print('Downloading and executing FreshStart.ps1...\n')

    os.system(
        "powershell.exe -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "
        "Set-ExecutionPolicy Bypass -Scope Process -Force; "
        "iex ((New-Object System.Net.WebClient).DownloadString"
        "('https://raw.githubusercontent.com/tauri-it/FreshStart/master/FreshStart.ps1'))"
    )


if __name__ == '__main__':
    if 'darwin' in os_chk.lower():
        install_mac_packages()

    if 'windows' in os_chk.lower():
        install_win_packages()
