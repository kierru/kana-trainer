import streamlit as st
import random
import time

# ================== KANA DATA ==================
HIRAGANA = {
    "あ":"a","い":"i","う":"u","え":"e","お":"o",
    "か":"ka","き":"ki","く":"ku","け":"ke","こ":"ko",
    "さ":"sa","し":"shi","す":"su","せ":"se","そ":"so",
    "た":"ta","ち":"chi","つ":"tsu","て":"te","と":"to",
    "な":"na","に":"ni","ぬ":"nu","ね":"ne","の":"no",
    "は":"ha","ひ":"hi","ふ":"fu","へ":"he","ほ":"ho",
    "ま":"ma","み":"mi","む":"mu","め":"me","も":"mo",
    "や":"ya","ゆ":"yu","よ":"yo",
    "ら":"ra","り":"ri","る":"ru","れ":"re","ろ":"ro",
    "わ":"wa","を":"wo","ん":"n",
}

KATAKANA = {
    "ア":"a","イ":"i","ウ":"u","エ":"e","オ":"o",
    "カ":"ka","キ":"ki","ク":"ku","ケ":"ke","コ":"ko",
    "サ":"sa","シ":"shi","ス":"su","セ":"se","ソ":"so",
    "タ":"ta","チ":"chi","ツ":"tsu","テ":"te","ト":"to",
    "ナ":"na","ニ":"ni","ヌ":"nu","ネ":"ne","ノ":"no",
    "ハ":"ha","ヒ":"hi","フ":"fu","ヘ":"he","ホ":"ho",
    "マ":"ma","ミ":"mi","ム":"mu","メ":"me","モ":"mo",
    "ヤ":"ya","ユ":"yu","ヨ":"yo",
    "ラ":"ra","リ":"ri","ル":"ru","レ":"re","ロ":"ro",
    "ワ":"wa","ヲ":"wo","ン":"n",
}

HIRAGANA_DAKUON = {
    "が":"ga","ぎ":"gi","ぐ":"gu","げ":"ge","ご":"go",
    "ざ":"za","じ":"ji","ず":"zu","ぜ":"ze","ぞ":"zo",
    "だ":"da","ぢ":"ji","づ":"zu","で":"de","ど":"do",
    "ば":"ba","び":"bi","ぶ":"bu","べ":"be","ぼ":"bo",
    "ぱ":"pa","ぴ":"pi","ぷ":"pu","ぺ":"pe","ぽ":"po",
}

KATAKANA_DAKUON = {
    "ガ":"ga","ギ":"gi","グ":"gu","ゲ":"ge","ゴ":"go",
    "ザ":"za","ジ":"ji","ズ":"zu","ゼ":"ze","ゾ":"zo",
    "ダ":"da","ヂ":"ji","ヅ":"zu","デ":"de","ド":"do",
    "バ":"ba","ビ":"bi","ブ":"bu","ベ":"be","ボ":"bo",
    "パ":"pa","ピ":"pi","プ":"pu","ペ":"pe","ポ":"po",
}

HIRAGANA_COMBO = {
    "きゃ":"kya","きゅ":"kyu","きょ":"kyo",
    "しゃ":"sha","しゅ":"shu","しょ":"sho",
    "ちゃ":"cha","ちゅ":"chu","ちょ":"cho",
    "にゃ":"nya","にゅ":"nyu","にょ":"nyo",
    "ひゃ":"hya","ひゅ":"hyu","ひょ":"hyo",
    "みゃ":"mya","みゅ":"myu","みょ":"myo",
    "りゃ":"rya","りゅ":"ryu","りょ":"ryo",
    "ぎゃ":"gya","ぎゅ":"gyu","ぎょ":"gyo",
    "じゃ":"ja","じゅ":"ju","じょ":"jo",
    "びゃ":"bya","びゅ":"byu","びょ":"byo",
    "ぴゃ":"pya","ぴゅ":"pyu","ぴょ":"pyo",
}


KATAKANA_COMBO = {
    "キャ":"kya","キュ":"kyu","キョ":"kyo",
    "シャ":"sha","シュ":"shu","ショ":"sho",
    "チャ":"cha","チュ":"chu","チョ":"cho",
    "ニャ":"nya","ニュ":"nyu","ニョ":"nyo",
    "ヒャ":"hya","ヒュ":"hyu","ヒョ":"hyo",
    "ミャ":"mya","ミュ":"myu","ミョ":"myo",
    "リャ":"rya","リュ":"ryu","リョ":"ryo",
    "ギャ":"gya","ギュ":"gyu","ギョ":"gyo",
    "ジャ":"ja","ジュ":"ju","ジョ":"jo",
    "ビャ":"bya","ビュ":"byu","ビョ":"byo",
    "ピャ":"pya","ピュ":"pyu","ピョ":"pyo",
}


