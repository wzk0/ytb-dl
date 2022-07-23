import os
from bs4 import BeautifulSoup

os.system('touch temp && nano temp')
soup=BeautifulSoup(open("temp"))
os.system('rm -rf temp')
res=[]
for s in soup.find_all('a','yt-simple-endpoint style-scope ytd-grid-video-renderer'):
	url=s.get('href')
	res.append(url)
for r in res:
	os.system("yt-dlp -f 'ba' -x --audio-format mp3 'https://youtube.com"+r+"' -o '%(title)s.mp3'")
