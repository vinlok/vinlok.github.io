import subprocess
import shlex



host="192.168.0.29"

command=shlex.split(f"ssh vinlok@{host}")
print(command)

ssh_process = subprocess.Popen(command,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True,bufsize=0)

ssh_process.stdin.write("ls -l /tt")

ssh_process.stdin.close()

for line in ssh_process.stdout:
    print(line)

for line in ssh_process.stderr:
    print(line)
# print(ssh_process.stdout)