import streamlit as st

# 페이지 설정
st.set_page_config(page_title="Play - AI Voice", layout="wide", initial_sidebar_state="collapsed")

# CSS 스타일
st.markdown("""
<style>
    /* 전체 배경 */
    .stApp {
        background-color: #1a1a1a;
        color: #ffffff;
    }
    
    /* 사이드바 스타일 */
    [data-testid="stSidebar"] {
        background-color: #0d0d0d;
        padding-top: 20px;
    }
    
    [data-testid="stSidebar"] .stButton button {
        width: 100%;
        background-color: transparent;
        color: #999999;
        border: none;
        text-align: left;
        padding: 15px 20px;
        border-radius: 0;
    }
    
    [data-testid="stSidebar"] .stButton button:hover {
        background-color: #2a2a2a;
        color: #ffffff;
    }
    
    /* 상단 헤더 */
    .top-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 15px 40px;
        background-color: #0d0d0d;
        border-bottom: 1px solid #2a2a2a;
    }
    
    .logo {
        font-size: 24px;
        font-weight: bold;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    
    .credits {
        display: flex;
        align-items: center;
        gap: 10px;
        background-color: #2a2a2a;
        padding: 8px 16px;
        border-radius: 20px;
        font-size: 14px;
    }
    
    /* 메인 배너 */
    .hero-banner {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #7e22ce 100%);
        padding: 60px 40px;
        text-align: center;
        margin: 0;
        position: relative;
        overflow: hidden;
    }
    
    .hero-banner::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 120"><path d="M0,0 Q300,60 600,30 T1200,60 L1200,120 L0,120 Z" fill="rgba(255,255,255,0.1)"/></svg>') no-repeat bottom;
        background-size: cover;
    }
    
    .hero-content {
        position: relative;
        z-index: 1;
    }
    
    .hero-banner h1 {
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 15px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .hero-banner p {
        font-size: 18px;
        color: #e0e0e0;
        margin-bottom: 30px;
    }
    
    .character-images {
        display: flex;
        justify-content: center;
        gap: 30px;
        margin-top: 30px;
    }
    
    .character-card {
        text-align: center;
    }
    
    .character-avatar {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        margin: 0 auto 10px;
        border: 3px solid #ffffff;
    }
    
    /* 음성 입력 섹션 */
    .voice-input-section {
        background-color: #2a2a2a;
        padding: 40px;
        margin: 40px;
        border-radius: 20px;
    }
    
    .voice-input-section h2 {
        font-size: 28px;
        margin-bottom: 30px;
    }
    
    .voice-input-box {
        background-color: #1a1a1a;
        padding: 30px;
        border-radius: 15px;
        border: 2px solid #3a3a3a;
        display: flex;
        align-items: center;
        gap: 20px;
        cursor: pointer;
        transition: all 0.3s;
    }
    
    .voice-input-box:hover {
        border-color: #667eea;
        background-color: #222222;
    }
    
    .mic-icon {
        font-size: 32px;
        color: #4ade80;
    }
    
    /* 보이스 카테고리 */
    .category-section {
        padding: 40px;
    }
    
    .category-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }
    
    .category-tabs {
        display: flex;
        gap: 10px;
        overflow-x: auto;
        padding: 10px 0;
    }
    
    .category-tab {
        background-color: #2a2a2a;
        color: #999999;
        padding: 10px 20px;
        border-radius: 25px;
        border: none;
        cursor: pointer;
        white-space: nowrap;
        transition: all 0.3s;
        font-size: 14px;
    }
    
    .category-tab:hover {
        background-color: #3a3a3a;
        color: #ffffff;
    }
    
    .category-tab.active {
        background-color: #667eea;
        color: #ffffff;
    }
    
    /* 보이스 카드 */
    .voice-cards {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
        gap: 20px;
        margin-top: 20px;
    }
    
    .voice-card {
        background-color: #2a2a2a;
        border-radius: 15px;
        padding: 20px;
        cursor: pointer;
        transition: all 0.3s;
        border: 2px solid transparent;
    }
    
    .voice-card:hover {
        transform: translateY(-5px);
        border-color: #667eea;
        box-shadow: 0 10px 30px rgba(102, 126, 234, 0.3);
    }
    
    .voice-card-header {
        display: flex;
        align-items: center;
        gap: 15px;
        margin-bottom: 15px;
    }
    
    .voice-avatar {
        width: 50px;
        height: 50px;
        border-radius: 50%;
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    }
    
    .voice-name {
        font-size: 16px;
        font-weight: bold;
    }
    
    .voice-description {
        font-size: 14px;
        color: #cccccc;
        line-height: 1.5;
        margin-bottom: 15px;
    }
    
    .voice-actions {
        display: flex;
        justify-content: flex-end;
        gap: 10px;
    }
    
    .action-btn {
        background-color: #3a3a3a;
        border: none;
        padding: 8px 12px;
        border-radius: 50%;
        color: #ffffff;
        cursor: pointer;
        transition: all 0.3s;
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .action-btn:hover {
        background-color: #667eea;
        transform: scale(1.1);
    }
    
    /* 언어 선택 */
    .language-selector {
        background-color: #2a2a2a;
        border: 1px solid #3a3a3a;
        color: #ffffff;
        padding: 8px 16px;
        border-radius: 20px;
        cursor: pointer;
    }
    
    /* 숨기기 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 사이드바
with st.sidebar:
    st.markdown("### 🏠 Home")
    st.button("Home", key="nav_home")
    st.markdown("### 📦 Projects")
    st.button("Projects", key="nav_projects")
    st.markdown("### 🎁 Rewards")
    st.button("Rewards", key="nav_rewards")
    st.markdown("### 💳 Subscription")
    st.button("Subscription", key="nav_sub")
    st.markdown("---")
    st.markdown("### 🎤 Voice Cloning")
    st.button("Voice Cloning", key="nav_voice")
    st.markdown("### 🔌 API")
    st.button("API", key="nav_api")
    st.markdown("### ❓ Help")
    st.button("Help", key="nav_help")

# 상단 헤더
st.markdown("""
<div class="top-header">
    <div class="logo">
        <span>▶</span> Play
    </div>
    <div class="credits">
        <span>🪙</span>
        <strong>2,689 Credits</strong>
    </div>
</div>
""", unsafe_allow_html=True)

# 히어로 배너
st.markdown("""
<div class="hero-banner">
    <div class="hero-content">
        <h1>✨ 꿀🍯보이스 테포, 경재헌 성우님 Play에 등장! ✨</h1>
        <p>정제된 성우님과 함께하는 특별 콘텐츠에 지금 도전하세요!</p>
        <div class="character-images">
            <div class="character-card">
                <div class="character-avatar" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);"></div>
                <div>Dudumchi</div>
            </div>
            <div class="character-card">
                <div class="character-avatar" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);"></div>
                <div>Dohyun</div>
            </div>
            <div class="character-card">
                <div class="character-avatar" style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);"></div>
                <div>Jinha</div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 음성 입력 섹션
