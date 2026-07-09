# Triadic Judgment Task — Words

Word-based adaptation of the image triadic judgment task. On each trial, participants see one target word and
two choice words, and pick the choice most similar in meaning to the target.

The 800-word stimulus set comes from the `Greedy_Init_800` sheet (`Word` column)
of `800wordlist_313seed.xlsx`.

## Structure

```
index.html                          # Main experiment (jsPsych)
kc_lab_consent_prolific.png         # Consent form image (unused by default; text consent is inline)
stimuli/
└── words800/
    └── manifest.json               # {"words": [...]} generated from the xlsx
additional_scripts/
└── generate_word_manifest.py       # Regenerates manifest.json from the xlsx
800wordlist_313seed.xlsx            # Source word list
```

## Regenerating the word manifest

If the word list changes, regenerate `stimuli/words800/manifest.json`:

```bash
pip install openpyxl
python additional_scripts/generate_word_manifest.py [xlsx_path] [sheet_name]
# defaults to 800wordlist_313seed.xlsx and sheet "Greedy_Init_800"
```
