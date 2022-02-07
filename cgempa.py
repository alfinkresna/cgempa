#!/usr/bin/env python3
import json
import requests as rq

req = rq.get ("https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json")
data = json.loads(req.text)

Bujur = data["Infogempa"]["gempa"]["Bujur"]
Koordinat = data["Infogempa"]["gempa"]["Coordinates"]
HariWaktu = data["Infogempa"]["gempa"]["DateTime"]
Jam = data["Infogempa"]["gempa"]["Jam"]
Kedalaman = data["Infogempa"]["gempa"]["Kedalaman"]
Lintang = data["Infogempa"]["gempa"]["Lintang"]
Magnitude = data["Infogempa"]["gempa"]["Magnitude"]
Dirasakan = data["Infogempa"]["gempa"]["Dirasakan"]
Potensi = data["Infogempa"]["gempa"]["Potensi"]
Tanggal = data["Infogempa"]["gempa"]["Tanggal"]
Wilayah = data["Infogempa"]["gempa"]["Wilayah"]

print(f"""
   ___
  / __\__ _  ___ _ __ ___  _ __   __ _
 / /  / _` |/ _ \ '_ ` _ \| '_ \ / _` |
/ /__| (_| |  __/ | | | | | |_) | (_| |
\____/\__, |\___|_| |_| |_| .__/ \__,_|
      |___/               |_|

     Cek Informasi Gempa Terkini

          Created by Alfin


>> Info Gempa <<

> Tanggal : {Tanggal}

> Jam : {Jam}

> Hari/Waktu : {HariWaktu}

> Koordinat : {Koordinat}

> Lintang : {Lintang}

> Bujur : {Bujur}

> Magnitude : {Magnitude}

> Kedalaman : {Kedalaman}

> Wilayah : {Wilayah}

> Potensi : {Potensi}

> Dirasakan : {Dirasakan}

""")

print()