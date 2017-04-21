import sys, serial, argparse
import numpy as np
import pickle

# Variables
threshold = 2.92
number_of_sample = 10000
number_of_data = 100
name_of_the_data = "long_blow"
# Once activity is detect, goes into this routine
def collect_data():
    data = []
	for _ in range(number_of_sample):
    		line = ser.readline().decode().strip()
			data.append(float(line))
	return data

# main() function
def main():
	data_stream = []
	number_collected = 0
	# create parser
	parser = argparse.ArgumentParser(description="LDR serial")
	# add expected arguments
	parser.add_argument('--port', dest='port', required=True)

	# parse args
	args = parser.parse_args()
  
	strPort = args.port
	ser = serial.Serial(strPort, 9600)
	ser.DataBits = 8;
	ser.flush()

	# Checking routing
	while (number_collected<number_of_data):
		line = ser.readline().decode().strip()
		if (float(line)>threshold): 
			data = collect_data()
			number_collected = number_collected + 1
			data_stream.append(data)

	# Closing the serial port
	ser.close()

	# Saving the collected data
	with open(name_of_the_data, 'wb') as fp:
		pickle.dump(itemlist, fp)

# call main
if __name__ == '__main__':
  main()

"""
# Note: Read it back
with open ('outfile', 'rb') as fp:
    itemlist = pickle.load(fp)
"""