
# 🌿 Smart/Automated Irrigation Using Soil Moisture and Weather Data  
**AICTE-Edunet Internship | Machine Learning-Based Irrigation System**

This project presents a smart irrigation solution that leverages machine learning to automate water distribution in farms using real-time **soil moisture**, **sensor readings**, and environmental data. By analyzing inputs from **20+ sensors**, the system predicts which of the **three pumps (P1, P2, P3)** need to be activated, thereby conserving water and optimizing crop yield.

---

## ✅ Project Highlights

- 🔍 **EDA & Preprocessing**: Cleaned and prepared real sensor data using Python and Pandas  
- 🤖 **Model Training**: Trained an ML classifier to predict pump statuses based on 20 input features  
- 💾 **Model Deployment**: Saved model as `.pkl` and integrated into a custom **Streamlit web app**  
- 🌐 **Frontend UI**: Built an intuitive interface with sliders, visual insights, and smart predictions  
- 🚀 **Result**: A live-working model to assist farmers in automating irrigation with data-driven insights

---

## 🛠️ Tools & Technologies Used

| Category               | Stack                               |
|------------------------|--------------------------------------|
| **Programming**        | Python                               |
| **IDE/Environment**    | VS Code                              |
| **Libraries**          | Pandas, NumPy, Scikit-learn, Matplotlib, Streamlit |
| **ML Algorithm**       | Random Forest classifier             |
| **Model Saving**       | `joblib`                             |
| **Deployment**         | Streamlit with multipage navigation  |

---

## 📁 Project Structure

```
├── smart_irrigation.ipynb        # Core notebook for EDA, training, model building
├── model/
│   └── irrigation_model.pkl      # Trained ML model
├── app.py                        # Streamlit multipage launcher
├── home.py                       # Landing page UI
├── pages/
│   └── predict.py                # Sensor input + prediction interface
├── assets/
│   ├── edunet_logo.png
│   ├── aicte_logo.png
│   └── field.png
└── smart_irrigation.csv          # Sensor dataset
```

---

## 📊 Dataset Overview

The dataset contains 20 sensor readings (scaled between 0–1) representing various soil and environmental factors.  
Each row corresponds to a snapshot of sensor data and the corresponding **ON/OFF state for pumps P1, P2, and P3**.

---

## 🚀 How to Run the Project

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-repo/smart-irrigation.git
   cd smart-irrigation
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App**
   ```bash
   streamlit run app.py
   ```

---

## 🎯 Learning Outcomes

- Understood the workflow of ML projects — from **data cleaning to deployment**
- Applied **EDA, model selection, evaluation**, and saved production-ready models
- Created a responsive and visual **web interface for real-time ML prediction**
- Learned to **integrate UI with ML** to deliver end-user solutions

---

## 🔮 Future Enhancements

- Integrate **live sensor data** from Arduino/ESP32-based IoT hardware  
- Use external **weather APIs** for smarter, environment-aware decisions  
- Enable **automated pump triggering** in real-world farms via embedded systems

---

## 🤝 Acknowledgements

This project was developed under the **Edunet Foundation** Internship program supported by **AICTE**, Government of India.

---

## 📌 Author

**Mukilan K.**  
B.Tech AI & DS Student | Passionate about AgriTech & ML  
Connect: [LinkedIn](https://www.linkedin.com/in/mukilan-k-ai) • [GitHub](https://github.com/MUKILAN-K)
