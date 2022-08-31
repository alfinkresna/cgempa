#!/usr/bin/env python3
import json as js
import requests as rq
from src import conn


class getConnection:
    def __init__(self, connect):
        self.connect = connect

    def __str__(self):
        return f"{self.connect}"


def main():

    connection = getConnection(conn.connect)
    get = rq.get(connection.__str__())
    data = js.loads(get.text)

    res = {
        "Bujur": data["Infogempa"]["gempa"]["Bujur"],
        "Koordinat": data["Infogempa"]["gempa"]["Coordinates"],
        "HariWaktu": data["Infogempa"]["gempa"]["DateTime"],
        "Jam": data["Infogempa"]["gempa"]["Jam"],
        "Kedalaman": data["Infogempa"]["gempa"]["Kedalaman"],
        "Lintang": data["Infogempa"]["gempa"]["Lintang"],
        "Magnitude": data["Infogempa"]["gempa"]["Magnitude"],
        "Dirasakan": data["Infogempa"]["gempa"]["Dirasakan"],
        "Potensi": data["Infogempa"]["gempa"]["Potensi"],
        "Tanggal": data["Infogempa"]["gempa"]["Tanggal"],
        "Wilayah": data["Infogempa"]["gempa"]["Wilayah"],
    }

    print(
        f"""
   ___
  / __\__ _  ___ _ __ ___  _ __   __ _
 / /  / _` |/ _ \ '_ ` _ \| '_ \ / _` |
/ /__| (_| |  __/ | | | | | |_) | (_| |
\____/\__, |\___|_| |_| |_| .__/ \__,_|
      |___/               |_|

     Cek Informasi Gempa Terkini

          Created by Alfin


>> Info Gempa <<

> Tanggal : {res["Tanggal"]}

> Jam : {res["Jam"]}

> Hari/Waktu : {res["HariWaktu"]}

> Koordinat : {res["Koordinat"]}

> Lintang : {res["Lintang"]}

> Bujur : {res["Bujur"]}

> Magnitude : {res["Magnitude"]}

> Kedalaman : {res["Kedalaman"]}

> Wilayah : {res["Wilayah"]}

> Potensi : {res["Potensi"]}

> Dirasakan : {res["Dirasakan"]}

"""
    )


if __name__ == "__main__":
    main()
