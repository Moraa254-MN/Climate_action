import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt


np.random.seed(42)
data = {
    'GDP': np.random.uniform(1000, 80000, 100),
    'Population': np.random.uniform(1e6, 1.4e9, 100),
    'Energy_Use': np.random.uniform(100, 10000, 100),
    'Industrial_Output': np.random.uniform(500, 20000, 100)
}
df = pd.DataFrame(data)


df['CO2_Emissions'] = (
    0.5 * df['GDP'] +
    0.3 * df['Energy_Use'] +
    0.1 * df['Industrial_Output'] +
    np.random.normal(0, 10000, 100)
)


X = df[['GDP', 'Population', 'Energy_Use', 'Industrial_Output']]
y = df['CO2_Emissions']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


lr = LinearRegression()
rf = RandomForestRegressor(n_estimators=100, random_state=42)

lr.fit(X_train, y_train)
rf.fit(X_train, y_train)


lr_preds = lr.predict(X_test)
rf_preds = rf.predict(X_test)

lr_mae = mean_absolute_error(y_test, lr_preds)
rf_mae = mean_absolute_error(y_test, rf_preds)

lr_r2 = r2_score(y_test, lr_preds)
rf_r2 = r2_score(y_test, rf_preds)


print(f"Linear Regression MAE: {lr_mae:.2f}, R2 Score: {lr_r2:.2f}")
print(f"Random Forest MAE: {rf_mae:.2f}, R2 Score: {rf_r2:.2f}")

plt.figure(figsize=(8, 6))
plt.scatter(y_test, rf_preds, alpha=0.7)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--')
plt.xlabel("Actual CO2 Emissions")
plt.ylabel("Predicted CO2 Emissions")
plt.title("Random Forest: Predicted vs Actual CO2 Emissions")
plt.grid(True)
plt.tight_layout()
plt.savefig("prediction_plot.png")
