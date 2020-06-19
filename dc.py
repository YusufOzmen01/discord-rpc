import rpc
import time

client_id = '723384936165408839' #Your application's client ID as a string. (This isn't a real client ID)
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id) #Send the client ID to the rpc module
print("Bağlantı başarılı.")

while True:
    activity1 = {
            "state": "İşletim Sistemi: Ubuntu 20.04 LTS",
            "details": "Kernel : 5.4.0-37-generic",
        }
    activity2 = {
	   "state": "Intel Core 2 Duo E8400 @ 3Ghz",
	   "details": "4GB DDR3 RAM RV770 120GB SSD"
	}
    activity3 = {
            "state": "Soyadım : Özmen",
            "details": "Adım : Yusuf Çınar",
        }
    activity4 = {
	   "state": "Java, C#, Python, Javascript",
	   "details": "---Bildiğim Diller---"
	}
    activity5 = {
	   "state": "Ortaokul Mezunu Lise'ye Giriş",
	   "details": "---Eğitim Durumum----"
	}
    activity6 = {
	   "state": "CS:GO / Minecraft / Indie Games",
	   "details": "---Oynadığım Oyunlar-"
	}
    activity7 = {
	   "state": "https://github.com/yusufozmen01",
	   "details": "---Github Sayfam-----"
	}
    
    rpc_obj.set_activity(activity3)
    time.sleep(5)
    rpc_obj.set_activity(activity5)
    time.sleep(5)
    rpc_obj.set_activity(activity4)
    time.sleep(5)
    rpc_obj.set_activity(activity6)
    time.sleep(5)
    rpc_obj.set_activity(activity7)
    time.sleep(5)
    rpc_obj.set_activity(activity1)
    time.sleep(5)
    rpc_obj.set_activity(activity2)
    time.sleep(5)