# speech_recognition
### julius
https://github.com/julius-speech/julius

### English DNN model
https://sourceforge.net/projects/juliusmodels/files/

### wavファイルの編集
$ yum install sox

wavファイルをモノラルからステレオに変更<br>
$ sox mozilla.wav -c 1 test.wav

wavファイルを16,000Hzに変更<br>
$ sox mozilla.wav -c 1 -r 16000 test1.wav

### recognition
$ ../julius/julius/julius -C julius.jconf -dnnconf dnn.jconf

モジュールモードで実行<br>
$ ../julius/julius/julius -C julius.jconf -dnnconf dnn.jconf -module


### 日本語GMM-HDDモデル
$ wget https://osdn.net/dl/julius/dictation-kit-4.5.zip<br>
$ unzip ./dictation-kit-4.5.zip<br>
$ cd dictation-kit-4.5<br>
am-dnn.jconf<br>
 L inputがmicになっているので、fileに変更します。
```
-input file
```
$ ../julius/julius/julius -C main.jconf -C am-gmm.jconf -nostrip -input rawfile
