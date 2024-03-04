#!/bin/bash

#ls
#pwd
#date

#echo "Hello World"

#MINHA_VAR=1
#echo $MINHA_VAR

echo "Digite seu nome: "
read NOME
#NOME=`echo $NOME | tr a-z A-Z
NOME=`echo $NOME | tr [:lower:] [:upper:]`
#echo "Boa noite $NOME"

#if COMANDOS; then COMANDOS; [ elif COMANDOS; then COMANDOS; ]... [ else COMANDOS; ] fi

#if (($NOME="Jose")) then
#if [ $NOME == "JOSE" ]; then	
#    echo -e "\nBoa noite $NOME";
#else
#    echo -e "\nNão falo com voce $NOME"
#fi

#for(exp1; exp2; exp3);


#while: while COMMANDS; do COMMANDS-2; done
if [ $NOME == "JOSE" ]; then	
    I=0
#   while(( $I<3 )); do
    while [ $I -lt 3 ]; do
#        ((I=$I+1))
#        I=`expr $I + 1`
        I=$(expr $I + 1)
#	let "I=$I+1"
	echo -e "\n$I - Boa noite $NOME";
	sleep 1
#	(($I++))
    done
else
    echo -e "\nNão falo com voce $NOME"
fi


