# Experiment 1: Environment & Connectivity
# AIM:
# To install the required Python libraries, securely configure the API key, establish connectivity with
# the Large Language Model (LLM), and verify successful model access by executing a simple
# prompt ("Hello, World").
# DESCRIPTION:
# Large Language Models (LLMs) require proper environment setup and API configuration before
# they can be used for prompt engineering tasks. This experiment introduces the basic workflow for
# establishing communication between a Python application and an LLM using an API.
#  The experiment focuses on setting up the Python environment by installing the required
# libraries, configuring the API key securely using a .env file, and establishing connectivity with the
# Large Language Model (LLM). After creating the client and loading the API credentials, a simple
# "Hello, World!" prompt is executed to verify successful communication with the model. The
# successful response confirms that the environment and API are correctly configured, providing the
# foundation for all subsequent prompt engineering experiments.
#  PROGRAM:
# Step 1: Import the Google GenAI library
from google import genai
# Step 2: Create the Gemini client using your API key
client = genai.Client(
api_key="YOUR_GEMINI_API_KEY"
)
# Step 3: Display a heading
print("GOOGLE GEMINI ENVIRONMENT & CONNECTIVITY TEST\n")
# Step 4: Send a prompt to the Gemini model
response = client.models.generate_content(
model="gemini-3.6-flash",
contents="Print only: Hello World"
)
# Step 5: Display the generated response
print("Response from Gemini:\n")
print(response.text)

"""OUTPUT:
 GOOGLE GEMINI ENVIRONMENT & CONNECTIVITY TEST
 Response from Gemini:
 Hello World """