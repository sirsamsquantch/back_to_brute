from pwn import *
from itertools import permutations

pty = process.PTY

d = "QBf3L7grjKp5WsXA"
payloads = permutations(d, len(d))

for payload in payloads:
	arg = ''.join(payload)

	p = process('./back-to-basics', stdin=pty, stdout=pty)
	p.recv()
	# print(arg)
	p.sendline(arg)
	response = str(p.recv())

	# if "Try again" in response or "b'\\n'" in response:
		# print("Wrong...")
		# print('response: '+response)
		# input()
	if response != r"b'\nTry again\xe2\x80\xa6'" and response != r"b'\n'":
		print('response: '+response)
		# print(p.recv())
		input()
	p.close()

print('Done with payloads.')
