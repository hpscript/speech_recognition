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