st.markdown("""
<div class="voice-input-section">
    <h2>나만의 글로벌 보이스 만들기</h2>
    <div class="voice-input-box">
        <span class="mic-icon">🎤</span>
        <span style="font-size: 16px; color: #cccccc;">내 목소리로 다양한 음성 파일을 생성해보세요</span>
    </div>
</div>
""", unsafe_allow_html=True)

# 카테고리 섹션
st.markdown("""
<div class="category-section">
    <div class="category-header">
        <h2>내가 쓴 대사의 다양한 보이스를 들어보세요!</h2>
        <select class="language-selector">
            <option>한국어 ▼</option>
            <option>English</option>
            <option>日本語</option>
        </select>
    </div>
</div>
""", unsafe_allow_html=True)

# 카테고리 탭
categories = ["신규", "추천", "게임", "스토리텔링", "연기", "밈", "다큐멘터리", "오디오북", 
              "나레이션", "비즈니스", "호러", "광고", "공지", "교육", "뉴스", "대화", "리뷰", "엔터테인먼트"]

cols = st.columns(len(categories[:6]))
for i, cat in enumerate(categories[:6]):
    with cols[i]:
        if st.button(cat, key=f"cat_{cat}"):
            pass

# 보이스 카드 데이터
voices = [
    {
        "name": "Ppang BuJang",
        "description": "안녕하세요, 농심의 뽕부장입니다. 제가 연구해서 만든 소금빵, 초코빵 많이 사랑해주세요~",
        "avatar_gradient": "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)"
    },
    {
        "name": "Melong",
        "description": "먹어도 먹어도 배고프걸 어떡하면 좋지? 빨리 냥장고를 체워줘!!",
        "avatar_gradient": "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)"
    },
    {
        "name": "Dudumchi",
        "description": "안냥! 전 세계의 무대를 책임질 슈퍼스타, 두둠치야! 날 만나다니, 넌 정말 행운아구나~",
        "avatar_gradient": "linear-gradient(135deg, #fa709a 0%, #fee140 100%)"
    },
    {
        "name": "Cherry",
        "description": "체리는 달콤한 요정이에요! 함께 즐거운 하루를 보내요~ 🍒",
        "avatar_gradient": "linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%)"
    }
]

# 보이스 카드 표시
cols = st.columns(2)
for idx, voice in enumerate(voices):
    with cols[idx % 2]:
        st.markdown(f"""
        <div class="voice-card">
            <div class="voice-card-header">
                <div class="voice-avatar" style="background: {voice['avatar_gradient']};"></div>
                <div class="voice-name">{voice['name']}</div>
            </div>
            <div class="voice-description">{voice['description']}</div>
            <div class="voice-actions">
                <button class="action-btn">✏️</button>
                <button class="action-btn">➕</button>
            </div>
        </div>
        """, unsafe_allow_html=True)
