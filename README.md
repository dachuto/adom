#ADOM save helpers
Play softcore with:
```
cp --backup ~/.adom.data/savedg/PIO.svg
cp -n ./PIO.svg ~/.adom.data/savedg/PIO.svg
```
Utility `touch` automates tedious process of checking random future. It runs in text mode. General pattern goes like this:
- load backed save
- perform actions
- save
- backup
- load
- quit
- copy memorial and info to folder with backup
- repeat any number of times

Then one can just go over generated saves and extract information from text files `grep -E 'Spell' -A 5  /tmp/adom/save*/pio.flg`.
Artifacts are pretty important so we have a special program for that `python list_artifacts.py /tmp/adom/save*/pio.flg -n 1 -e -l`.
**Troubleshooting**
Colored menus can mess with expect. You can turn them off in settings.
This utility sometimes encounters unexpected message and halts. I do not think it is worth the effort to make it bulletproof.

Running on linux depends on a few libraries and sometimes you have to link with an old version. Just see `adom_run` file.

