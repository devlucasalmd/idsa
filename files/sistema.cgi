#!/bin/bash

cat <<EOF
Content-type: text/html

<html>
<head>
<title>Sistema</title>
</head>
<body>
<h1>Informacao do Sistema</h1>
EOF

echo "`uname -a`"
echo "</br>"
echo "<h3>Data e Horario: "`date`"</h3>"
#echo "`date`"
echo "</br>"
echo "`uptime`"
echo "</br>"
echo "`free -h`"
echo "</br>"
echo -e "<textarea cols=\"100\" rows=\"30\" readonly=\"readonly\" style=\"resize:none;\">"
man ls
echo -e "</textarea>"
echo "</br>"
echo "</body>"
echo "</html>"
