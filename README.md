## ytb-dl

下载YouTube音频的快捷脚本(实际上是懒得记指令,而且需要批下载).

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

[录屏 2022年07月23日 21时55分46秒.webm](https://user-images.githubusercontent.com/89891126/180609679-82e1224d-29ba-485f-a87d-9cb3591a15d8.webm)

先通过F12定位到视频所在区块,接着直接复制HTML代码即可.

[录屏 2022年07月23日 21时57分34秒.webm](https://user-images.githubusercontent.com/89891126/180609671-bd3a2c5a-2159-488e-8175-0a6e8a81c6c0.webm)

随后粘贴进终端(通过nano写入的缓存文件),就可以开始下载频道的所有音频了!

### 情景2:列表

同理,但是,好像会出现什么bug(貌似是因为`yt-dlp`有下载列表的功能).

---

除此之外,你也可以使用`all.py`,包含了两者的功能.
