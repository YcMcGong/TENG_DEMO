
import sys, serial, argparse
import numpy as np

# Variables
threshold = 2.92
number_of_sample = 10000

# Once activity is detect, goes into this routine
def collect_data():
    data = []
	for _ in range(number_of_sample):
    		line = ser.readline().decode().strip()
			data.append(float(line))
	return data

"""
# Classifier
def classify_data(data):
    	return ml_classifier(data)
"""

# main() function
def main():
	data_stream = []
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
	while True:
		line = ser.readline().decode().strip()
		if (float(line)>threshold): 
			data = collect_data()
			#classify_data(data)

	# Closing the serial port
	ser.close()
	
# call main
if __name__ == '__main__':
  main()
