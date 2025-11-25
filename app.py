import streamlit as st
import random
import time


def judge_janken(user_hand: str, ai_hand: str) -> str:
    """Return the result of a rock-paper-scissors game for given hands."""
    hands = {"グー": 0, "チョキ": 1, "パー": 2}
    if user_hand == ai_hand:
        return "引き分け"
    if (hands[user_hand] - hands[ai_hand]) % 3 == 1:
        return "あなたの勝ち！"
    return "あなたの負け！"


def janken_tab() -> None:
    """Janken (rock-paper-scissors) game tab."""
    st.header("じゃんけんゲーム")
    st.write("ボタンを押すと自分と相手の手をランダムに選び、勝敗を表示します。")

    hands = ["グー", "チョキ", "パー"]
    if st.button("じゃんけん！", key="janken_btn"):
        user_hand = random.choice(hands)
        ai_hand = random.choice(hands)
        result = judge_janken(user_hand, ai_hand)
        st.write(f"あなた: {user_hand} ／ 相手: {ai_hand}")
        st.success(result)


def number_guess_tab() -> None:
    """Number guessing game tab."""
    st.header("数字当てゲーム")
    st.write("コンピュータが 1〜100 の中から選んだ数字を予想しましょう。ヒントが表示されます。")

    # Initialize target number and guess count in session state
    if 'target_number' not in st.session_state:
        st.session_state.target_number = random.randint(1, 100)
        st.session_state.guess_count = 0
    
    # User input for guessing
    guess = st.number_input(
        "1〜100 の数字を入力して予想してください",
        min_value=1,
        max_value=100,
        step=1,
        key="guess_input",
    )
    
    if st.button("予想する", key="guess_btn"):
        st.session_state.guess_count += 1
        target = st.session_state.target_number
        if guess < target:
            st.info("もっと大きいです。")
        elif guess > target:
            st.info("もっと小さいです。")
        else:
            st.success(f"正解です！ {st.session_state.guess_count} 回目で当たりました。")
    
    if st.button("新しいゲーム", key="new_game_btn"):
        st.session_state.target_number = random.randint(1, 100)
        st.session_state.guess_count = 0
        st.info("新しい数字を選びました。再挑戦してください。")


def timer_tab() -> None:
    """Simple timer tab for counting down seconds."""
    st.header("タイマー")
    st.write("任意の秒数を設定してカウントダウンを開始します。")

    seconds = st.number_input(
        "タイマー（秒）を入力してください",
        min_value=1,
        value=5,
        step=1,
        key="timer_seconds_input",
    )
    placeholder = st.empty()
    
    if st.button("タイマー開始", key="timer_start_btn"):
        for remaining in range(int(seconds), 0, -1):
            placeholder.metric("残り時間", f"{remaining} 秒")
            time.sleep(1)
        placeholder.success("タイムアップ！")


def main():
    """Entry point for the mini games box."""
    st.title("ミニゲーム3本セット（箱）")
    st.write("じゃんけん、数字当て、タイマーを一つのアプリで楽しめます。")

    tab_labels = ["じゃんけん", "数字当てゲーム", "タイマー"]
    tabs = st.tabs(tab_labels)
    
    with tabs[0]:
        janken_tab()
    
    with tabs[1]:
        number_guess_tab()
    
    with tabs[2]:
        timer_tab()


if __name__ == "__main__":
    main()