import pandas as pd
import numpy as np
import csv

def cal_score(product_info, weight_list):
    total_score = 0
    for idx in range(1, 3):
        factor_score = product_info[idx] * weight_list[idx]
        #요소 값에 그대로 가중치를 곱하니 단위가 큰 가격 요소가 가장 많이 반영됨
        #해결해야 함
        total_score += factor_score
    return total_score

data = pd.read_csv("data/sample_product.csv")
user_input = list(map(int,input("상품의 선호 순위를 입력해주십시오").split()))
# user_input = [3, 7, 4, 2, 5, 6]
#웹이나 앱을 통해 유저 입력 받을 예정

weight_list = []
for factor in data.columns[1:]:
    corel = np.corrcoef(data[factor], user_input)
    weight_list.append(corel[0][1])

#프로토타입용으로 임의의 새로운 상품 정보를 설정했음
#그 다음 단계에서 데이터셋으로 바꿀 예정

user_search = input("검색하려는 상품을 입력해주세요")

f = open('data/processed_data.csv','r')
rdr = csv.reader(f)
rdr = list(rdr)

product_list = []
for row in rdr[1:]:
    if user_search in row[1]:
        product_list.append(row)

product_df = pd.DataFrame(product_list, columns=rdr[0])

score_df = product_df[["Commodity", "co2", "organic", "Average", "score"]]

for idx, row in score_df.iterrows():
    row["score"] = cal_score((int(row["co2"]), int(row["organic"]), float(row["Average"])), weight_list)

score_df = score_df.sort_values(by=["score"], ascending= False)


print("당신의 추천 아이템은")
print("===============================")
print(score_df.head())
print("===============================")