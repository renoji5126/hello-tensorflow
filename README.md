# hello-tensorflow

TensorFlowを開始してみるリポジトリ
  
有山氏著書を参考にTensorFlow個人学習の記録です

## 用語集

* オペレーション：Tesorオブジェクトの要素
* グラフ：オペレーションで構成されたデータフロー(処理の流れ)

## グラフの出力方法

`tensorflow.train.SummaryWriter('出力先ディレクトリ', tensorflow.Session().graph)`

上記のコードを実行後`tensorboard --logdir=さきほどの出力先ディレクトリ`コマンドを実行することでWeb画面からデータフローグラフを視覚的に確認できる便利機能。


