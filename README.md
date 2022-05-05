# TCG To Archidekt Wrapper
The TCG Scanner app for mobiles does a great job at scanning cards but if you are using Archidekt for card storage importing your collection can be a bit cumbersome, specially for promos or different printers.

## Usage
1. Scan your cards with the TCG App, make sure the scan is accurate
2. Export the csv to your computer (use Gdrive, dropbox, etc)
3. Copy the csv to the same folder where the wrapper will run, the default name is `TCGplayer.csv`
4. Run the command 
``` 
python parcer.py
```
5. Use the file `archidekt.csv` to upload to archidekt.com[archidekt.com]. Make sure you use the `File Upload` option.

![image](https://user-images.githubusercontent.com/46324369/167026928-c04255a9-9e1e-4efe-9361-765977976e43.png)
