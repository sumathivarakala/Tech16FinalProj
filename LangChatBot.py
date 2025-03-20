pip install openai
import openai
import streamlit as st

# Function to interact with GPT-3.5-turbo model and get responses
def get_chatbot_response(messages, api_key):
    openai.api_key = api_key
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=messages,
        temperature=0.7,
        max_tokens=150,
    )
    return response['choices'][0]['message']['content'].strip()

# LanguageLearningChatbot Class
class LanguageLearningChatbot:
    def __init__(self, language="Kannada"):
        self.language = language
        self.english_to_kannada = {
            "hello": "Namaskara (ನಮಸ್ಕಾರ)",
            "how are you?": "Neevu Chennaagidira? (ನೀವು ಚೆನ್ನಾಗಿದೀರಾ?)",
            "i am fine.": "Naanu chennagiddene (ನಾನು ಚೆನ್ನಾಗಿದ್ದೇನೆ)",
            "fine, thank you.": "Chennagiddene. Dhanyavaada (ಚನ್ನಾಗಿದ್ದೇನೆ. ಧನ್ಯವಾದ)",
            "goodbye": "Hogibitt barthene (ಹೋಗಿಬಿಟ್ಟ ಬರುವುದೇ)",
            "what is your name?": "Nimma hessarenu? (ನಿಮ್ಮ ಹೆಸರೇನು?)",
            "my name is…": "Nanna hesaru… (ನನ್ನ ಹೆಸರು…)",
            "nice to meet you.": "Nimmannu nodi santhoshavaythu (ನಿಮ್ಮನ್ನು ನೋಡಿ ಸಂತೋಷವಾಗಿದೆ)",
            "please": "Dayavit.t.u. (ದಯವಿಟ್ಟು)",
            "thank you": "Vandenegalo (ವಂದನೆಗಳೋ)",
            "you're welcome": "Tamage suswagatha (ತಮಗೆ ಸುಸ್ವಾಗತ)",
            "yes": "Havdu (ಹವ್ದು)",
            "no": "Illa (ಇಲ್ಲ)",
            "excuse me (getting attention)": "Illinodi (ಇಲ್ಲಿನೋಡಿ)",
            "excuse me (begging pardon)": "K-shamisi (ಕ್ಷಮಿಸಿ)",
            "i’m sorry.": "Nannindha thappaihu (ನಾನು ತಪ್ಪೆಯಿದ್ದೇನೆ)",
            "good morning": "Shubha munjane (ಶುಭ ಮುಂಜಾನೆ)",
            "good evening": "Shubha sanje (ಶುಭ ಸಂಜೆ)",
            "good night": "Shubha ratri (ಶುಭ ರಾತ್ರಿ)",
            "mother": "Amma / taayi (ಅಮ್ಮ / ತಾಯಿ)",
            "father": "Appa / tande (ಅಪ್ಪ / ತಂದೆ)",
            "son": "Maga (ಮಗ)",
            "daughter": "magaLu (ಮಗಳು)",
            "elder brother": "aNNa (ಅಣ್ಣ)",
            "younger brother": "Tamma (ತಮ್ಮ)",
            "elder sister": "Akka (ಅಕ್ಕ)",
            "younger sister": "Tangi (ತಂಗಿ)",
            "grandfather": "Ajja / taata (ಅಜ್ಜ / ತಾತ)",
            "grandmother": "Ajji (ಅಜ್ಜಿ)",
            "husband": "ganDa (ಗಂಡ)",
            "wife": "henDathi (ಹೆಂಡತಿ)",
            "children": "makkaLu (ಮಕ್ಕಳು)",
            "breakfast": "Thindi (ತಿಂದಿ)",
            "lunch": "Oota (ಊಟ)",
            "eggs": "Motte (ಮೊಟ್ಟೆ)",
            "rice": "Anna (ಅನ್ನ)",
            "coffee": "Kaapi (ಕಾಫಿ)",
            "water": "Neeru (ನೀರು)",
            "beans": "huraLikaayi (ಹುರಳಿಕಾಯಿ)",
            "potato": "Aaloo geDDe (ಆಲೂ ಗೇಡ್ಡೆ)",
            "apple": "sEbu (ಸೆಬು)",
            "orange": "kittaLe (ಕಿತ್ತಲೆ)",
            "vegetables": "Tarakaarigalu (ತರಕಾರಿಗಳು)",
            "salad": "kOsaMbari (ಕೋಸಂಬರಿ)",
            "butter": "beNNe (ಬೆಣ್ಣೆ)",
            "milk": "Haalu (ಹಾಲು)",
            "sugar": "Sakkare (ಸಕ್ಕರೆ)",
            "tea": "Chaa (ಚಾ)"
        }
    
    def greet_user(self):
        return "Hello! I can help you learn Kannada. How can I assist you?"
    
    def translate(self, user_input):
        english_word = user_input.lower().strip()
        return self.english_to_kannada.get(english_word, "Sorry, I don't have that word.")

# Streamlit UI for the chatbot
def main():
    # Get the OpenAI API key from the user
    api_key = st.text_input("Please enter your OpenAI API key:", type="password")
    
    if api_key:
        # Initialize the chatbot
        chatbot = LanguageLearningChatbot()

        st.title("Kannada Language Learning Chatbot")
        st.write(chatbot.greet_user())

        # Input for user queries
        user_input = st.text_input("Enter an English word (e.g., 'hello') to get its Kannada translation:", "")
        
        if user_input:
            response = chatbot.translate(user_input)
            st.write(f"The Kannada translation is: {response}")
            
    else:
        st.write("Please provide a valid OpenAI API key to start interacting.")

# Run the Streamlit app
if __name__ == "__main__":
    main()
