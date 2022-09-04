from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

dataset = load_diabetes() # Şeker hastalığı veri seti
result = dataset.DESCR
result = dataset.head
print(result)