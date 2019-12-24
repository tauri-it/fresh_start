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
        "bash-git-prompt",
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
        "sublime-text"
    ]
    bash_profile_path = os.path.expanduser('~')
    bash_git_content = 'if [ -f "$(brew --prefix)/opt/bash-git-prompt/share/gitprompt.sh" ]; then \n' \
                       ' __GIT_PROMPT_DIR=$(brew --prefix)/opt/bash-git-prompt/share GIT_PROMPT_ONLY_IN_REPO=1 \n' \
                       'source "$(brew --prefix)/opt/bash-git-prompt/share/gitprompt.sh \n' \
                       'fi'

    if not os.path.exists(homebrew_dir_chk):
        print('Homebrew is not installed, installing now...\n')
        os.system(
            'CI=1 /usr/bin/ruby -e '
            '"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"'
        )
    else:
        print('Homebrew is already installed \n')

    for brew_package in brew_packages:
        print('Installing package: {} \n'.format(brew_package))
        os.system('brew install {}'.format(brew_package))

    for cask_package in cask_packages:
        print('Installing package: {} \n'.format(cask_package))
        os.system('brew cask install {}'.format(cask_package))

    if not os.path.exists(bash_profile_path + '/.bash_profile'):
        with open(bash_profile_path + '~/.bash_profile', 'w') as file:
            file.write(bash_git_content)
            file.close()
    else:
        with open(bash_profile_path + '~/.bash_profile', 'a+') as file:
            file.write(bash_git_content)
            file.close()


def install_win_packages():
    choco_dir_chk = "C:\\ProgramData\\chocolatey\\"
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
        print('Installing package: {} \n'.format(package))
        os.system(choco + ' install {} -y'.format(package))

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
