import streamlit as st
import os
import json
import sys
from pprint import pformat
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from io import BytesIO
from pathlib import Path
from PIL import Image

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
important_questions = exam_zone_data

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

def load_visual_panel(image_name, panel=None):
    image_path = BASE_DIR / "images" / image_name

    with Image.open(image_path) as image:
        if panel is None:
            return image.copy()

        width, height = image.size
        half_width = width // 2
        half_height = height // 2

        crop_boxes = {
            "top_left": (0, 0, half_width, half_height),
            "top_right": (half_width, 0, width, half_height),
            "bottom_left": (0, half_height, half_width, height),
            "bottom_right": (half_width, half_height, width, height),
        }

        return image.crop(crop_boxes[panel]).copy()
st.set_page_config(
    page_title="POL060304",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# -----------------------------------
# MASTER CONTENT MAP
# -----------------------------------

file_path = os.path.join(str(BASE_DIR), "data", "notes.json")
important_questions_file_path = BASE_DIR / "questions" / "important_questions.py"

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

def save_important_questions_data(question_data):
    temp_file_path = f"{important_questions_file_path}.tmp"
    serialized_data = "exam_zone_data = " + pformat(
        question_data,
        width=120,
        sort_dicts=False
    ) + "\n"

    with open(temp_file_path, "w", encoding="utf-8") as f:
        f.write(serialized_data)
        f.flush()
        os.fsync(f.fileno())

    os.replace(temp_file_path, important_questions_file_path)

all_units = load_notes_data()

query_params = st.query_params
selected_state = query_params.get("state", "home")

if isinstance(selected_state, list):
    selected_state = selected_state[0]

selected_state = str(selected_state).strip().lower()

state_pages = {
    "assam": ("Assam (অসম)", "Welcome to the Assam Textbook and Paper section."),
    "arunachal": ("Arunachal Pradesh", "Welcome to the Arunachal Pradesh Paper section."),
    "manipur": ("Manipur", "Welcome to the Manipur Paper section."),
    "meghalaya": ("Meghalaya", "Welcome to the Meghalaya Paper section."),
    "mizoram": ("Mizoram", "Welcome to the Mizoram Paper section."),
    "nagaland": ("Nagaland", "Welcome to the Nagaland Paper section."),
    "sikkim": ("Sikkim", "Welcome to the Sikkim Paper section."),
    "tripura": ("Tripura", "Welcome to the Tripura Paper section.")
}

st.sidebar.title("বিভাগ নির্বাচন কৰক")
st.sidebar.subheader("Select State")

if selected_state != "home":
    if selected_state in state_pages:
        state_title, state_message = state_pages[selected_state]
        st.title(state_title)
        st.write(state_message)
    else:
        st.title("Northeast Textbook & Papers")
        st.write("Select a state from the Android Menu to view specific papers.")

    st.stop()


# -----------------------------------
# HEADER
# -----------------------------------

st.image("images/logo.png", width=90)

st.markdown("## POL060304")
st.markdown("### Politics in Northeast India")

st.markdown("**B.P. Chaliha College (BPC)**  \nBA 6th Semester Academic Learning Platform")

st.caption("Version 1.0 • Updated for Academic Session 2026")

st.info("Faculty-guided academic support for study materials, exam preparation, model answers, revision, and visual learning.")

st.markdown("---")

# -----------------------------------
# MAIN MENU
# -----------------------------------

if "menu" not in st.session_state:
    st.session_state.menu = "পাঠ্য সামগ্ৰী"

col1, col2 = st.columns(2)

with col1:
    if st.button("📘 Study Materials", use_container_width=True):
        st.session_state.menu = "পাঠ্য সামগ্ৰী"

    if st.button("📝 Exam Zone", use_container_width=True):
        st.session_state.menu = "Exam Zone"

    if st.button("📄 Model Answers", use_container_width=True):
        st.session_state.menu = "Model Answers"

    if st.button("⚡ Quick Revision", use_container_width=True):
        st.session_state.menu = "দ্ৰুত পুনৰালোচনা"

with col2:
    if st.button("🗺 Visual Learning Zone", use_container_width=True):
        st.session_state.menu = "Visual Learning Zone"

    if st.button("🔍 Search Topic", use_container_width=True):
        st.session_state.menu = "Search Topic"

    if st.button("👨‍🏫 Faculty Admin", use_container_width=True):
        st.session_state.menu = "Faculty Admin"

    if st.button("ℹ About & Disclaimer", use_container_width=True):
        st.session_state.menu = "About & Disclaimer"

menu = st.session_state.menu

st.markdown("---")
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

    st.title("Smart Topic Finder")

    st.write("Quickly find important topics from your semester content.")

    search_unit = st.selectbox(
        "Select Unit",
        ["All Units"] + list(all_units.keys())
    )

    search_keyword = st.text_input(
        "Enter topic keyword"
    )
    normalized_keyword = search_keyword.strip().lower()

    st.markdown("---")

    results_found = False

    if normalized_keyword:
        for unit_name, topics in all_units.items():

            if search_unit != "All Units" and unit_name != search_unit:
                continue

            for topic_name, topic_content in topics.items():

                if normalized_keyword in topic_name.lower():

                    results_found = True

                    st.subheader(f"{unit_name} → {topic_name}")
                    st.write(topic_content[:500] + "...")

                    if st.button(
                        f"Open Full Topic: {topic_name}",
                        key=topic_name
                    ):
                        st.session_state.menu = "পাঠ্য সামগ্ৰী"
                        st.rerun()

    if normalized_keyword and not results_found:
        st.warning("No matching topic found.")

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
    st.subheader("Revision + Infographic Center")

    st.markdown("""
This section helps students revise important concepts quickly using
maps, diagrams, timelines, and visual summaries.
""")

    visual_unit = st.selectbox(
        "Select Visual Learning Topic",
        [
            "Political Map of Northeast India",
            "Ethnic Movements Timeline",
            "Autonomy Councils Structure",
            "Regional Political Movements",
            "Constitutional Framework of Northeast India",
            "Demographic Changes in Undivided Goalpara District",
        ]
    )

    st.markdown("---")

    if visual_unit == "Political Map of Northeast India":
        st.image("images/northeast_india_map.jpg", use_container_width=True)
        st.write("""
Important for understanding state formation, political boundaries,
strategic location, and regional identity politics.
""")

    elif visual_unit == "Ethnic Movements Timeline":
        st.image(
            load_visual_panel("ethnic_movements.png", "top_left"),
            use_container_width=True
        )
        st.write("""
Covers major ethnic assertions, identity movements, and autonomy demands
across Northeast India.
""")

    elif visual_unit == "Autonomy Councils Structure":
        st.image(
            load_visual_panel("autonomy_council.png", "top_right"),
            use_container_width=True
        )
        st.write("""
Explains Sixth Schedule areas, Autonomous District Councils,
and governance mechanisms.
""")

    elif visual_unit == "Regional Political Movements":
        st.image(
            load_visual_panel("regional_movements.png", "bottom_left"),
            use_container_width=True
        )
        st.write("""
Important student revision topic for regionalism, sub-nationalism,
and statehood movements.
""")

    elif visual_unit == "Constitutional Framework of Northeast India":
        st.image(
            load_visual_panel("constitutional_framework.png", "bottom_right"),
            use_container_width=True
        )
        st.write("""
Important for exams covering constitutional provisions,
special status, and federal structure.
""")
    elif visual_unit == "Demographic Changes in Undivided Goalpara District":

        st.image(
            "images/goalpara_demographic_changes.png",
            use_container_width=True
        )

    st.write("""
This visual explains the long-term demographic transformation of
Undivided Goalpara District from 1901 to 2020.

It helps students understand:

- migration and settlement patterns  
- religion and identity politics  
- demographic change and electoral politics  
- political implications of population shifts  
- regional tensions linked to migration debates

This is highly relevant for understanding Assam politics,
identity movements, and contemporary electoral discourse.
""") 
elif menu == "About & Disclaimer":

    st.title("About This Academic App")

    st.markdown("""
### POL060304 - Politics in Northeast India

This platform is developed for academic support of BA 6th Semester students.

### Academic Disclaimer

- This app is created strictly for educational purposes only.
- It is not an official university publication.
- Students must verify final academic guidance with faculty members and official syllabus.

### Credits

- Developed By: Nirban Ray
- Institution Support: B.P. Chaliha College
- Department: Political Science
- Course Code: POL060304
- Semester: BA 6th Semester
- Platform Version: v1.0

### Copyright Notice

- Content belongs to respective academic and educational sources and is in the developmental stage.
- Unauthorized commercial reproduction is prohibited.
- Educational fair use only.

### Feedback

For corrections, updates, or faculty review, please contact the department/admin.
""")
elif menu == "Faculty Admin":

    st.title("Faculty Admin")

    admin_password = st.text_input(
        "Enter Faculty Access Password",
        type="password"
    )

    if admin_password != FACULTY_PASSWORD:
        st.warning("Faculty access only.")
        st.stop()

    st.success("Access Granted")

    st.header("Faculty Admin Panel")
    st.warning("Only for faculty content updates")

    notes_data = load_notes_data()
    if not isinstance(notes_data, dict):
        notes_data = {}

    if st.session_state.pop("faculty_save_success", False):
        st.success("Note saved successfully")

    if st.session_state.pop("faculty_restore_success", False):
        st.success("Backup restored successfully")

    if st.session_state.pop("question_save_success", False):
        st.success("Question updated successfully.")

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
    st.subheader("Important Questions Editor")

    question_unit = st.selectbox(
        "Select Question Unit",
        list(important_questions.keys()),
        key="question_unit_select"
    )

    question_section = st.selectbox(
        "Select Section",
        list(important_questions[question_unit].keys()),
        key="question_section_select"
    )

    existing_questions = important_questions[question_unit][question_section]

    selected_question = st.selectbox(
        "Select Existing Question",
        ["Create New Question"] + existing_questions,
        key="question_existing_select"
    )

    if selected_question == "Create New Question":
        edited_question = st.text_area(
            "Enter New Question",
            height=150,
            key="new_question_editor"
        )
    else:
        edited_question = st.text_area(
            "Edit Selected Question",
            value=selected_question,
            height=150,
            key="existing_question_editor"
        )

    if st.button("Save Question Update"):

        normalized_question = edited_question.strip()

        if normalized_question:
            updated_questions = existing_questions.copy()

            if selected_question != "Create New Question":
                updated_questions.remove(selected_question)

            updated_questions.append(normalized_question)
            important_questions[question_unit][question_section] = updated_questions
            save_important_questions_data(important_questions)

            st.session_state["question_save_success"] = True
            st.rerun()

        else:
            st.error("Question cannot be empty.")
    
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
    "Dr. Nirban Ray,\n"
    "Assistant Professor, Department of Political Science"
)
