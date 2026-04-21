#!/bin/bash

echo "X sayisini (0 veya 1) giriniz:"
read x

echo "Y sayisini (0 veya 1) giriniz:"
read y

echo "Operatoru secin: 1=AND, 2=OR, 3=NOT"
read operator

if [ "$operator" -eq 1 ]; then
    # AND
    if [ "$x" -eq 1 ] && [ "$y" -eq 1 ]; then
        sonuc=1
    else
        sonuc=0
    fi
    echo "Sonuc (AND): $sonuc"

elif [ "$operator" -eq 2 ]; then
    # OR
    if [ "$x" -eq 1 ] || [ "$y" -eq 1 ]; then
        sonuc=1
    else
        sonuc=0
    fi
    echo "Sonuc (OR): $sonuc"

elif [ "$operator" -eq 3 ]; then
    echo "NOT alınacak değeri seçin:"
    echo "1 = X"
    echo "2 = Y"
    echo "3 = AND(X,Y)"
    echo "4 = OR(X,Y)"
    
    echo -n "Secim: "
    read sec

    if [ "$sec" -eq 1 ]; then
        echo "Sonuc (NOT X): $(( !x ))"

    elif [ "$sec" -eq 2 ]; then
        echo "Sonuc (NOT Y): $(( !y ))"

    elif [ "$sec" -eq 3 ]; then
        echo "Sonuc (NOT AND): $(( !(x && y) ))"

    elif [ "$sec" -eq 4 ]; then
        echo "Sonuc (NOT OR): $(( !(x || y) ))"

    else
        echo "Doğru Input gir maymun"
    fi

else
    echo "Gecersiz operator!"
fi
