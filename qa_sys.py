from transformers import pipeline

# Load a pre-trained QA model
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# Provide a text passage
text = """The Apollo program was the third United States human spaceflight program carried out by NASA, which succeeded in landing the first humans on the Moon from 1969 to 1972. First conceived during Dwight D. Eisenhower's administration as a three-person spacecraft to follow the one-person Project Mercury, which put the first Americans in space, Apollo was later dedicated to President John F. Kennedy's national goal of "landing a man on the Moon by the end of this decade and returning him safely to the Earth" in an address to Congress on May 25, 1961. Project Mercury was followed by the two-person Project Gemini (1962–66). The first manned flight of Apollo was in 1968. Apollo ran from 1961 to 1972, and was supported by the two-man Gemini program which ran concurrently with it from 1962 to 1966. Gemini missions developed some of the space travel techniques that were necessary for the success of the Apollo missions. Apollo used Saturn family rockets as launch vehicles. Apollo/Saturn vehicles were also used for an Apollo Applications Program, which consisted of Skylab, a space station that supported three manned missions in 1973–74, and the Apollo–Soyuz Test Project, a joint Earth orbit mission with the Soviet Union in 1975."""

# Provide a question
ques = "Who succeeded in landing the first humans on the Moon?"

# Get the answer
result = qa_pipeline(question=ques, context=text)
print(f"Question: {ques}")
print(f"Answer: {result['answer']}")
