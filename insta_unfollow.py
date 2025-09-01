from instagrapi import Client
import time
from getpass import getpass  # Terminalde şifreyi gizli almak için

# Kullanıcıdan giriş bilgilerini al
username = input("Instagram kullanıcı adınızı girin: ")
password = getpass("Instagram şifrenizi girin: ")

# Client oluştur ve giriş yap
cl = Client()
try:
    cl.login(username, password)
    print("✅ Instagram'a giriş başarılı!")
except Exception as e:
    print(f"⚠ Giriş başarısız: {e}")
    exit()

# Takip edilen kullanıcıları al
try:
    following = cl.user_following(cl.user_id)
    print(f"Takip ettiğiniz kişi sayısı: {len(following)}")
except Exception as e:
    print(f"⚠ Takip listesi alınamadı: {e}")
    exit()

# Takipten çıkma işlemi
for user_id, user_data in following.items():
    try:
        cl.user_unfollow(user_id)
        print(f"❌ Unfollow edildi: {user_data.username}")
        time.sleep(2)  # Instagram ban riskini azaltmak için
    except Exception as e:
        print(f"⚠ Hata oluştu: {e}")

print("✅ Tüm takipten çıkma işlemi tamamlandı!")
input("Çıkmak için Enter'a basın...")
