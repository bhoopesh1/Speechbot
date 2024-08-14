import google.generativeai as genai
import pyttsx3

GOOGLE_API_KEY = 'AIzaSyDNxkTwCLdkrCXcwGX1-ndJPthfS3GbUsc' 
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.0-pro-latest")

def generate_text(prompt):
    response = model.generate_content(prompt)
    return response.text
while True:
  user_input = input("Ask Gemini: ")
  if user_input.lower() == "exit":
    break
  if not user_input:
    print("Please provide a prompt.")
    continue
  response = generate_text(user_input)
  if response:
    print(response)

speech=pyttsx3.init()
speech.say(response)
speech.runAndWait


