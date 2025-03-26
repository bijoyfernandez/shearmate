# SHEARMATE

## Development Process

### **1. Data Collection & Processing**
- Soil samples were collected from **four different locations**, with **30 samples per location**, totaling **120 soil samples**.
- Each sample was **physically tested in a lab** to obtain its **input and output properties**:
  - **Liquid Limit (LL)**
  - **Plastic Limit (PL)**
  - **Specific Gravity (SG)**
  - **Initial Moisture Content (IMC)**
  - **Unconfined Compressive Strength (UCS) (target variable)**

### **2. Data Cleaning & Model Selection**
- The **120-sample dataset** was **analyzed for outliers**, which were removed.
- The dataset was tested against multiple regression models, with the **Random Forest Regressor** providing the best performance.

### **3. Model Training & Exporting**
- **Feature importance** was analyzed to ensure relevant parameters were used.
- A **Random Forest Regressor model** was trained, but due to its nature, no explicit equation could be derived to represent the relationship between inputs and UCS.
- The trained model was **exported as a `.pkl` file** for deployment.

### **4. App Development**
- The app was built using **PyQt5** for the graphical user interface.
- The **`.pkl` model** was integrated into the app for real-time and batch UCS predictions.

---

## Merits & Demerits

### **Merits**
- **Time-Saving & Efficient** – The model significantly reduces testing time compared to traditional lab methods.
- **Useful in Difficult Conditions** – It provides a viable alternative when sample collection is difficult due to climatic conditions or large site coverage.

### **Demerits**
- **Limited Soil Applicability** – The model is trained **only on soft clay soil** collected near water bodies. It may not work well for inland coarse soils commonly used in construction.

---

## Future Improvements

### **1. Expanding Soil Data**
To improve the model’s accuracy across various soil types, additional data should be collected:
- **Soil types**: Soft soil, hard clay soil, coarse soil, etc.
- **Geographical variation**: Inland, riverbanks, marshlands, plateaus, mountains, coastal regions.
- **Location-based classification**: Instead of just soil type, the model can incorporate the **district-wise soil properties** (e.g., specific states or regions).

### **2. Enhancing Input Parameters**
- **Soil color analysis** – Variations in color could indicate different compositions and mechanical properties.
- **Chemical composition** – Additional parameters like mineral content could improve prediction accuracy.
- **New derived features**:
  - **Plasticity Index (PI) = LL - PL**
  - **Plasticity Ratio = LL / PL**
  - Other ratios correlating **LL, PL, SG, and IMC**

### **3. Feature Engineering & Correlation Analysis**
- Introducing **additional parameters** that influence **UCS** while maintaining strong correlation with **LL, PL, SG, and IMC**.
- Evaluating relationships between existing and new properties to refine the prediction model.

---

## Conclusion
SHEARMATE is a step towards **automating soil strength prediction**, making it **faster and more accessible**. Future updates will improve its **accuracy, versatility, and real-world usability** for a wider range of soil conditions.
"""
