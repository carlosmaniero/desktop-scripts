#!/usr/bin/env bash

int_atual=0
interrupcao[0]="Como pano de engraxate!"
interrupcao[1]="Como dente de alicate!"
interrupcao[2]="Como sinos de chocolate!"
interrupcao[3]="Como caroço de abacate!"
interrupcao[4]="Já me deixou derretida!"

control_c() {
    espeak -v pt "${interrupcao[${int_atual}]}"

    if [ "$int_atual" -eq 4 ]; then
        espeak -v pt "Ele pensou que você não sabia rimar"
        exit
    fi

    int_atual=$((int_atual+1))
}

trap control_c SIGINT

canta() {
    while true;
    do
        espeak -v pt "Ma mãe querida. Meu coração por ti bate como"
    done 
}

# espeak -v pt "Mamãezinha, mamãezinha, viemos alegremente para cantar em seu louvor e felicitá-lá sempre!"
# espeak -v pt "Obrigado! Com muito prazer para todos vocês: Mamãe Querida e Adorada."



canta
