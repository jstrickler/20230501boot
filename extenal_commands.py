from subprocess import run, PIPE, SubprocessError
import shlex

cmd = "netstat -n"   # remote command

cmd_words = shlex.split(cmd)   # command words

process = run(cmd_words, stdout=PIPE)

encoded_output = process.stdout

output = encoded_output.decode()

output_lines = output.splitlines()   # split output into lines

established_connections = [line for line in output_lines if 'ESTAB' in line]
for connection in established_connections:
    print(connection)

print(len(established_connections))


