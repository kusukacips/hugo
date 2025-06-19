import streamlit as st
from datetime import datetime
import base64
import os

# Initialize session state
if 'cat_clicked' not in st.session_state:
    st.session_state.cat_clicked = False

# Improved image loading function
def get_image_base64(path):
    try:
        with open(path, "rb") as image_file:
            return f"data:image/jpeg;base64,{base64.b64encode(image_file.read()).decode()}"
    except FileNotFoundError:
        st.error(f"Image file not found at: {os.path.abspath(path)}")
        return None
    except Exception as e:
        st.error(f"Error loading image: {str(e)}")
        return None

# App configuration
st.set_page_config(
    page_title="🥊 Boxing Encouragement",
    page_icon="💬",
    layout="centered"
)

# App content
st.markdown('<div class="title-text">💬 Pesan ini dibuat khusus buat Hugo ! </div>', unsafe_allow_html=True)

# Current time for notification
current_time = datetime.now().strftime("%I:%M %p").lower().lstrip("0")

# Container for notification and cat button
st.markdown('<div class="container">', unsafe_allow_html=True)

# Custom CSS to mimic iOS 10 notification and style the cat button
st.markdown("""
<style>
    .ios-notification {
        width: 300px;
        border-radius: 15px;
        padding: 0;
        margin: 20px auto;
        background: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        font-family: -apple-system, BlinkMacSystemFont, sans-serif;
        overflow: hidden;
        position: relative;
    }
    .notification-header {
        background: #f8f8f8;
        padding: 10px 15px;
        border-bottom: 1px solid #e5e5e5;
        font-size: 0.8rem;
        color: #888;
        display: flex;
        justify-content: space-between;
    }
    .notification-body {
        padding: 15px;
    }
    .contact-name {
        font-weight: bold;
        font-size: 1rem;
        margin-bottom: 5px;
    }
    .message-text {
        font-size: 0.95rem;
        line-height: 1.4;
    }
    .time-text {
        font-size: 0.7rem;
        color: #888;
    }
    .title-text {
        font-size: 1.5rem;
        text-align: center;
        margin-bottom: 20px;
        color: #333;
    }
    .cat-button {
        cursor: pointer;
        transition: transform 0.2s;
        display: block;
        margin: 0 auto;
    }
    .cat-button:hover {
        transform: scale(1.05);
    }
    .gift-container {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        margin-top: 20px;
    }
    .gift-image {
        width: 30%;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .gift-message {
        text-align: center;
        font-style: italic;
        margin: 15px 0;
        color: #ff6b6b;
    }
    .container {
        display: flex;
        justify-content: center;
        align-items: flex-start;
        margin-bottom: 30px;
    }
    .cat-container {
        width: 100%;
        text-align: center;
        margin: 20px 0;
    }
</style>
""", unsafe_allow_html=True)

# iOS Notification
st.markdown(f"""
<div class="ios-notification">
    <div class="notification-header">
        <span>MESSAGES</span>
        <span>now</span>
    </div>
    <div class="notification-body">
        <div class="contact-name">Cipa</div>
        <div class="message-text">hugo, semangat ya tanding hari ini! cipa yakin hugo pasti bisa, karena hugo udah latian terus. Semoga tandingnya menang ya hugo! Oh iya, jangan lupa berdoa dulu sebelum mulai tandingnya sayang</div>
        <div class="time-text">{current_time}</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Instruction notification (centered)
st.markdown("""
<div style="text-align: center; margin: 15px 0;">
    <div class="ios-notification" style="display: inline-block; width: auto;">
        <div class="notification-body">
            <div class="message-text" style="text-align: center; font-style: italic;">
                Press 💝 below to see gifts from Cipa!
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Centered cat image container
st.markdown('<div class="cat-container">', unsafe_allow_html=True)

# Local cat image button
image_files_to_try = [
    "boxing_cat.jpeg",
    "boxing_cat.jpg", 
    "boxing_cat.png",
    os.path.join("images", "boxing_cat.jpeg"),
]

cat_image_base64 = None
for image_file in image_files_to_try:
    cat_image_base64 = get_image_base64(image_file)
    if cat_image_base64:
        break

if cat_image_base64:
    if st.button("💝", key="cat_button"):
        st.session_state.cat_clicked = True
    st.markdown(
        f'<div style="display: flex; justify-content: center;"><img src="{cat_image_base64}" class="cat-button" onclick="st.scriptrunner.scriptRun(\'cat_clicked\', \'cat_clicked\', False)"></div>', 
        unsafe_allow_html=True
    )
else:
    default_cat_url = "https://placekitten.com/100/100"
    if st.button("", key="cat_button"):
        st.session_state.cat_clicked = True
    st.markdown(
        f'<div style="display: flex; justify-content: center;"><img src="{default_cat_url}" class="cat-button" onclick="st.scriptrunner.scriptRun(\'cat_clicked\', \'cat_clicked\', False)"></div>',
        unsafe_allow_html=True
    )

st.markdown('</div>', unsafe_allow_html=True)  # Close cat-container

# Show gifts only if cat was clicked
if st.session_state.cat_clicked:
    # Centered gift message with pop-up animation
    st.markdown("""
    <style>
        @keyframes fadeIn {
            0% { opacity: 0; transform: translateY(20px); }
            100% { opacity: 1; transform: translateY(0); }
        }
        .pop-up {
            animation: fadeIn 0.5s ease-out;
        }
    </style>
    <div class="pop-up" style="text-align: center;">
        <div class="gift-message">This is a gift from Cipa for Hugo, to make him more excited! xixixi</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Notification message
    st.toast("Hope Hugo likes it, dear spirit ✨", icon='💝')
    
    # Gift images from local files with pop-up effect
    st.markdown('<div class="gift-container pop-up">', unsafe_allow_html=True)
    
    gift_images = ["ayam.jpeg", "kopi.jpeg", "kucing.jpeg", "love.jpeg", "cipa.jpeg", "susu.png"]
    cols = st.columns(2)  # Create 2 columns for better layout
    
    for i, img_name in enumerate(gift_images):
        img_base64 = get_image_base64(img_name) or \
                    get_image_base64(img_name.replace('.jpeg', '.jpg')) or \
                    get_image_base64(img_name.replace('.jpeg', '.png')) or \
                    get_image_base64(os.path.join("images", img_name))
        
        with cols[i % 2]:  # Alternate between columns
            if img_base64:
                st.markdown(
                    f'<div class="pop-up" style="margin-bottom: 20px; text-align: center;">'
                    f'<img src="{img_base64}" style="width:100%; border-radius:10px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);">'
                    f'</div>', 
                    unsafe_allow_html=True
                )
            else:
                st.error(f"Could not load gift image: {img_name}")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("Made with 💖 from Cipa")