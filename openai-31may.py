import openai
import pandas as pd

df = pd.read_csv(f'C:\\Users\\agraw\\OneDrive\\Documents\\Aparna\\Lexolve\\company-info\\invoice.csv', encoding='utf-8')

# all client options can be configured just like the `OpenAI` instantiation counterpart
openai.base_url = "https://api.openai.com/v1/"
openai.default_headers = {"x-foo": "true"}

# Function to translate text using OpenAI
def translate_text(text, desc, target_language='Norsk'):
  print('desc :: ' + desc)
  prompt = f"Please translate the following English text to Norwegian: {text} Only respond with the translation and nothing else. If the context of the text is unclear, the following description of the English text might help to clear up ambiguities: {desc}  If the English text is not likely to have a Norwegian equivalent, e.g. being an English name for some subject or similar, keep the English text."
  completion = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": prompt,
        },
    ],
  )
  return completion.choices[0].message.content

# Translate each text
for index, row in df.iterrows():
    translated_text = translate_text(row['referencevalue'], row['description'])
    df.at[index, 'translated_text'] = translated_text
# Save the DataFrame to a new Excel file
df.to_csv(f'C:\\Users\\agraw\\OneDrive\\Documents\\Aparna\\Lexolve\\company-info\\translated_texts-gpt3.5-31may.csv', encoding='utf-8')