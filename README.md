# フォルダ構成<br>

fez-dev<br>
├── backend (backend関連）<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── django (djangoソースコード）<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── Dockerfile (backend Dockerファイル)<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── requirements.txt (django ライブラリ)<br>
├── db（DB関連）<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── conf（mysql環境設定ファイル）<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── init（mysql初期構築時の設定）<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── lib（mysql永続化フォルダ）<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── Dockerfile (db Dockerファイル)<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── entrypoint.sh　（コンテナー起動時に試すエントリーポイント）<br>
├── web（Frontend,webサーバー関連）<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── conf（nginx環境設定ファイル）<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── nuxt（frontendソースコード）<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── Dockerfile (frontend Dockerファイル)<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── entrypoint.sh（コンテナー起動時に試すエントリーポイント）<br>
&nbsp;&nbsp;&nbsp;&nbsp;├── uwsgi_params (uwsgiパラメータ）<br>
