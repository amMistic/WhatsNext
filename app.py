
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.preprocessing.text import tokenizer_from_json
import tensorflow.keras.utils as ku
import streamlit as st
import tensorflow as tf
import json

# Load the tokenizer from the JSON file
with open("tokenizer.json", "r", encoding="utf-8") as f:
    tokenizer_json = json.loads(f.read())
    tokenizer = tokenizer_from_json(tokenizer_json)

# Function to generate text based on input sequence
def generate_text(seed_text, num_next_words, model, max_sequence_length):
    for num in range(num_next_words):
        
        # Tokenize the input sequence
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        
        # Pad the sequence
        token_list = pad_sequences([token_list], maxlen=max_sequence_length, padding='pre')
        
        # Feed the preprocessed input data into the model to generate the next word
        predicted_probs = model.predict(token_list)[0]
        
        # Find the index of the word with the highest probability
        predicted_index = np.argmax(predicted_probs)
        
        # Find the word corresponding to the predicted index
        output_word = ''
        for word, index in tokenizer.word_index.items():
            if index == predicted_index:
                output_word = word
                break
            
        # Update the seed text (input taken + generated word --> to predict next word)
        seed_text += " " + output_word
    
    return seed_text.title()

# Streamlit app
def main():
    st.title("Text Generation App")
    
    # load the model
    model = tf.keras.models.load_model('model.h5')
    
    # Input sequence from the user
    input_sequence = st.text_input("Enter the input sequence:")
    
    # Number of words to generate
    num_next_words = st.slider("Number of next words to generate:", min_value=1, max_value=10, value=5)
    
    # Specifying the max sequence length
    max_seq_len = 17
    
    # Button to generate text
    if st.button("Generate Text"):
        # Generate text based on the input sequence
        generated_text = generate_text(input_sequence, num_next_words, model, max_seq_len)
        
        # Display the generated text
        st.write("Generated Text:", generated_text)

if __name__ == "__main__":
    main()
