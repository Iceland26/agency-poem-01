# Active Voice — Agency Poem Entry

A deterministic Python 3 program (standard library only) that writes *"Active Voice"*, an 18-line free-verse poem about human and artificial agency, to `entry.txt`.

The poem traces the shift from physical labor—a stiff brass key, a sulfur match, soot on the knuckles—to a servant built of language that lifts the latch and lights the grate, turning on the realization that handing over the blister never hands over the hunger that refused the dark.

## Usage

Run `main.py` with `MAKEFUN_OUTPUT_DIR` set to the target directory (defaults to `/output` if unset):

```bash
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

This creates the output directory if needed and writes the poem as UTF-8 (773 characters, 775 bytes) to `entry.txt` with no extra trailing newline.

