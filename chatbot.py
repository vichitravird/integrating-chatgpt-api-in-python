pip install openai
from openai import OpenAI
user=OpenAI(api_key='sk-')
gptmodel="gpt-3.5-turbo"
userrole="user"
inputquestion=input("Type your Question here")
response=user.chat.completions.create(
model=gptmodel,messages=[
    {"role": userrole, "content": inputquestion}
])
response.choices[0].message.content
