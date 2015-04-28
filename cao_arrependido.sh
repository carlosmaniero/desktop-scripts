#!/usr/bin/env bash

control_c() {
    espeak -v pt "Muito bem, Chaves, muito bem!"
    sleep 1
    espeak -v pt "O verso é repetido 44 vezes"
    espeak -v pt "Volta o cão arreee eee eee"
    exit
}

trap control_c SIGINT

for i in {1..44} 
do
espeak -v pt "Volta o cão arrependido"
espeak -v pt "Com suas orelhas tão fartas"
espeak -v pt "Com seu osso roído"
espeak -v pt "E com o rabo entre as patas"
done
