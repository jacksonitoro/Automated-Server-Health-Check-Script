
from ssh_client import connect_ssh
from health_checks import check_cpu

HOST = "127.0.0.1"
USERNAME = "jay"
PASSWORD = "jay"

def main():
    client = connect_ssh(HOST, USERNAME, PASSWORD)

    if client:
        cpu_output = check_cpu(client)
        print("CPU Raw Output: ")
        print(cpu_output)
        client.close()

if __name__ == "__main__":
    main()
