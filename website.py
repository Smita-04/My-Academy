import streamlit as st
import streamlit.components.v1 as components



st.set_page_config(page_title="my academy", layout="wide")

# --- CSS and Fonts ---
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap" rel="stylesheet">
<style>
body {
    font-family: 'Poppins', sans-serif;
}
.section h2 {
    font-weight: 600;
.navbar {
    background-color: #2a2a2a;
    padding: 1rem 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: sticky;
    top: 0;
    z-index: 1000;
}
.navbar a {
    color: white;
    margin: 0 1rem;
    text-decoration: none;
    font-weight: 600;
}
.navbar a:hover {
    color: #white;
}
.hero {
    min-height: 90vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    color: white;
    background:url('https://static.fibre2fashion.com//articleresources/images/23/2287/988ebe_Big.jpg');
    background-size: cover;
    background-position: center;
    padding: 5rem 2rem;
    opacity: 0;
    animation: fadeIn 2s ease-out forwards;
}
.hero h1, .hero p, .hero button {
    animation: fadeInUp 1.5s ease-out;
}
.hero h1 {
    font-size: 3.5rem;
}
.hero p {
    font-size: 1.25rem;
}
.hero button {
    margin-top: 2rem;
    padding: 1rem 2rem;
    font-size: 1.1rem;
    background-color: #ff7043;
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
}
.hero button:hover {
    background-color: #e64a19;
}
.section {
    max-width: 1200px;
    margin: 3rem auto;
    padding: 3rem 2rem;
    background-color: #ffffff;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    color: #222;
    opacity: 0;
    animation: fadeIn 1.5s ease-out forwards;
}
h2, p {
    animation: fadeInUp 1.5s ease-out;
}
}
.button-style {
    background-color: #ff7043;
    color: white;
    padding: 0.8rem 1.5rem;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-weight: bold;
}
.button-style:hover {
    background-color: #e64a19;
}
.feature-card {
    text-align: center;
    padding: 2rem 1rem;
    background-color: #fafafa;
    border-radius: 12px;
    transition: 0.3s;
    border: 1px solid #eee;
}
.feature-card:hover {
    box-shadow: 0 6px 20px rgba(0,0,0,0.12);
    transform: translateY(-5px);
}
.feature-icon {
    width: 80px;
    margin-bottom: 2rem;
}
.feature-title {
    font-size: 1.2rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
}
.feature-desc {
    color: #555;
    font-size: 0.95rem;
    margin-bottom: 1rem;
}
div.stButton > button {
    background-color: #ff7043;
    color: white;
    padding: 0.6rem 1.3rem;
    border: none;
    border-radius: 8px;
    font-weight: bold;
    font-size: 0.9rem;
    cursor: pointer;
    transition: background-color 0.3s ease;
    position :centre;
}
div.stButton > button:hover {
    background-color: #e64a19;
}
.blog-card {
    background-color: #fff;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 2rem;
    display: flex;
    align-items: center;
    gap: 2rem;
    width: 100%;
    height: 300px; /* Fixed height to keep all cards same size */
}
.blog-card img {
    width: 150px;
    height: 150px;
    object-fit: cover;
    border-radius: 10px;
}
.blog-card .content {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100%;
    font-size: 0.95rem;  /* Adjusting the font size */
    color: #555;  /* Ensuring the text color is consistent */
}
.blog-card h3 {
    font-size: 1.15rem; /* Adjusting blog title size */
    margin-bottom: 0.5rem;  /* Adding spacing between title and description */
}
.blog-card p {
    font-size: 0.9rem;  /* Adjusting the paragraph font size */
}
.blog-card:hover {
    box-shadow: 0 8px 20px rgba(0,0,0,0.2);
}

</style>
""", unsafe_allow_html=True)

# ---- Navbar ----
st.markdown("""
<div style='background-color: white; padding: 1rem; display: flex; justify-content: space-between; color: black; '>
    <div><h3 style='margin: 0;'>MYACADEMY</h3></div>
    <div style='margin-top: 0.5rem;'>
        <a href="#home" style='margin: 0 1rem; color: black; text-decoration: none;'>Home</a>
        <a href="#features" style='margin: 0 1rem; color: black; text-decoration: none;'>Features</a>
        <a href="#Blogs" style='margin: 0 1rem; color: black; text-decoration: none;'>Blogs</a>
        <a href="#about" style='margin: 0 1rem; color: black; text-decoration: none;'>About</a>
        <a href="#team" style='margin: 0 1rem; color: black; text-decoration: none;'>Team</a>
        <a href="#contact" style='margin: 0 1rem; color: black; text-decoration: none;'>Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ---- Hero Section ----
st.markdown("""
<div id="home" style='text-align: center; padding: 5rem; background-image: url("https://static.fibre2fashion.com//articleresources/images/23/2287/988ebe_Big.jpg"); background-size: cover; color: white;'>
    <h1>Welcome to My Academy</h1>
    <p>AI-powered fashion demand </p>
<p>forecasting for tomorrow's style trends 
 .</p>
</div>
""", unsafe_allow_html=True)

