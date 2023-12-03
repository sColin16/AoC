redRegex='[0-9]+ red'
greenRegex='[0-9]+ green'
blueRegex='[0-9]+ blue'

gameNum=1
ans1=0
ans2=0

while read line; do
    redMax=$(echo $line | grep -oE "$redRegex" | awk '{print $1}' - | sort -n | tail -1)
    greenMax=$(echo $line | grep -oE "$greenRegex" | awk '{print $1}' - | sort -n | tail -1)
    blueMax=$(echo $line | grep -oE "$blueRegex" | awk '{print $1}' - | sort -n | tail -1)

    power=$((redMax * greenMax * blueMax))
    ans2=$((ans2 + power))

    if (( $redMax <= 12 && $greenMax <= 13 && $blueMax <= 14 ))
    then
        ans1=$((ans1 + gameNum))
    fi

    gameNum=$((gameNum + 1))
done

echo "Part 1: $ans1"
echo "Part 2: $ans2"

