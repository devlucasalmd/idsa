#!/bin/bash

echo "Content-type: text/html"
echo

cat <<EOF
<html>
<head>
<title>Verificar Rede</title>
<!-- Adiciona script JavaScript para limpar a string de consulta da URL -->
<script>
    if (window.history.replaceState) {
        window.history.replaceState({}, document.title, window.location.pathname);
    }
</script>
</head>
<body>
<div id="conteudo" style="float:left; width:350px; height:auto;">
<center><h2>Verificar Rede com o comando Ping</h2></center>

EOF

if [ "$QUERY_STRING" ]; then
    echo "$QUERY_STRING"

    # Extrair o valor do parâmetro 'host'
    host=$(grep -oP 'host=\K[^&]+' <<< "$QUERY_STRING")
    # O parâmetro -o faz com que o grep imprima apenas as partes correspondentes do texto.
    # -P habilita as expressões regulares Perl.
    # O que vem antes de \K não será incluído no resultado final. 
    # [^&]+ corresponde a um ou mais caracteres que não sejam '&'. Isso captura o valor real do parâmetro 'host'.

    if [ -n "$host" ]; then
        echo "<br>"
        echo "<pre>"
        ping -c5 "$host"
        echo "</pre>"
        echo "Fim."
    else
        echo "<br>"
        echo "<b>Parâmetro 'host' não encontrado ou vazio.</b>"
    fi
else
    echo "
    <form method=\"GET\" action=\"idsa.cgi\">
    <b>Entre com o nome ou IP do host para o ping:</b>
    <input size=40 name=host value=\"\">
    <input type=\"submit\" value=\"Enviar\">
    </form>"
fi

echo "</body>"
echo "</html>"

