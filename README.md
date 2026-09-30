# Size Game Index Content Info

## Adding a new game
Create a new folder in `/games/` containing `game.csv` and up to 5 thumbnails.

## game.csv

Two columns, one field per row: `field,value`. Use `|` to separate multiple values (tags, links, languages, author tags). 

Dates are in the format: `YYYY-MM-DD`. 

Checkboxes: `yes` / `no`. 

Ratings: `art\_rating`, `mechanic\_rating`, `animation\_rating` are 1–5; `size\_focus` is 1–3.

Currently included fields: title, original\_title, summary, narrative, time\_to\_complete, tags, development\_status, pricing\_model, game\_engine, art\_rating, main\_art\_style, mechanic\_rating, mechanics\_description, animation\_rating, size\_focus, game\_links, walkthrough (file name inside the game folder), creator\_link, forum\_link, authors, author\_tags, last\_updated, latest\_content\_update, release\_date, languages, recommended, filtered, contains\_ai, entry\_last\_updated, creation\_time, thumbnails (optional).

Thumbnails: .jpg/.png/.webp work. The first one listed is the gallery thumbnail.

## md2csv.exe

Used to convert notion markdown files from the size archive into .csv format with the correct formatting. Drag-and-drop any number of markdown files onto the executable and they will be deposited into appropriately named folders and formatted directly for use on the site.