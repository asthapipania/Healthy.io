#step:1 set api keys 

import os
GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

#step:2 convert image to required format
import base64
image_path="acne_img.jpg"
image_file=open(image_path,"rb")
encoded_image=base64.b64encode(image_file()).decode('utf-8')
def encode_image(image_path):
    image_path="acne_img.jpg"
    image_file=open(image_path,"rb")
    return base64.b64encode(image_file.read()).decode('utf-8')
    
    
#step:3 set up of multimodal llm
from groq import GROQ
query= "is there something wrong with my face?"
model="llama-3.2-90b-vision-preview"

def analyse_image_with_query(query,model, encoded_image):
   client=GROQ()


messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": query
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                },
            },
        ],
    }
]
chat_completion = client.chat.completions.create(
    messages=messages,
    model=model
)
return chat_completion.choices[0].message.content
