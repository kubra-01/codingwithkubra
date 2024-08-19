import random


def tas_kagit_makas_adiniz_soyadiniz():
    print('Taş,Kağıt,Makas Oyununa Hoş Geldiniz!')
    print('Oyun Kuralları: Taş, makası yener. Kağıt, taşı yener. Makas, kağıdı yener')
    print('İlk iki turu kazanan oyunun galibi olur.')


    while True:
        oyun_sayisi = 1
        oyuncu_galibiyeti = 0
        bilgisayar_galibiyeti = 0


        while oyuncu_galibiyeti < 2 and bilgisayar_galibiyeti < 2 :
            print(f'\n{oyun_sayisi}. Oyun:')
            secenekler = ['taş','kağıt','makas']
            oyuncu_secimi = input('taş, kağıt ya da makas seçin:')

            while oyuncu_secimi not in secenekler:
                oyuncu_secimi = input('Geçersiz seçim. Taş,kağıt ya da makas seçin:')

            bilgisayar_secimi = random.choice(secenekler)
            print(f'Bilgisayarın seçimi: {bilgisayar_secimi}')


            if oyuncu_secimi == bilgisayar_secimi:
                print('Beraberlik!')
            elif (oyuncu_secimi == 'taş' and bilgisayar_secimi == 'makas') or \
                 (oyuncu_secimi == 'kağıt' and bilgisayar_secimi == 'taş') or \
                 (oyuncu_secimi == 'makas' and bilgisayar_secimi == 'kağıt') or \
                print('Bu turu kazandınız!'):
                oyuncu_galibiyeti += 1
            else:
                print('Bilgisayar bu turu kazandı!')
                bilgisayar_galibiyeti += 1

                oyun_sayisi += 1
            if oyuncu_galibiyeti == 2:
                print('\nTebrikler! Oyunu kazandınız!')
            else:
                print('\nÜzgünüm, bilgisayar oyunu kazandı.')

            devam_et = input('Başka bir oyun oynamak ister misiniz? (evet/hayır): ')
            bilgisayar_devam = random.choice(['evet','hayır'])
            print(f'Bilgisayarın cevabı: {bilgisayar_devam}')


            if devam_et != 'evet' or bilgisayar_devam != 'evet':
                print('Oyun sona erdi. Tekrar bekleriz!')
                break













