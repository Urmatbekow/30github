from transformers import AutoTokenizer, AutoModelForSequenceClassification
from sklearn.tree import DecisionTreeClassifier

tokenizer = AutoTokenizer.from_pretrained("your-transformers-model")
model_transformers = AutoModelForSequenceClassification.from_pretrained("your-transformers-model")

def analyze_order_book(text_input):
    inputs = tokenizer(text_input, return_tensors="pt", truncation=True)
    outputs = model_transformers(**inputs)
    return outputs

order_book_data = "Example limit order book text data..."
result = analyze_order_book(order_book_data)
print(result)
