import json
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from cryptography.fernet import Fernet
from sentence_transformers import SentenceTransformer, util
import torch
# Load dynamic medical knowledge base from JSON
with open('medical_knowledge_base_realistic.json', 'r') as f:
    medical_data = json.load(f)
# Prepare dataset for training
symptom_texts = [" ".join(info['symptoms']) for info in medical_data.values()]
diagnoses = list(medical_data.keys())
# Initialize NLP model for semantic matching
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = embedding_model.encode(symptom_texts, convert_to_tensor=True)
# Treatment mapping
treatments = {disease: info['treatment'] for disease, info in medical_data.items()}
# Encryption key generation
key = Fernet.generate_key()
cipher_suite = Fernet(key)
# Chatbot-like interface
def diagnose_user_input(user_input):
    user_embedding = embedding_model.encode(user_input, convert_to_tensor=True)
    cosine_scores = util.pytorch_cos_sim(user_embedding, embeddings)[0]

    top_results = torch.topk(cosine_scores, k=3)  # Top 3 possible matches
    results = []
    for score, idx in zip(top_results[0], top_results[1]):
        disease = diagnoses[idx]
        confidence = float(score) * 100
        results.append((disease, confidence))
    return results

def secure_store_symptoms(symptoms):
    encrypted = cipher_suite.encrypt(symptoms.encode())
    decrypted = cipher_suite.decrypt(encrypted).decode()
    return encrypted, decrypted

def run_diagnostic_system():
    print("\nWelcome to the Advanced AI Healthcare Assistant")
    symptoms = input("Describe your symptoms (comma or space-separated): ").strip().lower()
    print("\nAnalyzing symptoms with AI model...\n")

    matches = diagnose_user_input(symptoms)

    for disease, confidence in matches:
        print(f"🩺 Possible Condition: {disease} (Confidence: {confidence:.2f}%)")
        print(f"💊 Recommended Treatment: {treatments[disease]}\n")

    encrypted, decrypted = secure_store_symptoms(symptoms)
    print(f"🔐 Encrypted Symptom Log: {encrypted}")
    print(f"✅ Decrypted Check (for reference): {decrypted}")
if __name__ == "__main__":
    run_diagnostic_system()
