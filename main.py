import google.generativeai as genai
import pyttsx3

GOOGLE_API_KEY = 'AIzaSyDNxkTwCLdkrCXcwGX1-ndJPthfS3GbUsc' 
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.0-pro-latest")

def generate_text(prompt):
  try:
    response = model.generate_content(prompt)
    return response.text
  except Exception as e:
    print(f"An error occurred: {e}")
    return None

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


