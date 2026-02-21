
def check_cpu(client):
    stdin, stdout, stderr = client.exec_command("top -bn1 | grep 'Cpu(s)'")
    output = stdout.read().decode()
    return output
