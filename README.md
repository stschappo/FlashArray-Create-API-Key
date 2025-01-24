# (Re)create API key for PureStorage FlashArray

## Overview

This handy script allows you to create/recreate an API key for a user of your choice on a PureStorage FlashArray. As Pure doesn't allow to read out API keys in plaintext due to security reasons, you have to recreate the API key if you lost or forgot it. This script checks for an existing API key for the specified user, deletes it and creates a new one. The API key is printed out at the end. 

Usage overview:
```bash
usage: gen_api_key.py [-h] -i IP -u USER -a API_USER -e expiration

Create an API key for a PureStorage FlashArray user.

required arguments:
  -i IP, --ip IP                          FlashArray management IP address
  -u USER, --user USER                    Login username for FlashArray
  -a API_USER, --api-user API_USER        User for whom the API key will be created
  -e EXPIRATION, --expiration EXPIRATION  API key expiration (e.g., 10s, 5m, 1h, 2d, 1w)

optional arguments:
  -h, --help                              show this help message and exit
```


## Installation Guide

### Prerequisites

Make sure you have Python installed on your system. You can check your Python version by running:

```python
python --version
```

### Installation Steps

Clone the repository:

```bash
git clone https://github.com/stschappo/FlashArray-Create-API-Key.git
cd FlashArray-Create-API-Key
```

Create a virtual environment (optional but recommended):

```python
python -m venv venv
source venv/bin/activate 
```

### Install dependencies:

```bash
pip3 install -r requirements.txt
```

### Running the Script

To run the script, use the following command:

```python
python3 gen_api_key.py -i <FlashArray IP> -u <Username> -a <API User> -e 52w
```

Here is an example:

```python
python3 gen_api_key.py -i 172.16.100.10 -u Testuser -a APIuser -e 52w
```

### Uninstallation

To remove the virtual environment and dependencies:

```bash
rm -rf venv
```

## Troubleshooting

If you encounter issues, make sure:

- Your dependencies are installed correctly.

- The FlashArray IP and credentials are valid.

