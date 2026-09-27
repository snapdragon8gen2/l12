import streamlit as st
import random
def draw_omikuji():
    fortune = random.choice(["大ミク","中ミク","小ミク","凶"])
    if fortune == "大ミク":st.balloons(); st.success("ミクは2007年に誕生し電子の歌姫ってよなれたんだ！")
    elif fortune == "中ミク":st.balloons(); st.success("adoがデビュー前によく聞いていた曲はボーカロイド通称ボカロなんだ！")
    elif fortune == "小ミク":st.balloons(); st.success("ミクのデビュー曲は01_balladeなんだ！")
    else: st.error("今日はミクを拝もう")
st.title("今日のミクミク占い")

if st.button("ミクくじを引く"):
    draw_omikuji()  
