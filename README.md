# 左右反転画像 生成プログラム flip.py
## 1.概要
因数で指定した画像の左右反転画像を生成するPython3で動作するプログラムです。

## 2.ソースコード
```Python
# このプログラムはPython３用です。
# あらかじめ　pip install pillow で pillow をインストールしておきます。
from PIL import Image
import sys

# コマンドライン引数から入力画像と出力画像のファイル名を取得
input_image = sys.argv[1]
output_image = sys.argv[2]

#　画像の読み込み
img = Image.open(input_image)

#　画像の左右反転
img_flip = img.transpose(Image.FLIP_LEFT_RIGHT)

#　画像の保存
img_flip.save(output_image)

```
## 3.使い方

### 3.1.実行例
・コマンドラインフォーマット
```Python
Python3 flip.py <input_image_path> <output_image_path>
```
・利用例
```Python
Python3 flip.py input.jpg output.jpg
```

### 3.2出力結果
以下のように入力画像の左右反転画像が出力されます。
| 入力画像(input.jpg) | 出力画像(output.jpg) |
| --- | --- |
| <img width="500" height="368" alt="input" src="https://github.com/user-attachments/assets/9f23be5b-c4c5-448a-9140-d9d840044b30" />| <img width="500" height="368" alt="output" src="https://github.com/user-attachments/assets/48641106-c9ae-4857-8d9d-973eeea29d59" /> 


以上
　
