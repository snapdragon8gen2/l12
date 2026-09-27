import streamlit as st
import random
def draw_omikuji():
    fortune = random.choice(["大吉","中吉","小吉","区"])
    if fortune == "大ミク":st.balloons(); st.success("運がいいねcatch the waveをきこう！")
    elif fortune == "中ミク":st.balloons(); st.success("いいね！プロセカを始めよう！")
    elif fortune == "小ミク":st.balloons(); st.success("ちょっとわるいねー熱風を聞いて元気になろう！")
    else: st.error("今日はミクを拝もう")
st.title("今日のミクミク占い")

if st.button("ミクくじを引く"):
    draw_omikuji()  
