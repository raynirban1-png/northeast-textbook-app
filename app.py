import streamlit as st
import os
import json
import sys
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from io import BytesIO
from pathlib import Path

# from content.unit1 import unit1_data
# from content.unit2 import unit2_data
# from content.unit3 import unit3_data
# from content.unit4 import unit4_data

BASE_DIR = Path(__file__).resolve().parent

if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from questions.important_questions import exam_zone_data
from questions.model_answers import model_answers_data
from content.references import reference_data
from revision.quick_revision import quick_revision_data
FACULTY_PASSWORD = "Hybrid2030"

def create_pdf(title, content):
    buffer = BytesIO()

    pdfmetrics.registerFont(
        TTFont(
            "AssameseFont",
            str(BASE_DIR / "NotoSansBengali-VariableFont_wdth,wght.ttf")
        )
    )

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    title_style = styles["Heading1"]
    title_style.fontName = "AssameseFont"
    title_style.fontSize = 16

    body_style = styles["Normal"]
    body_style.fontName = "AssameseFont"
    body_style.fontSize = 12
    body_style.leading = 18

    story = []

    story.append(
        Paragraph(title, title_style)
    )

    story.append(
        Spacer(1, 20)
    )

    for paragraph in content.split("\n"):
        if paragraph.strip():
            story.append(
                Paragraph(paragraph, body_style)
            )
            story.append(
                Spacer(1, 10)
            )

    doc.build(story)

    buffer.seek(0)
    return buffer
