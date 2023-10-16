import pandas as pd
import numpy as np


def cal_score(product_info, weight_list):
    total_score = 0
    for idx in range(1, len(product_info)):
        factor_score = product_info[idx] * weight_list[idx - 1]
        #요소 값에 그대로 가중치를 곱하니 단위가 큰 가격 요소가 가장 많이 반영됨
        #해결해야 함
        total_score += factor_score
    return (product_info[0], total_score)

        



data = pd.read_csv("data/sample_product.csv")
print(data)
user_input = [1, 3, 2, 5, 6, 4]
#웹이나 앱을 통해 유저 입력 받을 예정

weight_list = []
for factor in data.columns[1:]:
    corel = np.corrcoef(data[factor], user_input)
    weight_list.append(corel[0][1])

new_product = ["new", 8, 3, 2000]
#프로토타입용으로 임의의 새로운 상품 정보를 설정했음
#그 다음 단계에서 데이터셋으로 바꿀 예정

score = cal_score(new_product, weight_list)
print(weight_list)