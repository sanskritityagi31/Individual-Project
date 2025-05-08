import streamlit as st
import openai

# Set your API Key
openai.api_key = "your-api-key-here"

st.set_page_config(page_title="GenAI Study Assistant", layout="wide")

# Title
st.title("🎓 Smart GenAI-Based Study Assistant")
st.subheader("Get topic explanations, quizzes, summaries, and study plans")

# Sidebar
st.sidebar.title("🛠️ Options")
task = st.sidebar.radio("Choose a Task", ["Topic Explanation", "Quiz Generation", "Summary", "Study Plan"])

# Input
topic = st.text_input("📌 Enter your Topic or Subject")

# Prompt Templates
def generate_prompt(task, topic):
    if task == "Topic Explanation":
        return f"Explain the topic '{topic}' in simple terms with examples suitable for a college student."
    elif task == "Quiz Generation":
        return f"Create 5 multiple choice questions (MCQs) with answers on the topic '{topic}'."
    elif task == "Summary":
        return f"Provide a short summary with key points for the topic '{topic}'."
    elif task == "Study Plan":
        return f"Create a 7-day study plan to understand the topic '{topic}' in depth, with daily goals."
    return ""

# Generate
if st.button("✨ Generate"):
    if topic.strip() == "":
        st.warning("Please enter a topic.")
    else:
        with st.spinner("Generating content..."):
            prompt = generate_prompt(task, topic)
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7
                )
                content = response['choices'][0]['message']['content']
                st.markdown("### 📄 Output:")
                st.markdown(content)
            except Exception as e:
                st.error(f"An error occurred: {e}")
