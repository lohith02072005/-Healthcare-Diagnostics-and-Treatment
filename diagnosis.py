import torch
from sentence_transformers import SentenceTransformer, util
from knowledge_base_loader import embeddings, diagnoses

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def diagnose_user_input(user_input):
    user_embedding = embedding_model.encode(user_input, convert_to_tensor=True)
    cosine_scores = util.pytorch_cos_sim(user_embedding, embeddings)[0]
    top_results = torch.topk(cosine_scores, k=3)

    results = []
    for score, idx in zip(top_results[0], top_results[1]):
        disease = diagnoses[idx]
        confidence = float(score) * 100
        results.append((disease, confidence))
    return results
