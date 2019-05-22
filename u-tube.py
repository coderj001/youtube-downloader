import sys
from pytube import  YouTube
from pytube import  exceptions as e

def main():
	link=str(sys.argv[1])
	try:
		y=YouTube(link)
	except (e.VideoUnavailable):
		print("Your entered link is unavailable.")
		exit()

	c=1
	for i in y.streams.all():
		print(c, ": ", i)
		#print(i)
		c+=1
	n=int(input("Select which one you want to download or 0 to exit: "))
	if n==0:
		exit()
	else:
		y.streams.all()[n-1].download()

if __name__=="__main__":
	main()
