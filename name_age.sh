#!/bin/bash
#name = 'Jean-Paul'
#lastname = 'Sartre'
#birth_date = 1905
#death_date = 1980
current_year=$(date +%Y)

read  -p "Enter your name: " first_name
read -p "Enter your lastname: " last_name

read -p "Enter your birth date: " b_date
user_age=$((current_year - b_date))
echo "You are $first_name $last_name"
echo "You are $user_age years old!"

echo "Pick a philosopher:"
echo "1 - Jean-Paul Sartre"
echo "2 - David Hume"
echo "3 - Immanuel Kant"

read -p "Enter your choice (1-3): " selection

if [ "$selection" -eq 1 ]; then
    echo "20. yüzyıl Fransız filozofudur ve varoluşçuluk akımının en önemli temsilcilerindendir. İnsanların özgür olduğunu ve kendi anlamlarını kendilerinin yaratması gerektiğini savunur. “Varoluş özden önce gelir” sözüyle bilinir."
elif [ "$selection" -eq 2 ]; then
    echo "18. yüzyıl İskoç filozofudur. Deneycilik (empirizm) ve şüphecilik akımıyla tanınır. Bilginin deneyimden geldiğini savunmuş ve nedensellik gibi kavramları sorgulamıştır."
elif [ "$selection" -eq 3 ]; then
    echo "Alman Aydınlanma filozofudur. Akılcılık ile deneyciliği birleştirmeye çalışmıştır. Ahlak felsefesinde önemli bir yere sahiptir ve kategorik imperatif (evrensel ahlak yasası) kavramıyla tanınır."
else
    echo "Invalid selection"
fi

read -p "İşlem yapılacak ilk sayıyı girin: " num1
read -p "İşlem yapılacak ikinci sayıyı girin: " num2
echo "\n 1-Toplama \n 2-Çıkartma \n 3-Çarpma \n 4-Bölme"
read -p "Hangi tür işlem yapmak istersiniz: " calc

if [ "$calc" -eq 1 ]; then 
    echo "Toplam: $((num1 + num2))"
elif [ "$calc" -eq 2 ]; then
    echo "Çıkartma sonucu: $((num1 - num2))"
elif [ "$calc" -eq 3 ]; then
    echo "Çarpma sonucu: $((num1 * num2))"
elif [ "$calc" -eq 4 ]; then
    if [ "$num2" -eq 0 ]; then
        echo "Hata: Sıfıra bölme yapılamaz!"
    else
        echo "Bölme sonucu: $((num1 / num2))"
    fi
else
    echo "Geçersiz işlem seçimi"
fi
