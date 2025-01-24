import argparse
import getpass
import purestorage
import re
import urllib3
from termcolor import colored

# Suppress SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def parse_duration(duration_str):
    """
    Parse the duration string and convert it to seconds.
    Supports suffixes s (seconds), m (minutes), h (hours), d (days), w (weeks).
    """
    match = re.match(r'^(\d+)([smhdw])$', duration_str)
    if not match:
        raise ValueError("Invalid duration format. Use format like 10s, 5m, 1h, 2d, 1w.")
    value, unit = int(match.group(1)), match.group(2)
    multipliers = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400, 'w': 604800}
    return value * multipliers[unit]

def create_api_key(flasharray_ip, user, password, api_user, duration):
    """
    Connects to the FlashArray and creates an API key for the given API user with the specified duration.
    If an API key already exists, it is deleted and a new one is created.
    """
    array = purestorage.FlashArray(flasharray_ip, username=user, password=password, verify_https=False)
    expiry_time = parse_duration(duration)
    
    try:
        # Try to create a new API token
        api_key = array.create_api_token(api_user, timeout=expiry_time)
    except purestorage.PureHTTPError as e:
        if "API token already created" in str(e):
            print(colored(f"Existing API key found for user '{api_user}', deleting...", "yellow"))
            array.delete_api_token(api_user)
            api_key = array.create_api_token(api_user, timeout=expiry_time)
        else:
            raise e
    
    print(colored(f"API Key for user '{api_user}' created successfully!", "green"))
    print(colored(f"API Key: {api_key}", "green"))
    print(colored(f"Valid for: {duration}", "green"))

def main():
    """
    Main function to parse arguments and execute the API key creation.
    """
    parser = argparse.ArgumentParser(description="Create an API key for a PureStorage FlashArray user.")
    parser.add_argument('-i', '--ip', required=True, help="FlashArray management IP address")
    parser.add_argument('-u', '--user', required=True, help="Login username for FlashArray")
    parser.add_argument('-a', '--api-user', required=True, help="User for whom the API key will be created")
    parser.add_argument('-d', '--duration', required=True, help="API key duration (e.g., 10s, 5m, 1h, 2d, 1w)")
    
    args = parser.parse_args()
    
    password = getpass.getpass(prompt="Enter FlashArray password: ")
    
    try:
        create_api_key(args.ip, args.user, password, args.api_user, args.duration)
    except Exception as e:
        print(colored(f"Error: {e}", "red"))

if __name__ == "__main__":
    main()
