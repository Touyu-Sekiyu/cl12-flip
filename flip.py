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