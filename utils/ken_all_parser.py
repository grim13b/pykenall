"""
日本郵便の郵便番号ファイルに所々ある分割されたレコードを連結する
see: https://www.post.japanpost.jp/zipcode/dl/readme.html
"""
import csv
import json
import logging
from typing import Any, List


def parse_ken_all(kenall_file: str) -> List[dict[str, Any]]:
    postal_code = []
    with open(kenall_file, 'r', encoding='ms932') as f:
        reader = csv.reader(f)
        for row in reader:
            # 廃止は飛ばす
            if row[13] == '2':
                continue

            # 一番最初の扱いがキモい
            # 13.一つの郵便番号で二以上の町域を表す場合の表示　（注5）　（「1」は該当、「0」は該当せず）
            if row[12] == '0' and len(postal_code) > 0:
                # 連結が必要なデータ
                last_element = postal_code[-1]
                if last_element['postalcode'] == row[2]:
                    last_element['townkana'] += row[5]
                    last_element['town'] += row[8]
                    continue

            # 連結不要なデータ
            tmp = {
                'jisx0401x0402': row[0],
                'postalcode': row[2],
                'prefkana': row[3],
                'citykana': row[4],
                'townkana': row[5],
                'pref': row[6],
                'city': row[7],
                'town': row[8].replace('以下に掲載がない場合', '')
            }
            postal_code.append(tmp)
    return postal_code


def write_json(path: str, zipcode: List[dict[str, Any]]):
    with open(path, "w") as f:
        json.dump(zipcode, f, ensure_ascii=False, indent=4)


def main():
    ken_all = parse_ken_all("./data/KEN_ALL.CSV")
    write_json("./assets/ken_all.json", ken_all)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(message)s",
        datefmt="%Y/%m/%d %I:%M:%SZ%z",
    )

    logging.info("start")
    main()
    logging.info("finished")

    exit(0)
