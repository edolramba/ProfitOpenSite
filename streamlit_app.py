import streamlit as st
import pandas as pd
from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv
import altair as alt

# .env 불러오기
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]

# 매매 완료된 내역 전체 조회
query = {
    "buy_chk": "Y",
    "sell_chk": "Y",
    "buy_price": {"$ne": None},
    "sell_price": {"$ne": None},
    "order_time": {"$gt": datetime(2024, 10, 30)}
}

data = list(collection.find(query))

rows = []
for d in data:
    try:
        buy = d.get("buy_price", 0)
        sell = d.get("sell_price", 0)
        qty = d.get("filled_quantity", 0)
        profit = (sell - buy) * qty
        rate = ((sell - buy) / buy) * 100 if buy else 0
        order_time = d.get("order_time", datetime.min)

        # ISO 포맷 문자열로 들어온 경우 처리
        if isinstance(order_time, dict) and "$date" in order_time:
            order_time = datetime.fromisoformat(order_time["$date"].replace("Z", "+00:00"))
        elif isinstance(order_time, str):
            order_time = datetime.fromisoformat(order_time)

        rows.append({
            "종목명": d.get("stock_name", ""),
            "매수가": buy,
            "매도가": sell,
            "수익률(%)": round(rate, 2),
            "수익금(원)": profit,
            "수량": qty,
            "매수일": order_time.date()
        })
    except Exception as e:
        print(f"Error parsing document: {e}")

if not rows:
    st.error("✅ 매매 완료된 내역이 없습니다.")
    st.stop()

df = pd.DataFrame(rows).sort_values(by="매수일", ascending=True)

# 기준 시작일 명시
start_date = datetime(2024, 10, 30)

# 실제 종료일은 데이터 기준
end_date = df["매수일"].max()

# 투자 기간 (일 수)
duration_days = (end_date - start_date).days + 1  # 시작일 포함

# 문자열로 포맷팅
start_str = start_date.strftime("%Y-%m-%d")
end_str = end_date.strftime("%Y-%m-%d")

# 📊 누적 수익 추이 계산
df["누적수익"] = df["수익금(원)"].cumsum()

# 💰 총계 계산
total_invest = sum(df["매수가"] * df["수량"])
average_invest = total_invest / len(df)

total_profit = df["수익금(원)"].sum()
total_rate = (total_profit / average_invest * 100) if average_invest else 0

# 🖥️ Streamlit UI 출력
st.title("📈 라오르케봇 수익률 공개")

st.subheader("💰 누적 성과 요약")
st.markdown(f"**투자 기간**: {start_str} ~ {end_str} ({duration_days}일)")
st.markdown(f"**1회 평균 투자금**: {average_invest:,.0f}원")
st.markdown(f"**총 수익금**: {total_profit:,.0f}원")
st.markdown(f"**총 수익률**: {total_rate:.2f}%")

st.subheader("📉 누적 수익 추이")
chart = alt.Chart(df).mark_line(point=True).encode(
    x="매수일:T",
    y="누적수익:Q",
    tooltip=["매수일", "누적수익"]
).properties(
    width="container",
    height=400
)
st.altair_chart(chart, use_container_width=True)

sorted_df = df.sort_values(by="매수일", ascending=False)
st.subheader("📋 매매 내역 (최근 매수일 순)")
st.dataframe(sorted_df, use_container_width=True)

# 주석으로 감별