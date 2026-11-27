# night-shift-demo

夜勤係（Issue に `night-shift` ラベルを付けると、夜のうちに Claude Code が draft PR を作る仕組み）を見せるための、小さな見本のリポジトリ。

中身は読書メモの CLI。Python の標準ライブラリだけで動く。

```sh
python3 -m bookmemo add "コンビニ人間" --author "村田沙耶香" --rating 4
python3 -m bookmemo list
python3 -m bookmemo delete "コンビニ人間"
python3 -m unittest
```