# ---- Feature Section ----
st.markdown("""
<div id="features" style="text-align: center; padding: 4rem 2rem;">
    <h2 style="font-size: 2.5rem; font-weight: 600; margin-bottom: 0.5rem;">Features</h2>
    <p style="font-size: 1.1rem; color: #555;">Explore how MyntraMind predicts future fashion trends using AI and data science.</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
# Use columns to create three blocks side by side
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <!--  Forecast Image Block -->
        <img src="https://1.bp.blogspot.com/-3df860veUW4/VIlI3PT1JaI/AAAAAAAABBA/rgNpy8hoWFc/s1600/Fashion%2BFor%2BWomen%2B(3).jpg" class="feature-icon" style="width: 200px; height: 300px; object-fit: cover; border-radius: 10px;">
        <div class="feature-title">Forecast</div>
        <div class="feature-desc">AI-driven forecasts based on celebrity trends and pop culture.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Explore Forecast"):
        st.switch_page("pages/Forecast.py")

with col2:
    st.markdown("""
    <div class="feature-card">
        <!-- Grassroots Forecast Image Block -->
       <img src="https://luftkussatelier.com/wp-content/uploads/2022/06/How-to-design-clothes.jpg" class="feature-icon" style="width: 200px; height: 300px; object-fit: cover; border-radius: 10px;">
        <div class="feature-title">Upcoming Highlights</div>
        <div class="feature-desc">Track the  fashion movements and local style preferences.</div>
    </div>
      <a href="https://www.fsia.in/forever-miss-india-new.php" target="_blank">Read more...</a>
      <a href="https://www.mrsindiainternationalqueen.com/" target="_blank">Read more...</a>

    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <!-- Video Insights Image Block -->
        <img src="https://img.freepik.com/free-vector/hand-drawn-fashion-show-runway_23-2148815090.jpg?w=740&t=st=1661560119~exp=1661560719~hmac=352f220f1bee9d8a234bb6f1b75d0a17721d52e3ec8690b3994e863ea9999fbc" class="feature-icon" style="width: 200px; height: 300px; object-fit: cover; border-radius: 10px;">
        <div class="feature-title">Video Insights</div>
        <div class="feature-desc">Visual previews and animated trends based on demand data.</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("Watch Insights"):
        st.info("Coming soon: Trend videos and more!")



import streamlit as st

# Header
st.markdown("""
<div id="Blogs" style="text-align:center; padding: 4rem 2rem;">
    <h2 style="font-size: 2.5rem; font-weight: 600; margin-bottom: 0.5rem;">Latest Blogs</h2>
    <p style="font-size: 1.1rem; color: #555;">Stay updated with the latest insights and trends in fashion tech!</p>
</div>

<style>
.blog-card {
    border: 1px solid #eee;
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0,0,0,0.05);
    overflow: hidden;
    background-color: #fff;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    display: flex;
    flex-direction: column;
    height: 100%;
}
.blog-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0,0,0,0.1);
}
.blog-card img {
    width: 100%;
    height: 400px;
    object-fit: cover;
    display: block;
}
.blog-card .content {
    padding: 1rem;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    flex: 1;
}
.blog-card h3 {
    font-size: 1.2rem;
    margin-bottom: 0.5rem;
    color: #333;
}
.blog-card p {
    font-size: 1rem;
    color: #555;
    margin-bottom: 1rem;
}
.blog-card a {
    margin-top: auto;
    color: #ff7043;
    font-weight: bold;
    text-decoration: none;
}
.blog-card a:hover {
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# Blog columns
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="blog-card">
        <img src="https://thefashionguitar.com/wp-content/uploads/2019/10/Thefashionguitar-for-Hilfiger-Collection-2.jpg" alt="AI in Fashion Forecasting">
        <div class="content">
            <h3>How AI is Transforming Fashion Demand Forecasting</h3>
            <p>Explore how AI is revolutionizing fashion demand prediction.</p>
            <a href="https://phenav.com/fashion-show" target="_blank">Read more...</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="blog-card">
        <img src="https://somimag.com/wp-content/uploads/2016/09/lanvn2016-1.jpg" alt="Fashion Trends 2025">
        <div class="content">
            <h3>5 Trends to Watch in 2025</h3>
            <p>Discover the key fashion trends that are expected to dominate the industry in the coming years.</p>
            <a href="https://thedaileigh.com/what-to-wear#google_vignette" target="_blank">Read more...</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="blog-card">
        <img src="https://recollections.biz/blog/wp-content/uploads/2015/06/80966-636.jpg" alt="Climate and Apparel">
        <div class="content">
            <h3>The Role of Climate in Apparel Preferences</h3>
            <p>Understanding how climate patterns influence clothing choices and their impact on fashion sales.</p>
            <a href="https://thefashionguitar.com/" target="_blank">Read more...</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

components.html(
    """
    <style>
        #chatbotModal {
            display: none;
            position: fixed;
            z-index: 9999;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
            overflow: auto;
        }

        #chatbotModalContent {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            width: 80%;
            max-width: 600px;
            height: 70%;
            position: relative;
        }

        #closeBtn {
            position: absolute;
            top: 10px;
            right: 10px;
            background-color: #ff4c4c;
            color: white;
            border: none;
            padding: 10px;
            cursor: pointer;
            border-radius: 50%;
            font-size: 16px;
            z-index: 10;
        }

        .open-chat-btn {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            position: fixed;
            bottom: 20px;
            right: 20px;
            z-index: 999;
        }

        #loadingMessage {
            text-align: center;
            font-weight: bold;
            margin-top: 40%;
        }

        iframe {
            width: 100%;
            height: 100%;
            border: none;
            display: none;
        }
    </style>

    <button class="open-chat-btn" id="chatbotLink">Open Chatbot</button>

    <div id="chatbotModal">
        <div id="chatbotModalContent">
            <button id="closeBtn">&times;</button>
            <div id="loadingMessage">Loading chatbot...</div>
        </div>
    </div>

    <script>
        const chatbotModal = document.getElementById('chatbotModal');
        const chatbotLink = document.getElementById('chatbotLink');
        const closeBtn = document.getElementById('closeBtn');
        const modalContent = document.getElementById('chatbotModalContent');
        const loadingMessage = document.getElementById('loadingMessage');

        chatbotLink.addEventListener('click', function () {
            chatbotModal.style.display = 'block';

            const iframe = document.createElement('iframe');
            iframe.src = "https://cdn.botpress.cloud/webchat/v2.3/shareable.html?configUrl=https://files.bpcontent.cloud/2025/04/24/03/20250424033910-M05NO1OM.json";

            iframe.onload = function () {
                loadingMessage.style.display = 'none';
                iframe.style.display = 'block';
            };

            modalContent.appendChild(iframe);
        });

        closeBtn.addEventListener('click', function () {
            chatbotModal.style.display = 'none';
            modalContent.querySelector("iframe")?.remove();  // Remove iframe on close
            loadingMessage.style.display = 'block'; // Reset loading message
        });

        window.addEventListener('click', function (event) {
            if (event.target === chatbotModal) {
                chatbotModal.style.display = 'none';
                modalContent.querySelector("iframe")?.remove();
                loadingMessage.style.display = 'block';
            }
        });
    </script>
    """,
    height=700,
)

# ---- About Section ----
st.markdown("""
<div id="about" class="section" style="padding: 4rem 2rem;">
    <h2 style="text-align:center;">About Us</h2>
    <p style="text-align:center;">We are a team of engineers and designers passionate about transforming fashion retail through data science and machine learning.</p>
