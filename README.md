# 🚦 Traffic Signs Classification - Deep Learning Project

## 📋 Description

Ce projet utilise le Deep Learning pour classifier automatiquement les panneaux de signalisation routière. Il implémente un modèle de réseau de neurones convolutifs (CNN) capable de reconnaître 43 classes différentes de panneaux de signalisation.

Le projet inclut :
- 🤖 Un modèle de Deep Learning entraîné sur le German Traffic Sign Recognition Benchmark (GTSRB)
- 🌐 Une API Flask pour servir les prédictions
- 🐳 Configuration Docker pour le déploiement
- ☸️ Fichiers de configuration Kubernetes pour l'orchestration
- 📊 Notebooks Jupyter pour l'analyse et l'entraînement

## 🏗️ Structure du Projet

```
.
├── APPtrafic/                      # Application Flask principale
│   ├── app.py                      # API Flask pour les prédictions
│   ├── Dockerfile                  # Configuration Docker
│   ├── requirements.txt            # Dépendances Python
│   ├── traffic_sign_model.h5       # Modèle entraîné
│   └── k8s-yaml/                   # Fichiers de déploiement Kubernetes
│       ├── deployment.yaml
│       ├── service.yaml
│       ├── configmap.yaml
│       └── ...
│
└── deep learning/                  # Dossier d'entraînement et expérimentation
    ├── Traffic Signs image classification.ipynb  # Notebook d'analyse
    ├── traffic_sign_model.h5       # Modèle principal
    ├── mobilenet_best.h5           # Modèle MobileNet
    ├── model_aug_best.h5           # Modèle avec augmentation de données
    ├── archive/                    # Dataset GTSRB
    │   ├── Train/                  # Images d'entraînement (43 classes)
    │   ├── Test/                   # Images de test
    │   └── Meta/                   # Métadonnées
    └── model-viewer/               # Visualiseur de modèle
```

## 🎯 Classes de Panneaux Supportées

Le modèle peut reconnaître 43 types de panneaux de signalisation, incluant :
- Limitations de vitesse (20-120 km/h)
- Panneaux d'interdiction (Stop, No entry, etc.)
- Panneaux d'avertissement (Travaux, Piétons, etc.)
- Panneaux d'indication (Priorité, Cédez le passage, etc.)

## 🚀 Installation et Utilisation

### Prérequis

- Python 3.8+
- Docker (optionnel)
- Kubernetes (optionnel pour le déploiement)

### Installation Locale

1. **Cloner le repository**
```bash
git clone https://github.com/DorraMn/deepLearing_trafficSigns-.git
cd deepLearing_trafficSigns-
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. **Installer les dépendances**
```bash
cd APPtrafic
pip install -r requirements.txt
```

4. **Lancer l'application**
```bash
python app.py
```

L'API sera accessible sur `http://localhost:5000`

### Utilisation avec Docker

1. **Construire l'image Docker**
```bash
cd APPtrafic
docker build -t traffic-signs-app .
```

2. **Lancer le conteneur**
```bash
docker run -p 5000:5000 traffic-signs-app
```

### Déploiement avec Kubernetes

1. **Appliquer les configurations**
```bash
cd APPtrafic/k8s-yaml
kubectl apply -f configmap.yaml
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

2. **Vérifier le déploiement**
```bash
kubectl get pods
kubectl get services
```

## 🔌 Utilisation de l'API

### Endpoint de Prédiction

**POST** `/predict`

Envoyer une image encodée en base64 pour obtenir une prédiction.

**Exemple avec Python :**
```python
import requests
import base64

# Encoder l'image
with open("panneau.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode()

# Faire la requête
response = requests.post(
    "http://localhost:5000/predict",
    json={"image": encoded_string}
)

print(response.json())
```

**Réponse :**
```json
{
  "class": "Stop",
  "confidence": 0.98,
  "class_id": 14
}
```

## 📊 Modèles

Le projet contient plusieurs modèles entraînés :

1. **traffic_sign_model.h5** - Modèle CNN principal
2. **mobilenet_best.h5** - Transfer learning avec MobileNet
3. **model_aug_best.h5** - Modèle avec augmentation de données

## 🛠️ Technologies Utilisées

- **Deep Learning**: TensorFlow/Keras
- **Web Framework**: Flask
- **Data Processing**: NumPy, Pandas, PIL
- **Containerization**: Docker
- **Orchestration**: Kubernetes
- **Analysis**: Jupyter Notebook

## 📈 Performance du Modèle

Le modèle a été entraîné sur le German Traffic Sign Recognition Benchmark (GTSRB) avec :
- Plus de 50,000 images d'entraînement
- 43 classes de panneaux
- Haute précision de classification (>95%)

## 🔧 Développement

### Entraîner un nouveau modèle

1. Ouvrir le notebook `Traffic Signs image classification.ipynb`
2. Exécuter les cellules pour charger et prétraiter les données
3. Entraîner le modèle avec vos propres hyperparamètres
4. Sauvegarder le modèle entraîné

### Tester le modèle

```python
import tensorflow as tf
from PIL import Image
import numpy as np

# Charger le modèle
model = tf.keras.models.load_model('traffic_sign_model.h5')

# Charger et prétraiter l'image
img = Image.open('test_image.jpg')
img = img.resize((30, 30))
img_array = np.array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

# Prédire
prediction = model.predict(img_array)
class_id = np.argmax(prediction)
```

## 📝 Dataset

Le projet utilise le **German Traffic Sign Recognition Benchmark (GTSRB)** :
- Dataset disponible dans `deep learning/archive/`
- Images organisées par classe (0-42)
- Fichiers CSV avec métadonnées inclus

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est à des fins éducatives.



## 📞 Contact

Pour toute question ou suggestion, n'hésitez pas à ouvrir une issue sur GitHub.

---

⭐ Si ce projet vous a été utile, n'oubliez pas de mettre une étoile !
