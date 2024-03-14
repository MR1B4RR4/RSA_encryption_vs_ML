import numpy as np
import pandas as pd	

file = open("text_file.txt", "r")
content_text = file.read()
file.close()

content_text_characters = content_text.split()

df = pd.DataFrame(content_text_characters).rename(columns={0: "word"})
df['']