LOANWORDS = {
    "ファ":"fa","フィ":"fi","フェ":"fe","フォ":"fo",
    "ティ":"ti","ディ":"di",
    "チェ":"che",
    "シェ":"she","ジェ":"je",
    "ウィ":"wi","ウェ":"we","ウォ":"wo",
    "ヴァ":"va","ヴィ":"vi","ヴェ":"ve","ヴォ":"vo",
}

MODES = {
    "Hiragana": HIRAGANA,
    "Katakana": KATAKANA,
    "Hira Dakuon": HIRAGANA_DAKUON,
    "Kata Dakuon": KATAKANA_DAKUON,
    "Hira Combo": HIRAGANA_COMBO,
    "Kata Combo": KATAKANA_COMBO,
    "Loanwords": LOANWORDS,
    "All": {
        **HIRAGANA, **KATAKANA,
        **HIRAGANA_DAKUON, **KATAKANA_DAKUON,
        **HIRAGANA_COMBO, **KATAKANA_COMBO,
        **LOANWORDS
    }
}

# ================== HELPERS ==================
def kana_type(k):
    for c in k:
        if "\u30a0" <= c <= "\u30ff":
            return "Katakana"
    return "Hiragana"

# ================== PAGE ==================
st.set_page_config(page_title="Kana Trainer", layout="centered")

# ================== STYLE FIX ==================
st.markdown("""
<style>
.card {
    border: 2px solid #444;
    border-radius: 14px;
    padding: 28px;
    height: 155px;

    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;

    text-align: center;
}

.kana-main {
    display: block;
    font-size: 64px;
    line-height: 1;
    transform: translateY(-4px);
}

.kana-label {
    display: block;
    font-size: 20px;
    opacity: 0.6;
    margin-top: 6px;
}

/* FIX: disable browser memory */
input {
    autocomplete: off !important;
}
</style>
""", unsafe_allow_html=True)


st.title("Kana Trainer")

# ================== SESSION INIT ==================
if "started" not in st.session_state:
    st.session_state.started = False
    st.session_state.index = 0
    st.session_state.score = 0
    st.session_state.total = 0
    st.session_state.kana_items = []
    st.session_state.current = None
    st.session_state.feedback = ""
    st.session_state.mode = ""
    st.session_state.input_key = 0   # FIX

# ================== START ==================
if not st.session_state.started:
    mode = st.selectbox("Mode", list(MODES.keys()))
    total = st.number_input("Number of Questions", 1, 200, 20)

    if st.button("Start"):
        st.session_state.started = True
        st.session_state.mode = mode
        st.session_state.total = total
        st.session_state.kana_items = list(MODES[mode].items())
        st.session_state.index = 0
        st.session_state.score = 0
        st.session_state.current = random.choice(st.session_state.kana_items)
        st.session_state.feedback = ""
        st.session_state.input_key += 1  # FIX
        st.rerun()

# ================== QUIZ ==================
else:
    if st.session_state.index >= st.session_state.total:
        st.success(f"Finished! Score: {st.session_state.score}/{st.session_state.total}")
        if st.button("Restart"):
            st.session_state.started = False
            st.rerun()
    else:
        k, a = st.session_state.current

        st.caption(f"Question {st.session_state.index + 1} / {st.session_state.total}")

        col_left, col_right = st.columns([2, 1])

        # ---------- LEFT: KANA ----------
        with col_left:

            label_html = ""
            if st.session_state.mode == "All":
                label_html = f"<div class='kana-label'>{kana_type(k)}</div>"

            st.markdown(
                f"""
                <div class='card'>
                    <div class='kana-main'>{k}</div>
                    {label_html}
                </div>
                """,
                unsafe_allow_html=True
            )

        # ---------- RIGHT: INPUT / FEEDBACK ----------
        with col_right:

            # ===== STATE 1: ANSWERING =====
            if not st.session_state.feedback:
                with st.form("answer_form"):
                    answer = st.text_input(
                        "Romaji",
                        key=f"answer_{st.session_state.input_key}",  # FIX
                        autocomplete="off"                           # FIX
                    )
                    submit = st.form_submit_button("Submit")

                if submit:
                    if answer.strip().lower() == a:
                        st.session_state.score += 1
                        st.session_state.feedback = "✔ Correct"
                    else:
                        st.session_state.feedback = f"✘ Correct: {a}"

                    st.session_state.input_key += 1  # FIX
                    st.rerun()

            # ===== STATE 2: FEEDBACK =====
            else:
                st.info(st.session_state.feedback)

                time.sleep(1)

                st.session_state.index += 1
                st.session_state.current = random.choice(st.session_state.kana_items)
                st.session_state.feedback = ""
                st.session_state.input_key += 1

                st.rerun()
