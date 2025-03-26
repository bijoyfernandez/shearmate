# SHEARMATE

## Overview
**SHEARMATE** is a regression-based prediction app designed for estimating **Unconfined Compressive Strength (UCS)** of **clayey soil** using input parameters:

- **Liquid Limit (LL)**
- **Plastic Limit (PL)**
- **Specific Gravity (SG)**
- **Initial Moisture Content (IMC)**

The app provides **two processing modes**:
1. **Individual Prediction** – Enter input values manually to get a UCS prediction.
2. **Batch Processing** – Upload a CSV file containing multiple input values for batch prediction. The results can be saved as a CSV file.

> **Note:** This app is specifically trained on clayey soil data and may not provide accurate predictions for other soil types.

---

## Features
### Individual Prediction
- Users input values for **LL, PL, SG, and IMC** manually.
- The UCS is predicted and displayed instantly.
- The text boxes are aligned for an intuitive interface.

### Batch Processing
- Users upload a CSV file with multiple rows of input values.
- The app processes each row and generates UCS predictions.
- The results can be **saved as a CSV file**.

#### CSV File Requirements
- **File format:** `.csv`
- **Headers must be exactly:**  
  ```
  LL, PL, SG, IMC
  ```  
- **UCS column is not required in the input file.** The app will generate and append it to the output file.

---

## How It Works
1. **For Individual Prediction:**
   - Open the app.
   - Enter values for LL, PL, SG, and IMC.
   - Click **Predict** to get the UCS value.

2. **For Batch Processing:**
   - Click on **Batch Processing Mode**.
   - Upload a CSV file with LL, PL, SG, and IMC as headers.
   - The app processes the data and calculates UCS for each row.
   - Save the results as a CSV file.

---

## Model & Limitations
- The prediction model is trained on **clayey soil** data only.
- It is **not applicable** for other soil types.
- Future updates may include additional soil classifications and location-based parameters to improve versatility.

---

## Future Enhancements
* Support for different soil types (soft soil, coarse soil, etc.)  
* Location-based classification (e.g., riverside, coastal, inland)  
* More input parameters for better predictions  

---

## How to replicate the app
* User can download the exe file from link and run it direclty.  
* The second option is to download the UCS_model.pkl and config.json along with the main.p and use py_to)exe library to packaage the app to a runnable exe.

---

## License
SHEARMATE is provided as-is with no guarantees of accuracy beyond its trained dataset. Future improvements will enhance its usability and accuracy.
