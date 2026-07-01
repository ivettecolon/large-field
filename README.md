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

## Configuration

Edit the `CONFIG` object at the top of `index.html`:

- `wordDirectory`: path to the folder containing `manifest.json` (default `stimuli/words800/`)
- `numRandomTrials` / `numCheckTrials` / `numValidationTrials`: trial counts (default 900 / 10 / 90, matching the original image task)
- `validationTriplets`: optional hardcoded array of `{stimulus, choice1, choice2}` word triplets for consistent validation trials across participants; `null` samples random validation trials each run
- `experimentId` / `filenamePrefix`: [DataPipe](https://pipe.jspsych.org/) settings for saving CSV data
- `speedThreshold`: RT (ms) below which participants get a "too fast" warning
- `secretCode`: Prolific completion code

## Local testing

```bash
python -m http.server 8000
# then open http://localhost:8000
```

## GitHub Pages deployment

1. Push to GitHub.
2. Settings → Pages → Deploy from branch → `main` / root.
3. Experiment will be live at `https://<username>.github.io/<repo>/`.

## Differences from the image version

- Uses jsPsych's `html-button-response` plugin instead of `image-button-response`;
  words render as button text instead of images as button backgrounds.
- No `plugin-preload` step, since there are no image assets to preload.
- `manifest.json` has a `words` array instead of an `images` array, and validation
  triplets are plain words (no directory path prefix needed).
- Instructions/consent/demographics text otherwise kept identical to the original,
  with "images" reworded to "words" where relevant.
