
# HealthAI 🩺  
**Seamless Prediction, Smarter Prevention**  
AI-powered web application for early detection of chronic disease risks using personalized health data.

Link to the website : [https://healthai-smart-83d2096f7650.herokuapp.com/](https://healthai-seamless-prediction-smarter.onrender.com)
<p align="center">
  <img src="https://raw.githubusercontent.com/Jadav-Gajanand-19/HealthAI---seamless-prediction-smarter-prevention/main/logo.jpg" alt="HealthAI Logo" width="200"/>
</p>

🔗 GitHub Repository: [HealthAI---seamless-prediction-smarter-prevention](https://github.com/Jadav-Gajanand-19/HealthAI---seamless-prediction-smarter-prevention)

---

## 🧠 Problem Statement  
HealthAI addresses **Problem Statement 1** from the _Code for Care: AI & Tech for Preventive Healthcare_ hackathon.  
It is designed to enable **early prediction of lifestyle diseases** using **self-reported data**, eliminating the need for costly diagnostics.

> Predicts risks for:
- **Type 2 Diabetes**
- **Heart Disease**
- **Overall Chronic Disease Risk**

---

## 🌟 Key Features

### 🧬 Multi-Model Disease Prediction
- **Model 1: Diabetes Risk Classifier**  
  Based on PIMA Indian dataset — binary prediction (Diabetic/Non-Diabetic)
  
- **Model 2: Heart Disease Predictor**  
  Based on Cleveland Heart Disease dataset — binary prediction
  
- **Model 3: Overall Lifestyle Disease Risk**  
  Aggregates features and outputs to predict **Low / Medium / High** risk strata

### 🧠 Explainable AI
- Feature attribution using **SHAP** for transparency
- Users can see what factors contribute most to their predicted risk

### 🎯 Personalized Recommendations
- Context-aware health suggestions based on risk
- Covers:
  - Weight & diet goals
  - Activity & stress plans
  - Screening reminders

### 🖥️ Clean & Minimal UI
- Easy-to-use web interface for input and results
- Displays risk levels, top factors, and recommended actions

---

## 🧰 Tech Stack

| Component     | Technology Used                   |
|---------------|-----------------------------------|
| Frontend      | HTML, CSS, JavaScript             |
| Backend       | Flask (Python)                    |
| ML Models     | scikit-learn, XGBoost, SHAP       |
| Visualization | Matplotlib, SHAP                  |
| Deployment    | Heroku / Render                   |

---

## 📊 Datasets Used

1. **PIMA Indian Diabetes Dataset**  
   🔗 https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database

2. **Cleveland Heart Disease Dataset**  
   🔗 https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci

3. **Framingham Heart Study Dataset**  
   🔗 https://www.kaggle.com/datasets/amanajmera1/framingham-heart-study-dataset

---

## ⚙️ How to Run Locally

```bash
git clone https://github.com/Jadav-Gajanand-19/HealthAI---seamless-prediction-smarter-prevention.git
cd HealthAI---seamless-prediction-smarter-prevention

# (Optional) Create a virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Start the Flask app
python app.py
```

Visit: 📍 `http://localhost:5000` in your browser

---

## 📈 Evaluation Metrics

| Metric           | Purpose                              |
|------------------|---------------------------------------|
| Accuracy, AUROC  | Model performance                    |
| Brier Score      | Probability calibration              |
| SHAP Values      | Model explainability                 |
| Confusion Matrix | Class balance and misclassification  |

---

## 📦 Deliverables

- ✅ Web application for risk screening
- ✅ Three machine learning models
- ✅ SHAP visualizations for explainability
- ✅ Personalized health tips engine
- ✅ GitHub repo with complete code and documentation

---

## 🛡 Ethics & Disclaimers

- This tool is for **informational purposes only**.
- It is **not a diagnostic tool** and does not replace medical consultation.
- User data is processed locally and not stored without consent.

---

## 🔮 Future Roadmap

- 🔐 Add user authentication and data persistence
- 📱 Mobile app version (React Native or Flutter)
- 🌐 Multi-language interface
- 📊 Clinician dashboard for population risk tracking
- 📥 SMS/email health reminders

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!  
Please feel free to fork the repo and submit a pull request.

---

## 📬 Contact

Built with 💙 by **Gajanand Jadav and TeamAI**  
📧 Reach me via [GitHub Profile](https://github.com/Jadav-Gajanand-19)

---
