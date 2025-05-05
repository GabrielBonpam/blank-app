import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="🎈 My new app",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title and description
st.title("🎈 My new app")
st.write("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")

# Sidebar controls
st.sidebar.header("Customize")
chart_type = st.sidebar.selectbox("Chart type", ["Line", "Bar", "Area"])
num_points = st.sidebar.slider(
    "Number of points", min_value=10, max_value=200, value=50, step=10
)

# Generate sample data
data = pd.DataFrame(
    np.random.randn(num_points, 3),
    columns=["A", "B", "C"]
)

# Display chart
st.header("🔍 Random Data Visualization")
if chart_type == "Line":
    st.line_chart(data)
elif chart_type == "Bar":
    st.bar_chart(data)
else:
    st.area_chart(data)

# Show raw data in an expander
with st.expander("Show raw data"):
    st.dataframe(data)

# File uploader
st.header("📂 Upload Your CSV")
uploader = st.file_uploader("Upload a CSV file for preview", type=["csv"])
if uploader is not None:
    df = pd.read_csv(uploader)
    st.subheader("Preview of uploaded CSV")
    st.dataframe(df)

# Map example
st.header("🗺️ Sample Map")
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns=["lat", "lon"]
)
st.map(map_data)

# Metrics
st.header("📈 Key Metrics")
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "+1.2 °F")
col2.metric("Wind Speed", "9 mph", "-8%")
col3.metric("Humidity", "70%", "+4%")

# Progress bar example
st.header("⏳ Progress Demo")
if st.button("Run Progress"):
    progress_bar = st.progress(0)
    for i in range(100):
        progress_bar.progress(i + 1)
        st.time.sleep(0.01)

# AI chat placeholder
st.sidebar.header("🤖 AI Chat")
user_prompt = st.sidebar.text_input("Ask the app a question:")
if user_prompt:
    st.sidebar.write(f"You asked: {user_prompt}")
    # Placeholder for model integration
    st.sidebar.write("**AI response**: (model output would appear here)")

# Footer
st.write("---")
st.write("Built with ❤️ using Streamlit")
