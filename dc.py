import rpc
import time
import os
import util

util = util.Util()

client_id = "723384936165408839"#Your application's client ID as a string. (This isn't a real client ID)
rpc_obj = rpc.DiscordIpcClient.for_platform(client_id) #Send the client ID to the rpc module
print("Bağlantı başarılı.")

while True:
    rpc_obj.set_activity(util.durum("Adım : Yusuf Çınar", "Soyadım : Özmen"))
    time.sleep(2)
    rpc_obj.set_activity(util.durum("---Eğitim Durumum---", "9.Sınıf"))
    time.sleep(2)
    rpc_obj.set_activity(util.durum("---Bildiğim Diller---", "Java, C#, JavaScript, Python"))
    time.sleep(2)
    rpc_obj.set_activity(util.durum("---Oynadığım Oyunlar---", "CS:GO (Nova3) / Minecraft"))
    time.sleep(2)
    rpc_obj.set_activity(util.durum("---Github Sayfam---", "https://github.com/yusufozmen01"))
    time.sleep(2)
    rpc_obj.set_activity(util.durum("İşletim Sistemi: Ubuntu 20.04 LTS", "Kernel : 5.4.0-37-generic"))
    time.sleep(2)
    rpc_obj.set_activity(util.durum("Intel Core 2 Duo E8400 @ 3Ghz", "4GB DDR3 RAM RV770 120GB SSD"))
    time.sleep(2)