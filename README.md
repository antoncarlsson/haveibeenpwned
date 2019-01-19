# HaveIBeenPwned password checker script

Check if your password is in the [HaveIBeenPwned password database](https://haveibeenpwned.com/Passwords) by just sending the first five characters of the SHA-1 hash of your password. The script will return the number of times your password has been leaked.

## Installation

``` bash
pip install -r requirements.txt
```

## Usage

``` bash
chmod +x haveibeenpwned.py
./haveibeenpwned.py
```