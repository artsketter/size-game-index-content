"""Combine every games/<folder>/game.csv into one games/index.json.

Each game becomes one object: every CSV field (lower-cased name -> text value),
plus "id" (the folder name) and "files" (the file names in the folder, used to find thumbnails).
Empty creation_time / entry_last_updated fields are filled in from git history.
"""
import csv, json, os, pathlib, subprocess

GAMES = pathlib.Path(os.environ.get('GAMES_DIR', 'games'))
OUT = GAMES / 'index.json'


def git(*args):
    try:
        return subprocess.run(['git', *args], capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return ''


games = []
for d in sorted(p for p in GAMES.iterdir() if p.is_dir() and (p / 'game.csv').exists()):
    g = {}
    with open(d / 'game.csv', encoding='utf-8-sig', newline='') as f:
        for row in csv.reader(f):
            key = row[0].strip().lower() if row else ''
            if key and key != 'field' and len(row) > 1:
                g[key] = row[1].strip()

    # fill the automatic dates from git history when the CSV leaves them empty
    if not g.get('creation_time'):
        added = git('log', '--diff-filter=A', '--format=%as', '--', (d / 'game.csv').as_posix()).splitlines()
        if added:
            g['creation_time'] = added[-1]          # earliest commit that added the file
    if not g.get('entry_last_updated'):
        last = git('log', '-1', '--format=%as', '--', d.as_posix())
        if last:
            g['entry_last_updated'] = last

    g['id'] = d.name
    g['files'] = sorted(x.name for x in d.iterdir() if x.is_file())
    games.append(g)

OUT.write_text(json.dumps(games, ensure_ascii=False, separators=(',', ':')), encoding='utf-8')
print(f'Wrote {OUT} with {len(games)} games')
