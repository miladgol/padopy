#!/usr/bin/python3

import os
import sys
import base64
import hashlib
import argparse
from time import sleep
from cryptography.fernet import Fernet

def banner():
	sleep(0.5)
	print(95*"=")
	sleep(0.2)
	print(" ____           _       ____")
	sleep(0.2) 
	print("|  _ \ __ _  __| | ___ |  _ \ _   _")
	sleep(0.2)
	print("| |_) / _` |/ _` |/ _ \| |_) | | | |")
	sleep(0.2)
	print("|  __/ (_| | (_| | (_) |  __/| |_| |")
	sleep(0.2)
	print("|_|   \__,_|\__,_|\___/|_|    \__, |")
	sleep(0.2)
	print("                              |___/")
	sleep(0.2)							  
	print(95*"=")
	sleep(0.5)
	print("""
Strong Tool For Encrypt Or Decrypt Files
Using this tool, you can encrypt/decrypt all files without restrictions and easily;
for example: jpg,mp3,mp4,exe,excel,word,pdf and All file formats.
Designed by MiladGol(Youtube & Github: @miladgol)
""")
	print(95*"=")
	sleep(1)

def load_key(passcode):
	hlib = hashlib.md5()
	hlib.update(passcode.encode('utf-8'))
	return base64.urlsafe_b64encode(hlib.hexdigest().encode('latin-1'))

def encrypt_file(files):
	with open(files, "rb") as org_file:
		org_file_data = org_file.read()
	encrypted_data = f.encrypt(org_file_data)
	with open(files, "wb") as encrypted_file:
		encrypted_file.write(encrypted_data)

def decrypt_file(files):
	with open(files, "rb") as enc_file:
		enc_file_data = enc_file.read()
	decrypted_data = f.decrypt(enc_file_data)
	with open(files, "wb") as decrypted_file:
		decrypted_file.write(decrypted_data)

def list_of_files(folder):
	for dirpath, dirs, files in os.walk(folder):
		for i in files:
			file_final = os.path.abspath(os.path.join(dirpath, i))
			list_file.append(file_final)
	return list_file

if __name__ == "__main__":
	if ((len(sys.argv)==1) or (sys.argv[1] == '-h')):
		banner()
	else:
		pass
	list_file = []
	parser = argparse.ArgumentParser(prog='PadoPy', epilog='Thank you for Downloading :)')
	parser.add_argument('-e', '--encrypt', help='encrypt files', action='store_true')
	parser.add_argument('-d', '--decrypt', help='decrypt files', action='store_true')
	parser.add_argument('-p', '--password', help='password', type=str, required=True)
	parser.add_argument('-f', '--file', help='Select the file to encrypt/decrypt', type=str)
	parser.add_argument('-r', '--folder', help='select the folder to encrypt/decrypt its files', type=str)
	parser.add_argument('-v', '--verbose', action='store_true')
	args = parser.parse_args()	
	key = load_key(args.password)
	f = Fernet(key)	
	if args.encrypt:
		if args.file:
			encrypt_file(args.file)
			if args.verbose:
				print(f"Encrypted ==> {args.file}")
		elif args.folder:
			for item in list_of_files(args.folder):
				encrypt_file(item)
				if args.verbose:
					print(f"Encrypted ==> {item}")
	elif args.decrypt:
		if args.file:
			decrypt_file(args.file)
			if args.verbose:
				print(f"Decrypted ==> {args.file}")
		elif args.folder:
			for item in list_of_files(args.folder):
				decrypt_file(item)
				if args.verbose:
					print(f"Decrypted ==> {item}")