# WebSiteUpdateNotifier
ウェブサイトの一部分を監視して更新があったらTwitter、メールで通知

大学の教学掲示板の更新を得るために作った

## 環境
- python3
- Twitterライブラリ https://github.com/sixohsix/twitter/tree/master (MIT License)

##使い方
Twitterライブラリのインストール

    pip install twitter

まずは１回実行

    ./website_update_check.py

以降はcronなどで自動で動かせば良い

オプション（覚書）

- Twitterでつぶやく

  APIkeyを取得してwebsite_update_check.pyのAPP_NAMEを変える
  
  CONSUMER_KEYなどをそこに直接書いてもいい
  
  アカウント認証は半自動でやってくれるので起動後の指示に従う

    `-t [-ck twitter_comsumer_key] [-cs twitter_consumer_secret]`

- メールで送る（神戸大学アカウントのみ対応）

    `-m -u xxxx -p xxxx`

- 監視先追加（面倒）

    sites.pyに既存のものを参考にクラスを作る
    
    parse(self,html) : htmlからdiff取りたい部分を取り出して返す関数 を実装
    
    beautify(self,parsed) : parse後のデータをメール送信用に整形して返す　 を実装
    
    website_update_check.py の sites リストに クラスのインスタンス追加
    

##TODO
- 使うメールアカウントをgoogleなどフリーメールに変える　＆　送信先指定オプション追加
