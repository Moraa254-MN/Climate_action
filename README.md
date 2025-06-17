#  AI for Climate Action: Forecasting Carbon Emissions

This project uses "machine learning" to forecast "CO₂ emissions" by country, supporting **UN SDG 13 – Climate Action**. The goal is to help governments and environmental organizations make informed decisions using data.


##  Project Overview

- **SDG Focus**: SDG 13 – Climate Action  
- **Problem**: Carbon emissions continue to rise globally. Anticipating future emissions can help drive better climate policies.
- **Solution**: Using supervised machine learning (regression models) to predict CO₂ emissions based on features like GDP, population, and energy use.



##  Tools & Technologies

- Python  
- Jupyter Notebook  
- Pandas, NumPy  
- Scikit-learn  
- Matplotlib & Seaborn for visualizations  
- Dataset: [World Bank CO₂ Emissions](https://data.worldbank.org/indicator/EN.ATM.CO2E.KT) + [Kaggle CO2 Dataset](https://www.kaggle.com/datasets/yoannboyere/co2-ghg-emissionsdata)



## Model & Approach

- **Model Used**: Linear Regression & Random Forest Regressor  
- **Target Variable**: CO₂ Emissions (kt)  
- **Features**: GDP, population, energy use, industrial activity

Steps:
1. Data cleaning and preprocessing
2. Feature selection
3. Model training and testing
4. Evaluation (R² Score, MAE)
5. Visualization of predictions vs actual



##  Results

<p align="center">
  <img src="screenshots/prediction_plot.png" width="600"/>
  <br>
  <em>Predicted vs Actual CO₂ emissions (sample countries)</em>
</p>

- R² Score: `0.87` (example)
- MAE: `45,000 kt` (example)


##  Ethical Reflection

- **Bias:** Some countries have incomplete or outdated reporting, which may impact accuracy.
- **Fairness:** We aim for an inclusive model that considers countries of all income levels.
- **Sustainability:** A data-driven approach supports better environmental policy and awareness.



##  Files Included

| File Name              | Description                                  |
|------------------------|----------------------------------------------|
| `ClimateForecast.ipynb`| Jupyter Notebook with full ML pipeline       |
| `climate_model.py`     | Python script version of the notebook        |
| `README.md`            | Project overview                             |
| `screenshots/`         | Folder with result screenshots               |



##  How to Run

```bash
git clone https://github.com/yourusername/climate-co2-forecast.git
cd climate-co2-forecast
pip install -r requirements.txt
jupyter notebook ClimateForecast.ipynb
