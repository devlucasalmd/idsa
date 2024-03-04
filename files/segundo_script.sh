#!/bin/bash

# Obtém o argumento passado (termo de busca)
SEARCH_TERM=$1

# Executa o comando e retorna o resultado
if [ -n "$SEARCH_TERM" ]; then
    man "$SEARCH_TERM"
fi

