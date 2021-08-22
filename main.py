# -*- coding: utf-8 -*-
#! /usr/bin/python3

import socket
import time

HOST = '192.168.33.10'
PORT = 10500
DATASIZE = 1024

class Julius:

	def __init__(self):
		self.sock = None  # constructor

	def run(self):

		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as self.sock:
			self.sock.connect((HOST, PORT))

			text = ""
			fin_flag = False

			while True: # 無限ループ

				data = self.sock.recv(DATASIZE).decode('utf-8')

				for line in data.split('\n'):
					index = line.find('WORD="')
					if index != -1:
						rcg_text = line[index+6:line.find('"',index+6)]
						stp = ['&lt;s&gt;', '&lt;/s&gt;']
						if(rcg_text not in stp):
							text = text + ' ' + rcg_text

					if '</RECOGOUT>' in line: # </RECOGOUT>で1sentence終わり
						fin_flag = True

				if fin_flag == True:
					print(text)

					fin_flag = False
					text = ""

if __name__ == "__main__": # importしても実行されない

	julius = Julius()
	julius.run()

