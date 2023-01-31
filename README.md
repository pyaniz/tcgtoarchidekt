# TCG To Archidekt Wrapper
The TCG Scanner app for mobiles does a great job at scanning cards but if you are using Archidekt for card storage importing your collection can be a bit cumbersome, specially for promos or different printers. This wrapper will cycle through the export from the TCG app and will create a new csv that contains the `Scryfall ID` number to import.

## Usage
1. Download this script
```
git pull https://github.com/pyaniz/tcgtoarchidekt.git
```
2. Scan your cards with the TCG App, make sure the scan is accurate
3. Export the csv to your computer (use Gdrive, dropbox, etc)
4. Copy the csv to the same folder where the wrapper will run, the default name is `TCGplayer.csv`
5. Run the command 
``` 
python parcer.py
```
6. Use the file `archidekt.csv` to upload to archidekt.com[archidekt.com]. Make sure you use the `File Upload` option.
7. Make sure you change the last option from `Set Name` to `Scryfall ID`
  **Note:** if you don't set this option the importer will work but Archidekt will try to guess what printing you have and you will likely end up with the wrong printing in the collection.
  
![image](https://user-images.githubusercontent.com/46324369/167026928-c04255a9-9e1e-4efe-9361-765977976e43.png)

## Commands
| Description | Flag | Command | Default |
| ----------- | ---- | ------- | ------- |
| Detail cards being processed | -l | --log | *no default* |
| Choose filename to READ, it will read the default if no flag used | -f | --filename | TCGplayer.csv |
| Choose filename to WRITE, it will write to default if no flag used | -w | --write|archidekt.csv |

## Error handling
Any line that cannot be converted will be written to an errorfile and will **not** be included in the exported file.
