stdin, stdout, stderr = ssh.exec_command(
    "sudo mariadb -e 'SHOW DATABASES;'"
)

print(stdout.read().decode())