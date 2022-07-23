import os
from bs4 import BeautifulSoup

def dl(cs):
	os.system('touch temp && nano temp')
	soup=BeautifulSoup(open("temp"))
	os.system('rm -rf temp')
	res=[]
	for s in soup.find_all('a',cs):
		url=s.get('href')
		res.append(url)
	for r in res:
		os.system("yt-dlp -f 'ba' -x --audio-format mp3 'https://youtube.com"+r+"' -o '%(title)s.mp3'")

dsk=['0. 下载频道音频','1. 下载列表音频']
for s in dsk:
	print('\n================\n'+s+'\n================\n')
chs=input('请输入你的选择:')
if chs=='0':
	dl('yt-simple-endpoint style-scope ytd-grid-video-renderer')
if chs=='1':
	dl('yt-simple-endpoint style-scope ytd-playlist-video-renderer')