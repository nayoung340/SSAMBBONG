import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import koreanize-matplotlib

import pandas as pd

# CSV 파일 경로
file_path = '/mnt/data/202406_202406_연령별인구현황_월간.csv'

# 데이터 읽기
data = pd.read_csv(file_path, encoding='cp949')  # 한국어 인코딩 (euc-kr 또는 cp949)로 읽기

# 데이터 확인
data.head()


# 데이터 파일 경로
file_path = '/mnt/data/202406_202406_연령별인구현황_월간.csv'

# 데이터 불러오기
@st.cache
def load_data():
    data = pd.read_csv(file_path, encoding='cp949')
    return data

data = load_data()

# 지역 선택
regions = data['지역명'].unique()
selected_region = st.selectbox('지역을 선택하세요:', regions)

# 선택한 지역의 데이터 필터링
region_data = data[data['지역명'] == selected_region]

# 중학생 인구 비율 계산 (예: 13세~15세)
total_population = region_data['총인구수'].sum()
middle_school_population = region_data[['13세', '14세', '15세']].sum().sum()
middle_school_ratio = (middle_school_population / total_population) * 100

# 원 그래프 그리기
labels = ['중학생 인구 비율', '기타 인구 비율']
sizes = [middle_school_ratio, 100 - middle_school_ratio]
colors = ['#ff9999','#66b3ff']
explode = (0.1, 0)  # 중학생 인구 비율 부분을 강조

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

st.pyplot(fig1)
