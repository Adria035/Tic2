#condicional, exercici 5

numero3=$ ((RANDOM%36))
numero4=$ ((RANDOM%3))
numero5=$ ((Random%37))
echo "Digues un numero1"
read numero1
echo "Digues un numero2"
read numero2

    if test $numero1 -gt $numero2
        then
        echo "El numero 1 és més gran"
fi

echo "La multiplicació del $numero1 per 2 resultat"$((numero1*2))""
    if test $numero1 -gt $numero2 
    then 
echo "El $numero1 és més gran que el $numero2"
fi

echo "El $numero3 és un numero random"

if test $numero2 -gt $numero3
then
echo "El $numero2 és més gran que el $numero3"
fi

echo "$numero4 és un numero random"
echo "$numero5 és un numero ranom "
    if test $numero4 -gt $numero5
    then
echo "El $numero5 és més gran que el $numero$"
fi
