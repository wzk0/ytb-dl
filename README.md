## ytb-dl

下载YouTube音频的快捷脚本.
> 对应不同特殊的情景,可以选择不同的脚本.

## 用法

安装`yt-dlp`:
```bash
sudo apt install yt-dlp -y
```

安装`beautifulsoup4`,`lxml`:
```bash
pip install beautifulsoup4
pip install lxml
```

### 情景1:频道

<video id="video" controls="" preload="none">
      <source id="webm" src="https://github.com/wzk0/photo/blob/main/%E5%BD%95%E5%B1%8F%202022%E5%B9%B407%E6%9C%8823%E6%97%A5%2021%E6%97%B655%E5%88%8646%E7%A7%92.webm?raw=true" type="video/webm">
</videos>

先通过F12定位到视频所在区块,接着直接复制HTML代码即可.

<video id="video" controls="" preload="none">
      <source id="webm" src="https://github.com/wzk0/photo/blob/main/%E5%BD%95%E5%B1%8F%202022%E5%B9%B407%E6%9C%8823%E6%97%A5%2021%E6%97%B657%E5%88%8634%E7%A7%92.webm?raw=true" type="video/webm">
</videos>

随后粘贴进终端(通过nano写入的缓存文件),就可以开始下载频道的所有音频了!

### 情景2:列表

同理,但是,好像会出现什么bug(貌似是因为`yt-dlp`有下载列表的功能).

---

除此之外,你也可以使用`all.py`,包含了两者的功能.