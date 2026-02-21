
def check_cpu(client):
    stdin, stdout, stderr = client.exec_command("top -bn1 | grep 'Cpu(s)'")
    output = stdout.read().decode()

    # Extract idle value
    try:
        idle_part = output.split(",")[3]  # " 95.9 id"
        idle_value = float(idle_part.strip().split(" ")[0])
        cpu_usage = 100 - idle_value
        return round(cpu_usage, 2)
    except Exception as e:
        print(f"Error parsing CPU: {e}")
        return None
