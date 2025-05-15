import streamlit as st
import pandas as pd
import pydeck as pdk

# CSV 데이터 로드
DATA_PATH = "0512 oss/KC_CLTUR_SAFE_MAP_INFO_2024.csv"
data = pd.read_csv(DATA_PATH)

st.title("2024년도 교통사고 데이터")

# 지역 필터링 선택 박스
regions = data['SIGNGU_NM'].str.split(' ').str[0].unique()

# 사이드바 지역 필터링 박스
selected_region = st.sidebar.selectbox("지역을 선택하세요:", options=regions)

# 선택된 지역 데이터 필터링
filtered_data = data[data['SIGNGU_NM'].str.startswith(selected_region)]

# 상세주소별 사고 수 계
filtered_data['상세주소'] = filtered_data['SIGNGU_NM'].str.split(' ').str[1]

# 지도
layer = pdk.Layer(
    "ScatterplotLayer",
    data=filtered_data,
    get_position="[FCLTY_LO, FCLTY_LA]",
    get_radius=100,
    get_fill_color="[255, 0, 0, 160]",
    pickable=True
)
view_state = pdk.ViewState(
    latitude=filtered_data['FCLTY_LA'].mean(),
    longitude=filtered_data['FCLTY_LO'].mean(),
    zoom=11,
    pitch=50
)

chart_options = ['사고건수', '사상자수', '중상자수', '경상자수', '사망자수', '종합']

# 사이드바 차트 필터링
selected_chart_option = st.sidebar.selectbox("차트에 표시할 데이터를 선택하세요:", options=chart_options)

# 차트 필터링
column_mapping = {
    '사고건수': 'ACDNT_CAS_CO',
    '사상자수': 'CASLT_CO',
    '중상자수': 'SWPSN_CO',
    '경상자수': 'SINJPSN_CO',
    '사망자수': 'DEATH_CO'
}
selected_column = column_mapping.get(selected_chart_option)

if selected_chart_option == '종합':
    address_counts = filtered_data.groupby('상세주소').agg({
        'ACDNT_CAS_CO': 'sum',
        'CASLT_CO': 'sum',
        'SWPSN_CO': 'sum',
        'SINJPSN_CO': 'sum',
        'DEATH_CO': 'sum',
        'FCLTY_LA': 'mean',
        'FCLTY_LO': 'mean'
    }).reset_index()
else:
    address_counts = filtered_data.groupby('상세주소').agg({
        selected_column: 'sum',
        'FCLTY_LA': 'mean',
        'FCLTY_LO': 'mean'
    }).reset_index()
    address_counts.rename(columns={selected_column: selected_chart_option}, inplace=True)

# 지도 위에 그래프 추가
if selected_chart_option == '종합':
    address_counts.rename(columns={
        'ACDNT_CAS_CO': '사고건수',
        'CASLT_CO': '사상자수',
        'SWPSN_CO': '중상자수',
        'SINJPSN_CO': '경상자수',
        'DEATH_CO': '사망자수'
    }, inplace=True)

    layers = []
    color_mapping = {
        '사고건수': [255, 0, 0, 255],  # 빨강
        '사상자수': [0, 255, 0, 255],  # 초록
        '중상자수': [0, 0, 255, 255],  # 파랑
        '경상자수': [255, 255, 0, 255],  # 노랑
        '사망자수': [255, 0, 255, 255]   # 보라
    }

    for metric, color in color_mapping.items():
        layers.append(
            pdk.Layer(
                "ColumnLayer",
                data=address_counts,
                get_position="[FCLTY_LO, FCLTY_LA]",
                get_elevation=metric,
                elevation_scale=10,
                radius=200,
                get_fill_color=color,
                pickable=True,
            )
        )
else:
    layers = [
        pdk.Layer(
            "ColumnLayer",
            data=address_counts[['FCLTY_LO', 'FCLTY_LA', selected_chart_option]],
            get_position="[FCLTY_LO, FCLTY_LA]",
            get_elevation=selected_chart_option,
            elevation_scale=10,
            radius=200,
            get_fill_color="[255, 165, 0, 255]", 
            pickable=True,
        )
    ]

# 차트 데이터 생성
if selected_chart_option == '종합':
    address_counts.rename(columns={
        'ACDNT_CAS_CO': '사고건수',
        'CASLT_CO': '사상자수',
        'SWPSN_CO': '중상자수',
        'SINJPSN_CO': '경상자수',
        'DEATH_CO': '사망자수'
    }, inplace=True)
    chart_data = address_counts[['상세주소', '사고건수', '사상자수', '중상자수', '경상자수', '사망자수']]
    chart_data = chart_data.set_index('상세주소')
else:
    chart_data = address_counts[['상세주소', selected_chart_option]].set_index('상세주소')

#부제목
st.subheader(f"{selected_region} 지역별 {selected_chart_option}")

# 차트표시
st.bar_chart(chart_data)

# 상위 3곳 데이터 추출
if selected_chart_option == '종합':
    top_3 = chart_data.sum(axis=1).nlargest(3).reset_index()
    top_3.columns = ['지역', '총합']
else:
    top_3 = chart_data.nlargest(3, selected_chart_option).reset_index()
    top_3.columns = ['지역', selected_chart_option]

# 상위 3곳 데이터 표시
st.subheader("상위 3지역")
st.table(top_3)

# 지도표시
st.pydeck_chart(pdk.Deck(layers=layers, initial_view_state=view_state))
