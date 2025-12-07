from flask import Flask
import tensorflow as tf

app = Flask(__name__)

# Charger le modèle
try:
    model = tf.keras.models.load_model('model_aug_best.h5')
    print("✅ Modèle 'model_aug_best.h5' chargé avec succès.")
except Exception as e:
    print(f"❌ Erreur de chargement du modèle : {e}")

@app.route('/')
def home():
    return "✅ Modèle 'model_aug_best.h5' chargé avec succès !"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
