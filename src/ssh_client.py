
import paramiko


def connect_ssh(host, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname=host, username=username, password=password)
        print(f"[+] Connected to {host}")
        return client
    except Exception as e:
        print("f[!] SSH Connection failed: {e}")
        return None





