#!/bin/bash

echo "content-type: text/html"
echo "<html> <head> <title>Contador</title> </head>"
echo "<body>"

ARQ="/tmp/page.hits"

n="$(cat $ARQ 2> /dev/null)" || n=0
echo $((n=n+1)) > "$ARQ"

echo "
<h1>Esta pagina ja foi visualizada: $n vezes</h1>
<br>

</body>
</html>"
