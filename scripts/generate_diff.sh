#!/bin/bash

# Usage: bash generate_diff.sh

# Get the commit hash from the user
OLD_COMMIT=<INSERT YOUR COMMIT HASH HERE>

# Directories to process
CHAP_DIRS=("chap1_intro" "chap2" "chap3" "chap4" "chap5_conclusion")

# Loop over each chapter directory and compare the tex files
for CHAP in "${CHAP_DIRS[@]}"; do
    # Find the .tex file in each directory
    for TEX_FILE in ../$CHAP/*.tex; do
        # Skip if the file is a diff file
        if [[ "$TEX_FILE" == *_diff.tex ]]; then
            continue
        fi

        # Get the base filename without extension
        BASE_NAME=$(basename "$TEX_FILE" .tex)

        # Define the diff file name
        DIFF_FILE="${TEX_FILE%.*}_diff.tex"

        # Check if the file has been updated since the old commit
        if git diff --quiet "$OLD_COMMIT" -- "$TEX_FILE"; then
            echo "Skipping $DIFF_FILE: no changes since commit $OLD_COMMIT."
            continue
        fi

        # Extract the old version from the given commit hash
        OLD_FILE="old_${BASE_NAME}.tex"
        git show "$OLD_COMMIT:$TEX_FILE" > "$OLD_FILE" 2>/dev/null

        # Check if the original .tex file exists in the specified commit
        if [ $? -ne 0 ]; then
            echo "Warning: Original file $TEX_FILE not found in commit $OLD_COMMIT. Skipping."
            rm "$OLD_FILE"  # Remove the temporary file if it was created
            continue
        fi

        # Create the diff file using latexdiff
        latexdiff "$OLD_FILE" "$TEX_FILE" > "$DIFF_FILE"

        # Remove the old file after diff is generated
        rm "$OLD_FILE"

        # Notify the user
        echo "Generated diff file: $DIFF_FILE"
    done
done

echo "Diff generation complete."
