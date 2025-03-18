from transformers import pipeline

# Ensure you have installed PyTorch or TensorFlow
classifier = pipeline("sentiment-analysis")

# Test the sentiment analysis pipeline
result1 = classifier("Being with you is waste of time")
result2 = classifier("I've been waiting for you my whole life")
print(result1)
print(result2)