st.set_page_config(
    page_title="POL060304",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -----------------------------------
# MASTER CONTENT MAP
# -----------------------------------

file_path = os.path.join(str(BASE_DIR), "data", "notes.json")

def load_notes_data():
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_notes_data(notes_data):
    temp_file_path = f"{file_path}.tmp"

    with open(temp_file_path, "w", encoding="utf-8") as f:
        json.dump(
            notes_data,
            f,
            ensure_ascii=False,
            indent=4
        )
        f.flush()
        os.fsync(f.fileno())

    os.replace(temp_file_path, file_path)

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

all_units = load_notes_data()


# -----------------------------------
# HEADER
# -----------------------------------

st.title("POL060304")
st.subheader("Politics in Northeast India")
st.write("ষষ্ঠ ষান্মাসিক | অসমীয়া ডিজিটেল পাঠ্যসামগ্ৰী")
st.markdown(
    """
    **B.P Chaliha College (BPC)**  
    BA 6th Semester
    """
)

st.markdown("---")

# -----------------------------------
# MAIN MENU
# -----------------------------------

menu = st.radio(
    "বিভাগ নির্বাচন কৰক",
    (
        "পাঠ্য সামগ্ৰী",
        "Search Topic",
        "Exam Zone",
        "Model Answers",
        "দ্ৰুত পুনৰালোচনা",
        "Visual Learning Zone",
        "Faculty Admin"
    )
)

# -----------------------------------
# STUDY MATERIALS
# -----------------------------------

if menu == "পাঠ্য সামগ্ৰী":

    selected_unit = st.selectbox(
        "ইউনিট নির্বাচন কৰক",
        list(all_units.keys())
    )

    selected_topic = st.selectbox(
        "বিষয় নির্বাচন কৰক",
        list(all_units[selected_unit].keys())
    )

    st.markdown("---")
    st.header(selected_topic)

    st.write(all_units[selected_unit][selected_topic])

    pdf_file = create_pdf(
    selected_topic,
    all_units[selected_unit][selected_topic]
    )

    st.download_button(
        label="PDF নোট ডাউনলোড কৰক",
        data=pdf_file,
        file_name=f"{selected_topic}.pdf",
        mime="application/pdf"
    )

# -----------------------------------
# IMPORTANT QUESTIONS
# -----------------------------------
elif menu == "Search Topic":

    st.header("Search Topic")

    search_term = st.text_input("বিষয় লিখক")

    if search_term:

        found = False

        for unit_name, topics in all_units.items():
            for topic_name, topic_content in topics.items():

                if (
                    search_term.lower() in topic_name.lower()
                    or search_term.lower() in topic_content.lower()
                ):
                    found = True

                    st.success(f"Found in {unit_name}")
                    st.subheader(topic_name)
                    st.write(topic_content)

                    # Suggested Further Reading
                    if search_term in reference_data:
                        st.markdown("---")
                        st.subheader("Suggested Further Reading")

                        for ref in reference_data[search_term]:
                            st.write(f"• {ref}")

        if not found:
            st.error("কোনো বিষয় পোৱা নগ'ল")

elif menu == "Exam Zone":

    st.header("Exam Zone")

    selected_exam = st.selectbox(
        "বিভাগ নিৰ্বাচন কৰক",
        list(exam_zone_data.keys())
    )

    st.header(selected_exam)

    for section, questions in exam_zone_data[selected_exam].items():

        st.subheader(section)

        for q in questions:
            st.write(q)

        st.markdown("---")

    

# -----------------------------------
# QUICK REVISION
# -----------------------------------
elif menu == "Model Answers":

    st.header("Model Answers")

    selected_answer = st.selectbox(
        "উত্তৰ নির্বাচন কৰক",
        list(model_answers_data.keys())
    )

    selected_model_answer = model_answers_data[selected_answer]

    if isinstance(selected_model_answer, dict):
        for question, answer in selected_model_answer.items():
            st.subheader(question)

            if isinstance(answer, str):
                st.markdown(answer.replace("\n", "\n\n"))
            elif isinstance(answer, dict):
                for sub_question, sub_answer in answer.items():
                    st.markdown(f"**{sub_question}**")
                    st.markdown(str(sub_answer).replace("\n", "\n\n"))
            elif isinstance(answer, (list, tuple)):
                for item in answer:
                    st.markdown(str(item).replace("\n", "\n\n"))
            else:
                st.markdown(str(answer).replace("\n", "\n\n"))

            st.markdown("---")
    else:
        st.markdown(str(selected_model_answer).replace("\n", "\n\n"))

elif menu == "দ্ৰুত পুনৰালোচনা":

    st.header("দ্ৰুত পুনৰালোচনা")

    selected_revision_unit = st.selectbox(
        "ইউনিট নির্বাচন কৰক",
        list(quick_revision_data.keys())
    )

    for item in quick_revision_data[selected_revision_unit]:
        st.write(f"• {item}")
elif menu == "Visual Learning Zone":

    st.title("Visual Learning Zone")

    st.subheader("Political Maps")
    st.image("images/northeast_india_map.jpg", caption="Northeast India Political Map", use_container_width=True)
    st.markdown("""
- Northeast India Political Map  
- Colonial Assam Administrative Divisions  
- Sixth Schedule Autonomous Areas  
- State Reorganisation Maps  
- Migration Routes in Assam  
""")

    st.subheader("Historical Timelines")
    st.markdown("""
- Treaty of Yandabo (1826)  
- Phulaguri Dhewa (1861)  
- Patharughat Uprising (1894)  
- Assam Movement (1979–1985)  
- Assam Accord (1985)  
""")

    st.subheader("Concept Flowcharts")
    st.markdown("""
- Colonial Policy → Economic Exploitation → Resistance  
- Immigration → Identity Politics → Assam Movement  
- Sixth Schedule → Autonomy → Political Consequences  
""")

    st.subheader("Comparative Analysis")
    st.markdown("""
- Colonial vs Marxist Historiography  
- Excluded Areas vs Sixth Schedule  
- Naga Nationalism vs Assam Movement  
""")
elif menu == "Faculty Admin":

    password = st.text_input(
        "Faculty Password",
        type="password"
    )

    if password:

        if password != FACULTY_PASSWORD:
            st.error("Access denied")
            st.stop()

        st.success("Faculty access granted")

        st.header("Faculty Admin Panel")
        st.warning("Only for faculty content updates")

        notes_data = load_notes_data()
        if not isinstance(notes_data, dict):
            notes_data = {}

        if st.session_state.pop("faculty_save_success", False):
            st.success("Note saved successfully")

        if st.session_state.pop("faculty_restore_success", False):
            st.success("Backup restored successfully")

        unit_name = st.selectbox(
            "Select Unit",
            [
                "Unit I",
                "Unit II",
                "Unit III",
                "Unit IV"
            ],
            key="faculty_unit_name"
        )

        unit_topics = notes_data.get(unit_name, {})
        if not isinstance(unit_topics, dict):
            unit_topics = {}

        topic_options = list(unit_topics.keys()) + ["+ Add New Topic"]

        pending_topic_choice = st.session_state.pop(
            "faculty_pending_topic_choice",
            None
        )
        if pending_topic_choice in topic_options:
            st.session_state["faculty_topic_choice"] = pending_topic_choice

        topic_choice = st.selectbox(
            "Select Existing Topic",
            topic_options,
            key="faculty_topic_choice"
        )

        if topic_choice == "+ Add New Topic":
            if st.session_state.pop("faculty_clear_new_topic_name", False):
                st.session_state["faculty_new_topic_name"] = ""
            topic_name = st.text_input(
                "New Topic Name",
                key="faculty_new_topic_name"
            ).strip()
        else:
            topic_name = topic_choice

        editor_target = (unit_name, topic_choice)
        if st.session_state.get("faculty_editor_target") != editor_target:
            st.session_state["faculty_topic_content"] = (
                unit_topics.get(topic_name, "")
                if topic_choice != "+ Add New Topic"
                else ""
            )
            st.session_state["faculty_editor_target"] = editor_target

        topic_content = st.text_area(
            "Full Note Content",
            height=300,
            key="faculty_topic_content"
        )

        if st.button("Save Note"):

            if not topic_name:
                st.error("Enter a topic name before saving.")
            else:
                latest_notes_data = load_notes_data()
                if not isinstance(latest_notes_data, dict):
                    latest_notes_data = {}

                latest_notes_data.setdefault(unit_name, {})
                latest_notes_data[unit_name][topic_name] = topic_content

                saved_data = save_notes_data(latest_notes_data)

                saved_content = saved_data.get(unit_name, {}).get(topic_name)

                if saved_content == topic_content:
                    st.session_state["faculty_save_success"] = True
                    st.session_state["faculty_pending_topic_choice"] = topic_name
                    st.session_state["faculty_clear_new_topic_name"] = True
                    st.session_state["faculty_editor_target"] = (unit_name, topic_name)
                    st.rerun()
                else:
                    st.error("Save verification failed. The JSON file did not update as expected.")


        st.markdown("---")
        st.subheader("Backup System")

        with open(file_path, "r", encoding="utf-8") as f:
            backup_data = f.read()

        st.download_button(
            label="Download Full Backup",
            data=backup_data,
            file_name="notes_backup.json",
            mime="application/json"
        )
        st.markdown("---")
        st.subheader("Restore Backup")

        uploaded_backup = st.file_uploader(
            "Upload Backup JSON File",
            type=["json"],
            key="faculty_uploaded_backup"
        )

        if uploaded_backup is not None and st.button("Restore Backup"):

            restored_data = json.load(uploaded_backup)
            if not isinstance(restored_data, dict):
                st.error("Backup JSON must contain a top-level object.")
                st.stop()

            save_notes_data(restored_data)

            st.session_state["faculty_restore_success"] = True
            st.rerun()
# -----------------------------------
# FOOTER
# -----------------------------------


st.markdown("---")
st.caption(
    "Prepared and Maintained by\n"
    "Dr. Nirban Ray\n"
    "Assistant Professor, Department of Political Science"
)
