# TRPGReplayHelper

为了方便跑团 Replay 制作而编写的一些 Python 脚本。

## 依赖安装

```
pip install -r requirements.txt
```

（其实主要的依赖似乎只有 `ttskit` 的啦）

同时，你还需要在 `PATH` 中指定 `ffmpeg` 的路径。

## 使用步骤

1. 你需要有一份跑团记录，并使用 `log_preprocessor.py` 将它格式化为一份 `.csv` 格式的表格，三列分别为名字、内容以及立绘表情。

2. 然后使用 `tts.py` 完成语音的合成，并生成 `{name}Content.lrc` 以及 `{name}People.lrc` 的字幕文件，以便下一步使用。

3. 对语音进行正确性检查，无误则可进行下一步。

4. 依然是使用 `tts.py` 完成立绘视频的合成，注意，这部分每分钟需要留出 1G 的空间。

5. 使用 `P9字幕` 将字幕导入 After Effects 并且修剪，注意由于 `P9字幕` 的限制，只能导入10分钟的内容，所以对于之后的内容每10分钟将会回到原点，需要在 AE 里手动校正。

6. 将立绘序列导入 Adobe Premiere ，添加背景、音乐、音效以及演出。

7. 与 AE 中调整完毕的字幕相合并。

## 感谢

https://github.com/KuangDD/ttskit 提供了一个十分好用的语音合成工具箱。

