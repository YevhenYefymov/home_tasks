#! /bin/bash

# save the keys
SOURCE_KEYS=$(cat source.yaml | grep -v "-" | sed '/^$/d' | cut -d ":" -f 1)

# this array must contain unique keys
KEYS=()

# add keys to array, ignore if the key is already present
IS_KEY_PRESENT=0
for KEY in ${SOURCE_KEYS[@]}
do
	for K in ${KEYS[@]}
	do
		if [ $K == $KEY ]; then
			IS_KEY_PRESENT=1
			break
		fi
	done
	if [ "$IS_KEY_PRESENT" -eq 0 ]; then
		KEYS+=($KEY)
	fi
	IS_KEY_PRESENT=0
done

# save the amount of keys to use later
NO_OF_KEYS=${#KEYS[@]}

#							SECOND COLUMN		ESCAPE '\'	TAG EMPTY VALUE
SOURCE_VALUES=$(cat source.yaml | grep -v "-" | sed '/^$/d' | cut -d ":" -f 2 | sed 's/\\/\\\\/g' | sed 's/^$/EMPTY/g')

RESULT_STRING=$(echo ${KEYS[@]}'\n' | sed 's/ /, /g')

OLD_IFS=$IFS
IFS=$'\n'

# iterate through values, add newline each NO_OF_KEYS value, so that values string matches keys string
i=0
for VAL in ${SOURCE_VALUES[@]}
do
	((i++))
	# remove whitespaces from the start of the string
	VAL=$(echo $VAL | sed 's/^ //g')
	
	# put strings that contain commas in double quotes
	if [ ! -z $(echo $VAL | grep ,) ]; then\
		VAL=$(echo $VAL | sed "s/$VAL/\"$VAL\"/g")
	fi

	if [ $i -eq $NO_OF_KEYS ]; then
		RESULT_STRING+=$VAL
		RESULT_STRING+='\n'
		i=0
	else
		RESULT_STRING+=$VAL', '
	fi
done

# don't forget to get rid of the EMPTY marker
RESULT_STRING=$(echo $RESULT_STRING | sed 's/, EMPTY//g')

# use printf to apply all the newlines
printf "$RESULT_STRING"

# probably unnecessary, as this runs in a subshell...
IFS=$OLD_IFS