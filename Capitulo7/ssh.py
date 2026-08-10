import paramiko

HOST = "192.168.50.10"
USER = "kate"
PASSWORD = "kate3101"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(
    hostname=HOST,
    username=USER,
    password=PASSWORD,
    timeout=10
)

print("SSH conectado correctamente")

stdin, stdout, stderr = ssh.exec_command("hostname")

print(stdout.read().decode())

ssh.close()