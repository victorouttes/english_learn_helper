from fuzzywuzzy import fuzz
import numpy as np
from docx import Document
from docx.shared import RGBColor


def combine_files():
    my_lyrics = r'my_lyrics/file.txt'
    official_lyrics = r'official_lyrics/file.txt'
    scores = []
    with open(my_lyrics, 'r') as my_lyrics_file, open(official_lyrics, 'r') as official_lyrics_file:
        my_lyrics_rows = my_lyrics_file.readlines()
        official_lyrics_rows = official_lyrics_file.readlines()

        result = Document()

        for my_lyrics_row, official_lyrics_row in zip(my_lyrics_rows, official_lyrics_rows):
            my_lyrics_row = my_lyrics_row.replace('\n', '').strip()
            official_lyrics_row = official_lyrics_row.replace('\n', '').strip()

            paragraph = result.add_paragraph()

            run1 = paragraph.add_run(my_lyrics_row)
            run1.font.color.rgb = RGBColor(255, 0, 0)
            paragraph.add_run('\n')
            run2 = paragraph.add_run(official_lyrics_row)
            run2.font.color.rgb = RGBColor(0, 0, 255)

            partial = fuzz.ratio(my_lyrics_row, official_lyrics_row)
            scores.append(partial)
        result.save('results.doc')
    return np.mean(scores)


score = combine_files()
print(f'Your score was: {score}/100.0!!')
print(f'Text saved in results.doc')
