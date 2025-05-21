import json
from sentence_transformers import SentenceTransformer

# Load medical data
with open('medical_knowledge_base_realistic.json', 'r') as f:
    medical_data = json.load(f)

# Prepare for model usage
symptom_texts = [" ".join(info['symptoms']) for info in medical_data.values()]
diagnoses = list(medical_data.keys())

# Load embeddings
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = embedding_model.encode(symptom_texts, convert_to_tensor=True)
