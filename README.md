output will be in this format:-
Device set to use cpu
[{'label': 'NEGATIVE', 'score': 0.9997662901878357}]
[{'label': 'POSITIVE', 'score': 0.9991620779037476}]

#The output will be seen in the terminal itself

This script uses the Hugging Face transformers library to perform sentiment analysis on a given text. It leverages a pre-trained model (distilbert-base-uncased-finetuned-sst-2-english) to classify the sentiment of the input text as either POSITIVE or NEGATIVE.

Usage
Install Dependencies:
Ensure you have the required libraries installed. Run the following command:

bash
Copy
pip install transformers tf-keras
Run the Script:
Execute the script using Python:

bash
Copy
python classifier.py
Output:
The script will output the sentiment analysis results directly in the terminal. The output will be in the following format:

plaintext
Copy
Device set to use cpu
[{'label': 'NEGATIVE', 'score': 0.9997662901878357}]
[{'label': 'POSITIVE', 'score': 0.9991620779037476}]
label: The predicted sentiment (POSITIVE or NEGATIVE).

score: The confidence score of the prediction (ranges from 0 to 1).
