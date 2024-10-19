#!/bin/bash

outputfile="/home/back_api/custom-list"
tempfile="/home/back_api/temp-customlist"

function sort_and_insert()
{

	while read line; do
		domains=$(echo $line | cut -d " " -f 1 )
		types=$(echo $line | cut -d " " -f 3 )
        address=$(echo $line | cut -d " " -f 4 )
		echo "$domains,$types,$address" >> $tempfile
	done < $outputfile

}

if [ ! -e "$outputfile" ]; then 
	touch $outputfile
else
	rm -f $outputfile
	touch $outputfile
fi

if [ ! -e "$tempfile" ]; then
	touch $tempfile
else
	rm -f $tempfile
	touch $tempfile
fi

cat /etc/bind/db.custom.dns | awk '$2=="IN" && $3=="A" {print}' > $outputfile

sort_and_insert 

cat $tempfile

rm $tempfile
rm $outputfile