import streamlit as st

# 페이지 설정
st.set_page_config(page_title="포스타입 오리지널", layout="wide", initial_sidebar_state="collapsed")

# CSS 스타일
st.markdown("""
<style>
    /* 전체 배경 */
    .stApp {
        background-color: #000000;
        color: #ffffff;
    }
    
    /* 헤더 스타일 */
    .header-container {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 20px 40px;
        background-color: #000000;
    }
    
    /* 배너 그라디언트 */
    .banner {
        height: 200px;
        background: linear-gradient(to right, #ff9a9e 0%, #fecfef 25%, #5b9cf5 50%, #4ecde4 75%, #6dd5ed 100%);
        border-radius: 15px;
        margin: 20px 40px;
    }
    
    /* 프로필 섹션 */
    .profile-section {
        padding: 40px;
        display: flex;
        gap: 30px;
        align-items: flex-start;
    }
    
    .profile-image {
        width: 120px;
        height: 120px;
        background-color: #ffffff;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 48px;
        font-weight: bold;
        color: #000000;
    }
    
    .profile-info h1 {
        font-size: 32px;
        margin-bottom: 10px;
        font-weight: bold;
    }
    
    .profile-stats {
        color: #999999;
        margin-bottom: 15px;
    }
    
    /* 탭 스타일 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 30px;
        background-color: transparent;
        border-bottom: 1px solid #333333;
        padding-left: 40px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: transparent;
        color: #999999;
        border: none;
        padding: 15px 0;
    }
    
    .stTabs [aria-selected="true"] {
        color: #ffffff;
        border-bottom: 2px solid #ffffff;
    }
    
    /* 카드 그리드 */
    .card-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 25px;
        padding: 30px 40px;
    }
    
    .card {
        background-color: #1a1a1a;
        border-radius: 12px;
        overflow: hidden;
        cursor: pointer;
        transition: transform 0.2s;
    }
    
    .card:hover {
        transform: translateY(-5px);
    }
    
    .card-image {
        width: 100%;
        height: 200px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .card-content {
        padding: 20px;
    }
    
    .card-title {
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 10px;
        color: #ffffff;
    }
    
    .card-description {
        font-size: 14px;
        color: #cccccc;
        margin-bottom: 15px;
        line-height: 1.5;
    }
    
    .card-stats {
        display: flex;
        gap: 15px;
        font-size: 13px;
        color: #999999;
        margin-bottom: 15px;
    }
    
    .card-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
    }
    
    .tag {
        background-color: #333333;
        color: #ffffff;
        padding: 5px 12px;
        border-radius: 15px;
        font-size: 12px;
    }
    
    .tag-성인 {
        background-color: #ff6b6b;
    }
    
    /* 정렬 버튼 */
    .sort-buttons {
        display: flex;
        justify-content: flex-end;
        gap: 10px;
        padding: 20px 40px 0 40px;
    }
    
    /* 버튼 스타일 */
    .stButton button {
        background-color: #333333;
        color: #ffffff;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
    }
</style>
""", unsafe_allow_html=True)

# 헤더
col1, col2, col3 = st.columns([1, 6, 1])
with col1:
    st.markdown("<div style='font-size: 24px; font-weight: bold;'>IP</div>", unsafe_allow_html=True)
with col3:
    if st.button("🔍"):
        pass
    if st.button("📬"):
        pass

# 배너
st.markdown('<div class="banner"></div>', unsafe_allow_html=True)

# 프로필 섹션
st.markdown("""
<div class="profile-section">
    <div class="profile-image">IP</div>
    <div class="profile-info">
        <h1>포스타입 오리지널</h1>
        <div class="profile-stats">
            포스타입 오리지널 · 구독자 3.5만명 · 포스트 1.9천개
        </div>
        <div style="color: #999999;">
            🔗 <a href="https://twitter.com/postype" style="color: #999999;">https://twitter.com/postype</a> 외 링크 2개
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# 탭
tab1, tab2 = st.tabs(["활동", "시리즈"])

with tab2:
    # 정렬 옵션
    col1, col2, col3, col4 = st.columns([1, 1, 1, 8])
    with col1:
        st.button("기본순")
    with col2:
        st.button("최신순")
    with col3:
        st.button("인기순")
    
    st.markdown("<h2 style='padding: 20px 40px 0 40px;'>시리즈 63개</h2>", unsafe_allow_html=True)
    
    # 시리즈 데이터 (예시)
    series_data = [
        {
            "title": "[GL] 2024 포스타입 앱솔로지 | 겨울",
            "description": "첫눈이 모든 걸 덮는 순간, 둘만의 집은 열기로 채워지는 GL 단편선",
            "episodes": "총 11화",
            "views": "48만",
            "likes": "7.6천",
            "comments": "437",
            "tags": ["성인", "웹툰", "단편", "gl", "겨울", "첫눈"],
            "gradient": "linear-gradient(135deg, #434343 0%, #000000 100%)"
        },
        {
            "title": "[GL] 분리수거 하다가 전여친 마주치는 만화",
            "description": "분리수거에서 해어진 옛 연인과 마주친 확률은? 아파트 주민으로 재회한 두 여자의 새로 쓰여지는 이야기",
            "episodes": "총 18화",
            "views": "59만",
            "likes": "1.4천",
            "comments": "1.2천",
            "tags": ["성인", "웹툰", "완성", "gl", "드라마", "재회물"],
            "gradient": "linear-gradient(135deg, #2c3e50 0%, #34495e 100%)"
        },
        {
            "title": "가상아이돌 김준의",
            "description": "🎤아이돌<트루픽스>와 네덜도 팬 에군의 하이퍼리얼리즘 k-pop 팬덤 실태 보고서",
            "episodes": "총 98화",
            "views": "164만",
            "likes": "3.3천",
            "comments": "8.2천",
            "tags": ["웹툰", "아이돌", "kpop", "현애계물", "팬덤"],
            "gradient": "linear-gradient(135deg, #e91e63 0%, #f48fb1 100%)"
        },
        {
            "title": "[BL] 2024 포스타입 앱솔로지 | 가을",
            "description": "가을에 펼쳐진 화려한 축제, 2024 포스타입 가을 앱솔로지",
            "episodes": "총 5화",
            "views": "9.6만",
            "likes": "1.3천",
            "comments": "165",
            "tags": ["성인", "웹툰", "bl", "가을", "축제"],
            "gradient": "linear-gradient(135deg, #3a506b 0%, #5b7c99 100%)"
        }
    ]
    
    # 카드 그리드
    cols = st.columns(2)
    for idx, series in enumerate(series_data):
        with cols[idx % 2]:
            st.markdown(f"""
            <div class="card">
                <div class="card-image" style="background: {series['gradient']};"></div>
                <div class="card-content">
                    <div class="card-title">{series['title']}</div>
                    <div class="card-description">{series['description']}</div>
                    <div class="card-stats">
                        <span>{series['episodes']}</span>
                        <span>👁 {series['views']}</span>
                        <span>❤️ {series['likes']}</span>
                        <span>💬 {series['comments']}</span>
                    </div>
                    <div class="card-tags">
                        {''.join([f'<span class="tag tag-{tag if tag == "성인" else ""}">{tag}</span>' for tag in series['tags']])}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)