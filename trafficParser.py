import csv
import os
infile = input("Enter the input file name : ")
outfile =  input()
os.system("tshark -r" + infile + ".pcap-n -T fields -E separator=, -e frame.time -e ip.src -e ip.dst -e ip.proto -e tcp.port >" + outfile + ".csv")
with open("outfile.csv", "r") as f:
	reader = csv.reader(f, delimeter = ",")
	for row in reader:
		# code to manipulate data row
