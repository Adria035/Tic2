
read n
a=0
n1=1
suma=0

for (( i=0; i<n; i++ ))
do  
    for (( j=0; j<n; j++ ))
    do  
        printf $a
        let suma=$suma+$n1
    done
    echo $suma
done
