from knowledge_base_loader import medical_data

treatments = {disease: info['treatment'] for disease, info in medical_data.items()}
