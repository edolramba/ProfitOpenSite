import streamlit as st
import pandas as pd
from datetime import datetime, timezone
import os
import json
import altair as alt
import glob

# ✅ 최신 JSON 파일 자동 탐색 (파일명 앞에 날짜가 붙는 경우)
json_candidates = glob.glob("*automatedTrading.dj00Trading.json")
if not json_candidates:
    st.error("❌ 자동 저장된 JSON 파일이 없습니다.")
    st.stop()

# 가장 최신 파일 선택
json_file_path = max(json_candidates, key=os.path.getctime)
st.info(f"📄 불러온 파일: `{os.path.basename(json_file_path)}`")

# ✅ JSON 파일 읽기
with open(json_file_path, "r", encoding="utf-8") as f:
    try:
        data = json.load(f)
    except json.JSONDecodeError:
        st.error("❌ JSON 파일 형식이 잘못되었습니다.")
        st.stop()

# ✅ 데이터 파싱
rows = []
for d in data:
    try:
        buy = d.get("buy_price") or 0
        sell = d.get("sell_price") or 0
        qty = d.get("filled_quantity") or 0
        if not (buy and sell and qty):
            continue

        profit = (sell - buy) * qty
        rate = ((sell - buy) / buy) * 100 if buy else 0
        order_time = d.get("order_time")

        # ✅ order_time 처리
        if isinstance(order_time, dict) and "$date" in order_time:
            order_time = datetime.fromisoformat(order_time["$date"].replace("Z", ""))
        elif isinstance(order_time, str):
            order_time = datetime.fromisoformat(order_time.replace("Z", ""))
        else:
            continue

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

# ✅ 유효한 데이터가 없으면 종료
if not rows:
    st.error("✅ 매매 완료된 내역이 없습니다.")
    st.stop()

df = pd.DataFrame(rows).sort_values(by="매수일", ascending=True)

# ✅ 2024-10-30 이후의 데이터만 분석
start_date = datetime(2024, 10, 30)
df = df[df["매수일"] > start_date.date()]

# ✅ 유효한 데이터가 없으면 종료
if df.empty:
    st.error("✅ 매매 완료된 내역이 없습니다.")
    st.stop()

end_date = df["매수일"].max()
duration_days = (end_date - start_date.date()).days + 1

# ✅ 누적 수익 계산
df["누적수익"] = df["수익금(원)"].cumsum()

# ✅ 총계 계산
total_invest = sum(df["매수가"] * df["수량"])
average_invest = total_invest / len(df)
total_profit = df["수익금(원)"].sum()
total_rate = (total_profit / average_invest * 100) if average_invest else 0

# ✅ UI 출력
st.title("📈 Raorke Bot Performance Report")

st.subheader("💰 Cumulative Summary")
st.markdown(f"**Investment Period**: {start_date.date()} ~ {end_date} ({duration_days}일)")
st.markdown(f"**Average Investment per Trade**: {average_invest:,.0f}원")
st.markdown(f"**Total Profit**: {total_profit:,.0f}원")
st.markdown(f"**Total Return**: {total_rate:.2f}%")

st.subheader("📉 Profit Trend Over Time")
chart = alt.Chart(df).mark_line(point=True).encode(
    x="매수일:T",
    y="누적수익:Q",
    tooltip=["매수일", "누적수익"]
).properties(
    width="container",
    height=400
)
st.altair_chart(chart, use_container_width=True)

st.subheader("📋 Trade History (Latest First)")
sorted_df = df.sort_values(by="매수일", ascending=False)
st.dataframe(sorted_df, use_container_width=True)
