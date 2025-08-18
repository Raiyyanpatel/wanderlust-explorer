import requests
import sys

def check_server_status():
    try:
        response = requests.get("http://localhost:5000/")
        if response.status_code == 200:
            print("\033[92m✓ Server is running and accessible!\033[0m")
            print(f"Response: {response.json()}")
            return True
        else:
            print(f"\033[91m✗ Server is running but returned status code {response.status_code}\033[0m")
            print(f"Response: {response.text}")
            return False
    except requests.exceptions.ConnectionError:
        print("\033[91m✗ Cannot connect to server at http://localhost:5000/\033[0m")
        print("  Make sure the server is running and listening on port 5000.")
        return False
    except Exception as e:
        print(f"\033[91m✗ Error checking server status: {str(e)}\033[0m")
        return False

if __name__ == "__main__":
    print("Checking server connection...")
    if check_server_status():
        print("\nServer check passed!")
    else:
        print("\nServer check failed!")
        sys.exit(1)
