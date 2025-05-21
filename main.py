from diagnosis import diagnose_user_input
from treatment import treatments
from encryption import secure_store_symptoms

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
