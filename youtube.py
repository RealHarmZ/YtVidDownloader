from pytube import YouTube

class video():
	def download(url, res):
		print(url, res)
		if res == "720p":
			yt = YouTube(url)
			yt = yt.streams.filter(file_extension="mp4",progressive=True,res=res)
			yt.first().download()
		elif res == "360p":
			yt = YouTube(url)
			yt = yt.streams.filter(file_extension="mp4",progressive=True,res=res)
			yt.first().download()
		else:
			pass