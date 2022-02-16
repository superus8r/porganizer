# porganizer
To make taking daily markdown notes easier and more organized, I created a simple script to create note files with a date prefix!
It also provides simple customization options to define `To-Do`s in a note and automatically copy them in next day notes.

## USAGE
```
python3 porganizer.py
```
    
Running this will create a file with the current date's prefix and a default suffix.

The suffix can be changed by simply updating the following paramter:

```
defaultSuffix = 'DailyLog'
```

Any note that comes after `todoId` will be considered as `To-Do`s for the next note. the `todoId` can also be simply modified:

```
todoId = '--------'
```

Add `porganizer.py` to your path. This way it can be called from any directory to create organized notes!
```
export path/to/porganizer.py
```

<hr/>

## Organizing Folders & More

Assuming `porganizer.py` is in the path, it can be simply called from your notes folder. 

For making notes even cleaner, a simple script in your notes folder can also call `porganizer.py` for you:
```
#!/bin/bash

year=$(date +"%Y")
month_number=$(date +"%m")
month_name=$(date +"%B" | tr a-z A-Z) # find the month name and make it all upper case
month="${month_number}_${month_name}"

mkdir -p $year
cd $year
mkdir -p $month
cd $month
porganizer.py
```
The above example organizes your porganizer-logs in a `YEAR/MONTH` order and creates the necessary folders.
Once the folder exists, it runs the `porganizer` inside the correct folder. 

Have fun porganizing! 😊