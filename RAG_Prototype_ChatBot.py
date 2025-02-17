import pandas as pd
import torch
from sentence_transformers import SentenceTransformer, util

# Load a pre-trained BERT embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load CSV database
csv_file = "knowledge_database.csv"  # Replace with your file
df = pd.read_csv(csv_file)

# Ensure the CSV has 'question' and 'answer' columns
if "question" not in df.columns or "answer" not in df.columns:
    raise ValueError("CSV file must contain 'question' and 'answer' columns.")

# Compute embeddings for all questions in the database
df["embedding"] = df["question"].apply(lambda x: model.encode(x, convert_to_tensor=True))

def retrieve_best_answer(user_query):
    """
    Retrieves the best answer from the CSV database using semantic similarity.
    
    Args:
        user_query (str): The input query from the chatbot user.

    Returns:
        best_answer (str): The most relevant answer from the database.
        best_score (float): Similarity score of the retrieved answer.
    """
    query_embedding = model.encode(user_query, convert_to_tensor=True)
    similarities = [util.pytorch_cos_sim(query_embedding, emb).item() for emb in df["embedding"]]
    
    best_idx = torch.argmax(torch.tensor(similarities)).item()
    best_answer = df.iloc[best_idx]["answer"]
    best_score = similarities[best_idx]
    
    return best_answer, best_score

# Example chatbot loop
while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        break

    response, score = retrieve_best_answer(user_input)
    print(f"Chatbot (Confidence: {score:.2f}): {response}")
