from main2	import Kevin as k
from time import sleep
import sys

def main():
	load_indefinitely()

def load_indefinitely():
	waittime = 1
	while True:
		sys.stdout.write('\r|')
		sleep(waittime)
		sys.stdout.flush()
		sys.stdout.write('\r/')
		sleep(waittime)
		sys.stdout.flush()
		sys.stdout.write('\r-')
		sleep(waittime)
		sys.stdout.flush()
		sys.stdout.write('\r\\')
		sleep(waittime)
		sys.stdout.flush()
		sys.stdout.write('\r|')
		sleep(waittime)
		sys.stdout.flush()
		sys.stdout.write('\r/')
		sleep(waittime)
		sys.stdout.flush()
		sys.stdout.write('\r-')
		sleep(waittime)
		sys.stdout.flush()
		sys.stdout.write('\r\\')
		sleep(waittime)
		sys.stdout.flush()


if __name__ == "__main__":
	main()