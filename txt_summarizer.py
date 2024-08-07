#TEXT SUMMARIZATION USING PRE TRAINED MODELS

"""libraries installation:  
    1. pip install transformers
    2. pip install torch  
"""

from transformers import pipeline

# Load a pre-trained summarization model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Provide a long text passage
text = """
The Apollo program was the third United States human spaceflight program carried out by NASA, which succeeded in landing the first humans on the Moon from 1969 to 1972. First conceived during Dwight D. Eisenhower's administration as a three-person spacecraft to follow the one-person Project Mercury, which put the first Americans in space, Apollo was later dedicated to President John F. Kennedy's national goal of "landing a man on the Moon by the end of this decade and returning him safely to the Earth" in an address to Congress on May 25, 1961. Project Mercury was followed by the two-person Project Gemini (1962–66). The first manned flight of Apollo was in 1968. Apollo ran from 1961 to 1972, and was supported by the two-man Gemini program which ran concurrently with it from 1962 to 1966. Gemini missions developed some of the space travel techniques that were necessary for the success of the Apollo missions. Apollo used Saturn family rockets as launch vehicles. Apollo/Saturn vehicles were also used for an Apollo Applications Program, which consisted of Skylab, a space station that supported three manned missions in 1973–74, and the Apollo–Soyuz Test Project, a joint Earth orbit mission with the Soviet Union in 1975.
"""

# Generate a summary
summary = summarizer(text, max_length=130, min_length=30, do_sample=False)

# Print the original text and the summary
print("Original Text:\n", text)
print("\nSummary:\n", summary[0]['summary_text'])
