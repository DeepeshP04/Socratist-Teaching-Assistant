import google.generativeai as genai
import os
from dotenv import load_dotenv
import time

load_dotenv()

class Socratist:
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
    model_name="gemini-1.5-flash-001-tuning",
    generation_config=self.generation_config)
    
    return model
  
  def fine_tune(self):
    base_model = self.create_model()
    
    # Read and load training data
    with open("../static/training_data.txt", "r") as f:
        training_data = f.read()
        
    # Use the training data in the API call to create a tuned model
    operation = genai.create_tuned_model(
        display_name="increment-pjszihh2m5wn",
        source_model=base_model.model_name,
        epoch_count=20,
        batch_size=4,
        learning_rate=0.001,
        training_data=training_data,
    )

    # Wait for the tuning operation to complete
    for status in operation.wait_bar():
        time.sleep(10)

    # Retrieve and print the result of the tuning operation
    result = operation.result()
    print("Fine-tuned model created:", result)
 
  def chat(self, user_message, chat_history=[]):
    model = genai.GenerativeModel(model_name="tunedModels/increment-pjszihh2m5wn")
    
    history = chat_history
    chat = model.start_chat(history=history)
        
    # Send the new user message to the model
    response = chat.send_message(user_message)
      
    # Add the response to the chat history
    history.append({"role": "user", "parts": user_message})
    history.append({"role": "model", "parts": response.text})
      
    return {"response": response.text, "history": history}