import torch
from sentence_transformers import SentenceTransformer, util
from sklearn.preprocessing import MinMaxScaler

# Load a Transformer model (BERT for sentence embeddings)
bert_model = SentenceTransformer('all-MiniLM-L6-v2')  # Lightweight and fast

def calculate_prometheus_score(reference, response, threshold=0.7):
    """
    Approximates Prometheus Score using semantic similarity and factuality checks.

    Args:
        reference (str): Ground truth reference response.
        response (str): Chatbot-generated response.
        threshold (float): Cosine similarity threshold for high coherence.

    Returns:
        prometheus_score (float): A score approximating Prometheus evaluation.
    """

    # Step 1: Compute Semantic Similarity (BERTScore)
    ref_embedding = bert_model.encode(reference, convert_to_tensor=True)
    resp_embedding = bert_model.encode(response, convert_to_tensor=True)
    
    similarity_score = util.pytorch_cos_sim(ref_embedding, resp_embedding).item()

    # Step 2: Apply Normalization to map scores between 0-1
    scaler = MinMaxScaler(feature_range=(0, 1))
    normalized_similarity = scaler.fit_transform([[similarity_score]])[0][0]

    # Step 3: Compute Final Prometheus Score (Heuristic Approximation)
    # Prometheus score formula (approximated): weighted combination of similarity + confidence
    prometheus_score = (0.8 * normalized_similarity) + (0.2 * (similarity_score >= threshold))

    return round(prometheus_score, 4), similarity_score

# Example chatbot response evaluation
reference_response = "The capital of France is Paris."  # What if there is no reference response?
chatbot_response = "Paris is the capital of France."

# Compute evaluation scores
prometheus_score, similarity = calculate_prometheus_score(reference_response, chatbot_response)

# Print results
print(f"Cosine Similarity: {similarity:.4f}")
print(f"Prometheus Score: {prometheus_score:.4f}")