</div>
""", unsafe_allow_html=True)

# ---- Team Section ----
st.markdown("""
<hr>
<div id="team" class="section" style="padding: 3rem 1rem; text-align:center;">
    <h2 style="color:#e91e63;">🤝 Our Team - <span style="color:#3f51b5;">MyntraMind</span></h2>
    <p>The creative minds behind the Fashion Demand Forecasting System</p>
</div>
""", unsafe_allow_html=True)

# Team layout
t1, t2, t3 = st.columns(3)

# Team Member 1
with t1:
    st.image("https://randomuser.me/api/portraits/women/44.jpg", caption="Soni Singh", use_container_width=True)
    st.markdown("""
    <p style="text-align:center;">
        📧 <a href="mailto:soni@example.com">Email</a> <br>
        📷 <a href="https://instagram.com/soni" target="_blank">Instagram</a> <br>
        🐦 <a href="https://twitter.com/soni" target="_blank">Twitter</a>
    </p>
    """, unsafe_allow_html=True)

# Team Member 2
with t2:
    st.image("https://randomuser.me/api/portraits/men/45.jpg", caption="Ravi Kumar", use_container_width=True)
    st.markdown("""
    <p style="text-align:center;">
        📧 <a href="mailto:ravi@example.com">Email</a> <br>
        📷 <a href="https://instagram.com/ravi" target="_blank">Instagram</a> <br>
        🐦 <a href="https://twitter.com/ravi" target="_blank">Twitter</a>
    </p>
    """, unsafe_allow_html=True)

# Team Member 3
with t3:
    st.image("https://randomuser.me/api/portraits/women/46.jpg", caption="Aditi Sharma", use_container_width=True)
    st.markdown("""
    <p style="text-align:center;">
        📧 <a href="mailto:aditi@example.com">Email</a> <br>
        📷 <a href="https://instagram.com/aditi" target="_blank">Instagram</a> <br>
        🐦 <a href="https://twitter.com/aditi" target="_blank">Twitter</a>
    </p>
    """, unsafe_allow_html=True)

# ---- Contact Section ----
st.markdown("""
<div id="contact" class="section" style="padding: 4rem 2rem;">
    <h2 style="text-align:center;">Contact Us</h2>
    <p style="text-align:center;">📧 info@myntramind.com | 📞 +91 12345 67890</p>
    <p style="text-align:center;">🏢 123 Fashion Street, Bangalore, India</p>
</div>
""", unsafe_allow_html=True)

# ---- Footer ----
st.markdown("""
<hr>
<div style='text-align:center; color: gray; padding-bottom: 1rem;'>
    &copy; 2025 MyntraMind — All Rights Reserved.
</div>
""", unsafe_allow_html=True)
