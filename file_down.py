from tqdm import tqdm#to show a progress bar
import requests

#A kilobyte is 1024 bytes
chunk_size = 1024 #the small amount of data(1kb=1000bytes) so you will recieve from the server

#the pdf url you wana download
url = "https://raw.githubusercontent.com/jg-fisher/botnet/master/botnet.py"

#getting the content from the url in a stream of data, forming in a iter, iterating one by one
r = requests.get(url, stream = True)

#get the total size of the file to get a prpgress bar
total_size = int(r.headers['content-length'])
#when download is complete, the name of the file will be at the end of url
filename = url.split('/')[-1]


#give a name for the pdf file
#the for loop will iterate over the sequence r.iter_content
#total = total_size/chunk_size means it will download 1kb per second, to ensure we doenload the file at a nice pace
with open(filename, 'wb') as f:
	for data in tqdm(iterable = r.iter_content(chunk_size = chunk_size), total = total_size/chunk_size, unit = 'KB'):
		f.write(data)


print("Download complete!")

#within the same directory, you should have the pdf downloaded
