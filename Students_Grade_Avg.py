import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page setup
st.set_page_config(page_title="Student Grade Report", layout="wide")

st.title("🎓 Student Grade Average & Performance Report")

st.markdown("Enter the subject-wise test scores for each student below:")

# Subjects list
subjects = ["English", "Maths", "Hindi", "Science", "Tamil"]

# Get number of students
num_students = st.number_input("Number of Students", min_value=1, max_value=20, step=1)

data = []
for i in range(int(num_students)):
    st.subheader(f"Student {i + 1}")
    name = st.text_input(f"Enter Name for Student {i + 1}", key=f"name_{i}")
    scores = []
    for subject in subjects:
        score = st.number_input(f"{subject} Score", min_value=0, max_value=100, key=f"{i}_{subject}")
        scores.append(score)

    avg_score = sum(scores) / len(subjects)

    # Fail if any score < 35
    if any(score < 35 for score in scores):
        status = "Fail"
    else:
        status = "Pass"

    data.append({
        "Name": name,
        "Scores": scores,
        "Average": avg_score,
        "Status": status
    })

# Button to generate report
if st.button("Generate Report"):
    df = pd.DataFrame(data)

    # Expand scores into separate subject columns
    score_df = pd.DataFrame(df['Scores'].tolist(), columns=subjects)
    df_expanded = pd.concat([df.drop(columns=['Scores']), score_df], axis=1)

    st.subheader("📋 Student Summary Table")
    st.dataframe(df_expanded.style.applymap(
        lambda val: "background-color: #ffcccc" if isinstance(val, (int, float)) and val < 35 else ""
    ))

    st.subheader("📊 Performance Graph")

    # Bar chart for average score per student
    fig, ax = plt.subplots()
    sns.barplot(x="Name", y="Average", hue="Status", data=df_expanded, palette={"Pass": "green", "Fail": "red"}, ax=ax)
    plt.title("Student Performance (Pass/Fail)")
    plt.xticks(rotation=45)
    st.pyplot(fig)
