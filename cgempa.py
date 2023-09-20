from system.banner import banner
from requests import get
from fake_useragent import UserAgent
from requests import exceptions
from json import load, loads
from os import system


class CekGempa:
	
	def __init__(self):
		self.user_agent = UserAgent()
		self.data = self.load_data()
		
	def load_data(self):
		try:
			with open('system/connect.json', 'r') as f:
				connect = load(f)
			return connect
		except FileNotFoundError:
			print("\n\033[1;31m[!] File 'connect.json' tidak ditemukan [!]\033[0m")
			return None
		
	def cek_gempa_terbaru(self):
		system("clear")
		print("\n\t\tGempa Terbaru\n")
		print("=" * 50)
		try:
			response = get(self.data["gempa terbaru"], headers = {"User-Agent" : self.user_agent.random}).text
			result = loads(response)
		except exceptions.ConnectionError:
			print("\n\033[1;31m[!] Kesalahan Koneksi [!]\033[0m\n")
			result = None
		try:
			print("\n=> Tanggal : %s" % result["Infogempa"]["gempa"]["Tanggal"])
			print("\n=> Jam : %s" % result["Infogempa"]["gempa"]["Jam"])
			print("\n=> Koordinat : %s" % result["Infogempa"]["gempa"]["Coordinates"])
			print("\n=> Magnitudo : %s" % result["Infogempa"]["gempa"]["Magnitude"])
			print("\n=> Kedalaman : %s" % result["Infogempa"]["gempa"]["Kedalaman"])
			print("\n=> Wilayah : %s" % result["Infogempa"]["gempa"]["Wilayah"])
			print("\n=> Potensi : %s\n" % result["Infogempa"]["gempa"]["Potensi"])
			print("=> Dirasakan : %s\n" % result["Infogempa"]["gempa"]["Dirasakan"])
		except TypeError:
			return None
		
	def cek_gempa_terkini(self):
		system("clear")
		print("\n\t\tGempa Terkini\n")
		try:
			response = get(self.data["gempa terkini"], headers = {"User-Agent" : self.user_agent.random}).text
			result = loads(response)
		except exceptions.ConnectionError:
			print("\033[1;31m[!] Kesalahan Koneksi [!]\033[0m\n")
			result = None
		try:
			for items in result["Infogempa"]["gempa"]:
				print("=" * 50)
				print("\n=> Tanggal : %s" % items["Tanggal"])
				print("\n=> Jam : %s" % items["Jam"])
				print("\n=> Koordinat : %s" % items["Coordinates"])
				print("\n=> Magnitudo : %s" % items["Magnitude"])
				print("\n=> Wilayah : %s" % items["Wilayah"])
				print("\n=> Potensi : %s\n" % items["Potensi"])
		except TypeError:
			   return None
						
	def cek_gempa_dirasakan(self):
		system("clear")
		print("\n\t\tGempa Dirasakan\n")
		try:
			response = get(self.data["gempa dirasakan"], headers = {"User-Agent" : self.user_agent.random}).text
			result = loads(response)
		except exceptions.ConnectionError:
			print("\033[1;31m[!] Kesalahan Koneksi [!]\033[0m\n")
			result = None
		try:
			for items in result["Infogempa"]["gempa"]:
				print("=" * 50)
				print("\n=> Tanggal : %s" % items["Tanggal"])
				print("\n=> Jam : %s" % items["Jam"])
				print("\n=> Koordinat : %s" % items["Coordinates"])
				print("\n=> Magnitudo : %s" % items["Magnitude"])
				print("\n=> Wilayah : %s" % items["Wilayah"])
				print("\n=> Dirasakan : %s\n" % items["Dirasakan"])
		except TypeError:
			return None


def main():
	while 1:
		print(banner)
		print("\n{1} Cek Gempa Terbaru")
		print("\n{2} Cek Gempa Terkini")
		print("\n{3} Cek Gempa Dirasakan")
		print("\n{0} Keluar Program")
		cek_gempa = CekGempa()
		try:
			choice = int(input("\n{+} Pilih Menu 0-3 : "))
		except ValueError:
			print("\n\033[1;31m[!] Masukkan hanya angka 0-3 [!]\n\033[0m")
			continue
		if choice == 1:
			cek_gempa.cek_gempa_terbaru()
		elif choice == 2:
			cek_gempa.cek_gempa_terkini()
		elif choice == 3:
			cek_gempa.cek_gempa_dirasakan()
		elif choice == 0:
			exit("\n\033[1;31m[!] K e l u a r  P r o g r a m [!]\033[0m")
		else:
			print("\n[!] Pilih 1-2")
			continue
	
if __name__ == '__main__' :
	main()
