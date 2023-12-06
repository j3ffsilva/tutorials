from dotenv import load_dotenv
import os
import requests
import json
import openai

class InteliAPI:

    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        self.url = None

    def get_response(self, prompt, type="Text"):
        if (type == "Text"):
            return self.get_reply(prompt)
        else:
            return self.get_image_url(prompt)

    def get_reply(self, content, model="gpt-3.5-turbo", temperature=0.7):
        api_response_json = self.get_code_completion(content, model, temperature)
        return api_response_json['choices'][0]['message']['content']
        
    def get_image_url(self, prompt, n_images=1, size="1024x1024"):
        response = openai.Image.create(
            prompt=prompt,
            n=n_images,
            size=size
        )
        return response['data'][0]['url']
     

    # Helper methods 
    #==========================================================================
    def get_code_completion(self, content, model, temperature):
        self.url = "https://api.openai.com/v1/chat/completions"
        data = {
            "model": model,
            "messages": [{"role": "user", "content": content}],
            "temperature": temperature
        }

        response = requests.post(self.url, headers=self.headers, json=data)
        SUCCESSFUL_REQUEST = 200
        if response.status_code == SUCCESSFUL_REQUEST:
            return json.loads(response.text)
        else:
            return {
                "status_code": response.status_code,
                "error": response.text
            } 