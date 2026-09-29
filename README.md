# \# Size Game Index

# 

# \## Adding a new game

# 1\. Create a new folder in `/games/` containing `game.csv` and up to 5 thumbnails.

# 2\. Run `rebuild\_manifest.bat` to regenerate the folder manifest.

# 

# \## game.csv

# Two columns, one field per row: `field,value`. Use `|` to separate multiple values (tags, links, languages, author tags). 

# Dates are in the format: `YYYY-MM-DD`. 

# Checkboxes: `yes` / `no`. 

# Ratings: `art\_rating`, `mechanic\_rating`, `animation\_rating` are 1–5; `size\_focus` is 1–3.

# 

# Currently included fields: title, original\_title, summary, narrative, time\_to\_complete, tags, development\_status, pricing\_model, game\_engine, art\_rating, main\_art\_style, mechanic\_rating, mechanics\_description, animation\_rating, size\_focus, game\_links, walkthrough (file name inside the game folder), creator\_link, forum\_link, authors, author\_tags, last\_updated, latest\_content\_update, release\_date, languages, recommended, filtered, contains\_ai, entry\_last\_updated, creation\_time, thumbnails (optional).

# 

# Thumbnails: .jpg/.png/.webp work. The first one listed is the gallery thumbnail.

# 

# \## Notes

# \- Entries with `filtered = yes` are hidden unless “Show filtered entries” is enabled.

# \- `entry\_last\_updated` and `creation\_time` are read from the CSV; update them when you edit or add an entry.

# \- Cookies: `filters` (tag filters) and `played` (played-before list).

# \- All styling lives in `css/style.css`.

