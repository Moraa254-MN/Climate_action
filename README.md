
#  AI for Climate Action: Forecasting Carbon Emissions

This project uses **machine learning** to forecast **CO₂ emissions** by country, supporting **UN SDG 13 – Climate Action**. The goal is to help governments and environmental organizations make informed decisions using data.


##  Project Overview

- **SDG Focus**: SDG 13 – Climate Action  
- **Problem**: Carbon emissions continue to rise globally. Anticipating future emissions can help drive better climate policies.
- **Solution**: Using supervised machine learning (regression models) to predict CO₂ emissions based on features like GDP, population, and energy use.



##  Tools & Technologies

- Python  
- Jupyter Notebook / Script  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib for visualizations  

Dataset: Synthetic demo dataset (real data can be used from [World Bank CO₂ Emissions](https://data.worldbank.org/indicator/EN.ATM.CO2E.KT) or [Kaggle CO2 Dataset](https://www.kaggle.com/datasets/yoannboyere/co2-ghg-emissionsdata))



##  Model & Approach

- **Model Used**: Linear Regression & Random Forest Regressor  
- **Target Variable**: CO₂ Emissions (kt)  
- **Features**: GDP, Population, Energy Use, Industrial Output

### Steps:
1. Data cleaning and preprocessing
2. Feature selection
3. Model training and testing
4. Evaluation (R² Score, MAE)
5. Visualization of predictions vs actual



##  Results

![Prediction Plot](prediction_plot.png)

- R² Score: ~0.60 (Linear Regression)
- MAE: ~7868.00 (Linear Regression)



##  Ethical Reflection

- **Bias**: Some countries may lack complete data, affecting prediction accuracy.
- **Fairness**: The goal is a fair model that serves all regions regardless of size or income.
- **Sustainability**: Aims to inform proactive climate action via predictive modeling.



##  Files Included

| File Name              | Description                                  |
|------------------------|----------------------------------------------|
| `climate_model.py`     | Python script with ML pipeline               |
| `prediction_plot.png`  | Result visualization image                   |
| `README.md`            | Project overview and instructions            |



##  How to Run

```bash
# Clone the repository
git clone https://github.com/yourusername/climate-co2-forecast.git
cd climate-co2-forecast

# Run the script
python climate_model.py
```



##  Contact

For questions or collaboration, feel free to connect!
email:mercynyabuto24@gmail.com
