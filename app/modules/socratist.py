import google.generativeai as genai
import os
import json

class SocraticLearnAi:
  generation_config = {
    "temperature": 0.2,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 100,
    "response_mime_type": "text/plain",
  }

  def __init__(self, api_key):
    self.api_key = api_key
    self.configure_client()
    
  def configure_client(self):
      genai.configure(api_key=self.api_key)

  def create_model(self):
    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=self.generation_config)
    
    return model
  
  def chat(self, user_message, chat_history=[]):
    model = self.create_model()
    
    history = chat_history
    chat = model.start_chat(history=history)
        
    # Send the new user message to the model
    response = chat.send_message(user_message)
      
    # Add the response to the chat history
    history.append({"role": "user", "parts": user_message})
    history.append({"role": "model", "parts": response['text']})
      
    return {"response": response["text"], "history": history}
    
    
    