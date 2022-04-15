# pykenall

## 使い方

1. ./data に KEN_ALL.CSV を置く
2. `python utils/ken_all_parser.py` を実行して ./assets/ken_all.json を作る
3. `docker-compose up --build` で起動する
4. 任意の http クライアントで `GET localhost:8000/kenall/{postal_code}` を実行する
    - `postal_code` は前方一致です