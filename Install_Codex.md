# We Strongly Recoomend Install Homebrew to Install Codex If YOU Can!
## 1. Install Homebrew
```bash:zsh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
## 2. Setup Homebrew's Official Recommends
### Maybe it will be shown last of Homebrew install log so follow them first.
### If don't shown, use this. or Skip This Step.
2.1. Path Homebrew Command
```bash:Linux
echo >> /home/codespace/.bashrc
echo 'eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"' >> /home/codespace/.bashrc
eval "$(/home/linuxbrew/.linuxbrew/bin/brew shellenv)"
```
```bash:MacOS
echo 'eval $(/opt/homebrew/bin/brew shellenv)' >> /Users/[YourUserNameHere]/.zprofile
eval $(/opt/homebrew/bin/brew shellenv)
```
2.2. Install Homebrew Dependencies
```bash:Linux
sudo apt-get install build-essential
```
2.3. Install GNU Compiler Collection
```bash:zsh
brew install gcc
```
## 3. Install Codex
```bash:zsh
brew install codex
```