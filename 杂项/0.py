import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.metrics import calinski_harabasz_score
import time

order_product = pd.read_csv("./29.预测用户对物品喜好案例_数据/order_products__prior.csv")
products = pd.read_csv("./29.预测用户对物品喜好案例_数据/products.csv")
orders = pd.read_csv("./29.预测用户对物品喜好案例_数据/orders.csv")
aisles = pd.read_csv("./29.预测用户对物品喜好案例_数据/aisles.csv")

table1 = pd.merge(order_product, products, on=["product_id", "product_id"])
table2 = pd.merge(table1, orders, on=["order_id", "order_id"])
table = pd.merge(table2, aisles, on=["aisle_id", "aisle_id"])

# 2.2 交叉表合并
table_cross = pd.crosstab(table["user_id"], table["aisle"])
print()