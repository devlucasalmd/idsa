#!/bin/bash

ARQ="/tmp/page.hits"

# Obtém o valor do campo BUSCA do formulário
SEARCH_TERM=$(echo "$QUERY_STRING" | sed -n 's/^.*BUSCA=\([^&]*\).*$/\1/p')

# Verifica se o parâmetro 'zerar' foi passado na string de consulta
ZERAR=$(echo "$QUERY_STRING" | grep -o 'zerar')

# Verifica se a página foi recarregada sem a ação de zerar
if [ -z "$ZERAR" ] && [ -z "$SEARCH_TERM" ]; then
    # Limpar o resultado na tela (opcionalmente, você pode resetar a contagem aqui se desejar)
    OUTPUT=""
    echo "0" > "$ARQ"
fi

# Lógica para zerar a contagem
if [ -n "$ZERAR" ]; then
    echo "0" > "$ARQ"
fi

# Chama o segundo script passando o valor de BUSCA como argumento
OUTPUT=$(bash segundo_script.sh "$SEARCH_TERM")

if [ -n "$SEARCH_TERM" ]; then
   # Incrementa o contador de visualizações
   n=$(($(cat "$ARQ" 2>/dev/null)+1))
   echo "$n">"$ARQ"
fi

# Início da resposta HTTP
echo "Content-type: text/html"
echo

# Cabeçalho HTML
cat <<EOF
<html>
<head>
<title>Man Page</title>
<!-- Adiciona script JavaScript para limpar a string de consulta da URL -->
<script>
    if (window.history.replaceState) {
        window.history.replaceState({}, document.title, window.location.pathname);
    }
</script>
</head>
<body>
<div id="conteudo" style="float:left; width:350px; height:auto;">
<center><h1>Online system's manual pager</h1></center>
<form name='form_nome' method='GET' action='primeiro.cgi'>
<label>P&aacutegina para busca: </label>
<input type="text" size="30" name="BUSCA" value="$SEARCH_TERM" />
<input type="submit" value="Enviar" />
</form>

<!-- Adiciona um botão para zerar a contagem -->
<form name='form_zerar' method='GET' action='primeiro.cgi'>
<input type="hidden" name="zerar" value="1" />
<input type="submit" value="Zerar Contagem" />
</form>
<br>
EOF

# Verifica se a variável não está vazia
if [ -n "$OUTPUT" ]; then
   echo "<hr />"
   echo "<p>Esta página já foi visualizada: $n vezes</p>"
   echo "<hr />"
   echo "<p>Resultado para: $SEARCH_TERM</p>"
   echo "<textarea cols=\"100\" rows=\"30\" readonly=\"readonly\" style=\"resize:none;\">"
   echo "$OUTPUT"
   echo "</textarea>"
fi

# Fim do corpo HTML
echo "</div></body></html>"

