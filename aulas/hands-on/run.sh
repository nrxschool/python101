#!/bin/bash

# Loop pelas pastas que seguem o padrão
for pasta in aula*-hands-on; do
    # Extrai o número da aula do nome da pasta
    numero=$(echo $pasta | sed 's/aula\([0-9]*\)-hands-on/\1/')
    
    # Renomeia a pasta
    mv "$pasta" "aula$numero"
done
