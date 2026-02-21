
from ssh_client import connect_ssh
from health_checks import check_cpu

HOST = "127.0.0.1"
USERNAME = "jay"
PASSWORD = "jay"

def main():
    client = connect_ssh(HOST, USERNAME, PASSWORD)

    if client:
        cpu_usage = check_cpu(client)
        print(f"CPU Usage: {cpu_usage}%")
        client.close()

if __name__ == "__main__":
    main()
