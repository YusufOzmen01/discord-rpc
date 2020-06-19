# Kolay Discord Rich Presence

## Açıklama

Kolayca durumunuzu Discord Rich Presence ile güzelleştirebilir, uygulamalar ve oyunlarla entegre ederek kendi özel oyun ve uygulama durumunuzu sorunsuz oluşturabilirsiniz!

## Discord Rich Presence Nedir?

Discord Rich Presence, Discord'daki '... Oynuyor' kısmında, yani oyun oynarken veya Spotify'dan şarkı dinlerken çıkan ve o uygulama/oyun hakkında bilgiler veren (Dinlediğiniz şarkı, kaç dakikadır kullanılıyor, oyunda bulunduğunuz sunucu veya mod gibi) bir yazı. 

<img src="https://i.redd.it/2t89k2v84qf21.png">

## Başlamadan Önce

Orta, belki de giriş düzeyinde bir Python bilgisine ihtiyacınız olacak. Eğer sadece bu template üzerinden yazıları değiştirecekseniz Python bilmenize gerek yok.

### Gereksinimler

* Python 3.8.2
* macOS 10.12 (Sierra) üstü, Linux (tercihen ubuntu veya debian), Windows (7 ve üstü)
* 15 dakika

### Uyarı

* Başlamadan önce sisteminizde Discord kurulu olması gerekmektedir. Ve Linux kullanıcısıysanız ASLA Snap Store veya Uygulama Mağazası'ndan Discord'u kurmayın! Discord'un sitesinden .deb veya .rpm dosyasını indirip Terminal'den kurun. (deb için dpkg -i *.deb*, rpm için rpm -i *.rpm*)

## Gerekli Uygulamaların Kurulumu

### 1- Python

İlk gereken uygulamamız Python. Kullandığımız bu kod, çalıştırılmak için Python Interpeter (yorumlayıcısı) istiyor. Kurmasıise çok kolay!

#### Linux - Ubuntu, Debian

* Terminal'i açın ve aşağıdaki komudu girin.

```
sudo apt install python3
```

* Python artık kuruldu!

#### macOS

* Aşağıda verdiğim linkden dosyayı indirin

```
https://www.python.org/ftp/python/3.8.3/python-3.8.3-macosx10.9.pkg
```

* Kurulum adımlarını tamamlayın.

#### Windows

* Aşağıda verdiğim linkden dosyayı indirin.

```
https://www.python.org/ftp/python/3.8.3/python-3.8.3-amd64.exe
```

* Çalıştırın ve gelen ekrandan alt kısımda 'Add to PATH' seçeneğini açın.

<img src="https://datatofish.com/wp-content/uploads/2018/10/0001_add_Python_to_Path.png">

### 2- Dosyaların indirilmesi

Dosyaları indirmek oldukça kolay. Projenin github sayfasında 'clone or download' butonuna basıp 'download as zip' butonuna basın. İndirilen zip dosyasını ayıklayın.

<img src="https://www.stevejgordon.co.uk/wp-content/uploads/2018/01/CloneOrDownloadGitHub.png">

## Kodların Düzenlenmesi


## Kodları Düzenleme

Kodları tercih ettiğiniz bir editör ile açabilirsiniz. Kodlara girdiğinizde satırlarca kod göreceksiniz ama korkmayın! Bizi sadece ilgilendiren 3 satır.

### Discord App Client ID Alma

Bu projeyi çalıştımak için önce aşağıdaki linke girin

```
https://discord.com/developers/applications
```

Linke girince Discord hesabınızla giriş yapın.

Ardından sağ üstten 'New Application' butonuna basın ve bir isim verin. Ama unutmayın. Bu isim, oynuyor kısmınızdaki uygulama ismi olacak.

Sonra gelen ekrandan 'CLIENT ID' kısmındaki client id'yi kopyalayın. (yaklaşık 18 sayı)

<img src="https://www.howtogeek.com/wp-content/uploads/2018/09/xbot_1.png.pagespeed.gp+jp+jw+pj+ws+js+rj+rp+rw+ri+cp+md.ic.uxaZDGrUCZ.png">

Kopyaladığınız id'yi bir yere not edin.

### Yazıları değiştirme

dc.py dosyasını metin editörüyle açın. Burda bulunan tırnak içindeki 'CLIENT IDNİZ' yazısını silin ve tırnakların arasına client id'nizi girin.

Altta benim durumumda kullandığım metinler mevcut. Burdan 'while True:' kısmının altındaki yerleri silin ve aşağıda verdiğim template'i değiştirerek yapıştırın. (Art arda yazabilirsiniz. Böylece animasyonlu bir şeyler yapabilirsiniz.)

```
rpc_obj.set_activity(util.durum("İLK YAZI", "İKİNCİ YAZI"))
time.sleep(2)
```

Buradaki '2' sayısını istediğiniz süreyle değiştirebilirsiniz.

Şunu not etmeliyim. Python boşluklarla kod öbeklerini tanıdığından bu template'i 'while True:' altına geçtikten sonra bir kez tab basarak (satır başından 4 boşluk fazla) yazın. Burdan "İLK YAZI" ve "İKİNCİ YAZI" kısmını değiştirebilirsiniz. Ama unutmayın, tırnak içinde olacak yoksa çalışmaz.

## Çalıştırma

Her şeyi hallettikten sonra sıra geldi denemeye. Discord hesabınızda oynadığınız oyunun durum olarak gösterilmesini sağlayan ayarın açık olduğundan emin olun. Ardından dc.py dosyasını Python ile açın ve oalia! Yazılarınızın kusursuz gelmiş olması lazım.

# Yapımcılar

* Yusuf Çınar Özmen (Türkçelendirme ve basit template) : https://www.github.com/yusufozmen01
* Nivesh Birangal (RPC.PY Yapımcısı) : https://github.com/niveshbirangal/

# Lisanslama

Bu yazılım, GNU lisanslama tipinde lisanslanmıştır. Tamamen açık kaynaklı olup değiştirilmesi veya satılması serbesttir.