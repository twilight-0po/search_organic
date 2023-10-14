import pandas as pd
import numpy as np


def cal_score(product_info, weight_list):
    total_score = 0
    for idx in range(1, len(product_info)):
        factor_score = product_info[idx] * weight_list[idx - 1]
        total_score += factor_score
    return (product_info[0], total_score)

        



data = pd.read_csv("sample_product.csv")
print(data)
user_input = [1, 3, 2, 5, 6, 4]

weight_list = []
for factor in data.columns[1:]:
    corel = np.corrcoef(data[factor], user_input)
    weight_list.append(corel[0][1])

new_product = ["new", 8, 3, 2000]

score = cal_score(new_product, weight_list)
print(weight_list)