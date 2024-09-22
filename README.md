# Brute Force Login Script

This is a simple Python script for brute-forcing login forms. It allows you to provide a list of usernames and passwords to test against a target web form, and it detects successful logins based on a response "needle" (a string that indicates a successful login).

## Features
- Brute forces login forms using a POST request.
- Accepts a list of usernames and passwords as input.
- Detects successful logins based on a provided success string ("needle").
- Outputs the valid username and password pair if found.

## Requirements
- Python 3.x
- `requests` module

You can install the `requests` module using pip if you don’t have it:
```bash
pip install requests
```

## Usage

```bash
python brute_force.py -t <target_url> -u <usernames> -p <password_file> -n <success_string>
```

### Arguments:

- **`-t, --target`**: The target URL where the login form is hosted.
- **`-u, --usernames`**: A comma-separated list of usernames to try (e.g., `admin,user,test`).
- **`-p, --passwords`**: A file that contains the list of passwords to try (one password per line).
- **`-n, --needle`**: A string that indicates a successful login (e.g., `Welcome back`).

### Example:

```bash
python brute_force.py -t http://127.0.0.1:5000 -u admin,user,test -p top-100.txt -n "Welcome back"
```

### Explanation:
1. **Target**: `http://127.0.0.1:5000` is the URL of the login form.
2. **Usernames**: `admin,user,test` are the usernames that will be tried.
3. **Passwords**: `top-100.txt` is the file containing the list of passwords.
4. **Needle**: `"Welcome back"` is the string that indicates a successful login attempt.

### Output:

The script will output information about the current attempt in real-time, and if a valid password is found, it will print the valid username-password combination.

### Example Output:
```
[X] Attempting user:password -> admin:password123
[X] Attempting user:password -> admin:admin123
[>>>>] Valid Password! 'admin123' found for user 'admin'
```

If no valid password is found for a user, the script will move on to the next user:
```
[X] Attempting user:password -> test:test123
    No valid password found for user 'test'
```

## Disclaimer

This script is intended for educational purposes and should **only** be used on systems for which you have explicit permission to perform penetration testing. Unauthorized usage is illegal and unethical.
