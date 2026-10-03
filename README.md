# Size Game Index Content Info

## Adding a new game
Create a new folder in `/games/` containing `game.csv` and up to 5 thumbnails.

## game.csv

Two columns, one field per row: `field,value`. Use `|` to separate multiple values (tags, links, languages). 

Dates are in the format: `YYYY-MM-DD`. 

Checkboxes: `yes` / `no`. 

Ratings: `art_rating`, `mechanic_rating`, `animation_rating` are 1–5; `size_focus` is 1–3.

Currently included fields: title, original_title, summary, narrative, time_to_complete, tags, interactions, development_status, pricing_model, game_engine, art_rating, main_art_style, mechanic_rating, mechanics_description, animation_rating, size_focus, game_links, walkthrough (file name inside the game folder), creator_link, forum_link, authors, last_updated, latest_content_update, release_date, languages, filtered, contains_ai, entry_last_updated, creation_time, thumbnails.

Thumbnails: .jpg/.png/.webp work. The first one listed is the gallery thumbnail.

## GameIndexEditor.exe

Batch csv processor with a variety of tools to manage data for all games in the collection at the same time, with a cached list of tag types for easy access.
Contains webp compressor, search/replace and tag moving function.
Changes logged to `Changes.txt`, simplified changes logged to `Changelog.txt` for future commit descriptions.