import streamlit as st
from pathlib import Path
import os

# ── Page config ──────────────────────────────────────────────────────────────
# st.set_page_config:(
#     page_title:="File Manager",
#     page_icon:="🗂️",
#     layout:="centered",
# )

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Syne:wght@400;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
}
code, .stTextInput input, .stTextArea textarea {
    font-family: 'JetBrains Mono', monospace !important;
}

/* Dark industrial theme */
[data-testid="stAppViewContainer"] {
    background: #0f0f0f;
    color: #e8e8e8;
}
[data-testid="stSidebar"] {
    background: #161616;
    border-right: 1px solid #2a2a2a;
}
[data-testid="stHeader"] { background: transparent; }

h1 { font-family: 'Syne', sans-serif; font-weight: 800; color: #f5f5f5; letter-spacing: -1px; }
h2, h3 { font-family: 'Syne', sans-serif; font-weight: 700; color: #d4d4d4; }

/* Buttons */
.stButton > button {
    background: #1a1a1a;
    color: #e8e8e8;
    border: 1px solid #333;
    border-radius: 4px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    padding: 0.5rem 1.2rem;
    transition: all 0.15s ease;
    width: 100%;
}
.stButton > button:hover {
    background: #ff5f1f;
    border-color: #ff5f1f;
    color: #fff;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(255,95,31,0.3);
}

/* Selectbox */
[data-testid="stSelectbox"] > div > div {
    background: #1a1a1a;
    border: 1px solid #333;
    color: #e8e8e8;
    font-family: 'JetBrains Mono', monospace;
}

/* Text inputs */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea {
    background: #1a1a1a !important;
    border: 1px solid #333 !important;
    color: #e8e8e8 !important;
    border-radius: 4px;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #ff5f1f !important;
    box-shadow: 0 0 0 1px #ff5f1f !important;
}

/* Info / success / error boxes */
.stSuccess { background: #0d2b1a !important; border-left: 3px solid #22c55e; }
.stError   { background: #2b0d0d !important; border-left: 3px solid #ef4444; }
.stInfo    { background: #0d1b2b !important; border-left: 3px solid #3b82f6; }
.stWarning { background: #2b200d !important; border-left: 3px solid #f59e0b; }

/* File list box */
.file-list {
    background: #141414;
    border: 1px solid #2a2a2a;
    border-radius: 6px;
    padding: 1rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    color: #a0a0a0;
    max-height: 220px;
    overflow-y: auto;
}
.file-list span { color: #ff5f1f; margin-right: 8px; }

/* Divider */
hr { border-color: #2a2a2a; }

/* Radio */
.stRadio > label { color: #a0a0a0; font-size: 13px; }
</style>
""", unsafe_allow_html=True)


# ── Helpers ───────────────────────────────────────────────────────────────────

def list_items() -> list[Path]:
    """Return all files and folders under cwd recursively."""
    return sorted(Path("").rglob("*"))


def render_file_list():
    items = list_items()
    if not items:
        st.info("No files or folders found in the current directory.")
        return
    lines = "".join(
        f"<span>{i+1}.</span>{item}<br>" for i, item in enumerate(items)
    )
    st.markdown(f'<div class="file-list">{lines}</div>', unsafe_allow_html=True)


# ── Layout ────────────────────────────────────────────────────────────────────

st.markdown("# 🗂️ File Manager")
st.markdown(f"`cwd: {Path.cwd()}`")
st.markdown("---")

OPERATIONS = [
    "📄 Create File",
    "📖 Read File",
    "✏️  Update File",
    "🗑️  Delete File",
    "🔁 Rename File",
    "📁 Create Folder",
    "❌ Delete Folder",
    "📄➕ Create File in Folder",
]

col_menu, col_main = st.columns([1, 2], gap="large")

with col_menu:
    st.markdown("### Operations")
    operation = st.radio("", OPERATIONS, label_visibility="collapsed")

with col_main:
    st.markdown("### Explorer")
    render_file_list()
    st.markdown("---")

    # ── Create File ──────────────────────────────────────────────────────────
    if operation == OPERATIONS[0]:
        st.markdown("#### Create File")
        fname = st.text_input("File name", placeholder="notes.txt")
        content = st.text_area("Content", placeholder="Type your content here…", height=150)
        if st.button("Create"):
            if not fname.strip():
                st.error("File name cannot be empty.")
            else:
                p = Path(fname.strip())
                if p.exists():
                    st.error(f"`{fname}` already exists.")
                else:
                    try:
                        p.write_text(content)
                        st.success(f"`{fname}` created successfully!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error: {e}")

    # ── Read File ────────────────────────────────────────────────────────────
    elif operation == OPERATIONS[1]:
        st.markdown("#### Read File")
        fname = st.text_input("File name", placeholder="notes.txt")
        if st.button("Read"):
            if not fname.strip():
                st.error("File name cannot be empty.")
            else:
                p = Path(fname.strip())
                if not p.exists():
                    st.error(f"`{fname}` not found.")
                elif p.is_dir():
                    st.error(f"`{fname}` is a folder, not a file.")
                else:
                    try:
                        text = p.read_text(encoding="utf-8")
                        st.markdown("**Contents:**")
                        st.code(text, language="text")
                    except Exception as e:
                        st.error(f"Error: {e}")

    # ── Update File ──────────────────────────────────────────────────────────
    elif operation == OPERATIONS[2]:
        st.markdown("#### Update File")
        fname = st.text_input("File name", placeholder="notes.txt")
        mode = st.radio("Mode", ["Overwrite", "Append"], horizontal=True)
        new_content = st.text_area("New content", height=150)
        if st.button("Update"):
            if not fname.strip():
                st.error("File name cannot be empty.")
            else:
                p = Path(fname.strip())
                if not p.exists():
                    st.error(f"`{fname}` not found.")
                elif p.is_dir():
                    st.error(f"`{fname}` is a folder.")
                else:
                    try:
                        write_mode = "w" if mode == "Overwrite" else "a"
                        with open(p, write_mode, encoding="utf-8") as f:
                            f.write(new_content)
                        st.success(f"`{fname}` updated ({mode.lower()})!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error: {e}")

    # ── Delete File ──────────────────────────────────────────────────────────
    elif operation == OPERATIONS[3]:
        st.markdown("#### Delete File")
        fname = st.text_input("File name", placeholder="notes.txt")
        if st.button("Delete", type="primary"):
            if not fname.strip():
                st.error("File name cannot be empty.")
            else:
                p = Path(fname.strip())
                if not p.exists():
                    st.error(f"`{fname}` not found.")
                elif p.is_dir():
                    st.error(f"`{fname}` is a folder. Use 'Delete Folder' instead.")
                else:
                    try:
                        p.unlink()
                        st.success(f"`{fname}` deleted.")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error: {e}")

    # ── Rename File ──────────────────────────────────────────────────────────
    elif operation == OPERATIONS[4]:
        st.markdown("#### Rename File")
        fname = st.text_input("Current file name", placeholder="old_name.txt")
        new_name = st.text_input("New file name", placeholder="new_name.txt")
        if st.button("Rename"):
            if not fname.strip() or not new_name.strip():
                st.error("Both fields are required.")
            else:
                p = Path(fname.strip())
                new_p = Path(new_name.strip())
                if not p.exists():
                    st.error(f"`{fname}` not found.")
                elif new_p.exists():
                    st.error(f"`{new_name}` already exists.")
                else:
                    try:
                        p.rename(new_p)
                        st.success(f"Renamed `{fname}` → `{new_name}`.")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error: {e}")

    # ── Create Folder ────────────────────────────────────────────────────────
    elif operation == OPERATIONS[5]:
        st.markdown("#### Create Folder")
        folder = st.text_input("Folder name", placeholder="my_folder")
        if st.button("Create Folder"):
            if not folder.strip():
                st.error("Folder name cannot be empty.")
            else:
                p = Path(folder.strip())
                if p.exists():
                    st.error(f"`{folder}` already exists.")
                else:
                    try:
                        p.mkdir(parents=True)
                        st.success(f"Folder `{folder}` created!")
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error: {e}")

    # ── Delete Folder ────────────────────────────────────────────────────────
    elif operation == OPERATIONS[6]:
        st.markdown("#### Delete Folder")
        folder = st.text_input("Folder name", placeholder="my_folder")
        force = st.checkbox("Force delete (removes non-empty folders)", value=False)
        if st.button("Delete Folder", type="primary"):
            if not folder.strip():
                st.error("Folder name cannot be empty.")
            else:
                p = Path(folder.strip())
                if not p.exists():
                    st.error(f"`{folder}` not found.")
                elif not p.is_dir():
                    st.error(f"`{folder}` is a file, not a folder.")
                else:
                    try:
                        if force:
                            import shutil
                            shutil.rmtree(p)
                        else:
                            p.rmdir()  # raises if non-empty
                        st.success(f"Folder `{folder}` deleted.")
                        st.rerun()
                    except OSError:
                        st.error(f"`{folder}` is not empty. Enable 'Force delete' to remove it.")
                    except Exception as e:
                        st.error(f"Error: {e}")

    # ── Create File in Folder ────────────────────────────────────────────────
    elif operation == OPERATIONS[7]:
        st.markdown("#### Create File in Folder")
        folder = st.text_input("Folder name", placeholder="my_folder")
        fname = st.text_input("File name", placeholder="notes.txt")
        content = st.text_area("Content", height=150)
        if st.button("Create"):
            if not folder.strip() or not fname.strip():
                st.error("Both folder and file name are required.")
            else:
                folder_p = Path(folder.strip())
                if not folder_p.exists():
                    st.error(f"Folder `{folder}` does not exist. Create it first.")
                elif not folder_p.is_dir():
                    st.error(f"`{folder}` is not a folder.")
                else:
                    p = folder_p / fname.strip()
                    if p.exists():
                        st.error(f"`{p}` already exists.")
                    else:
                        try:
                            p.write_text(content, encoding="utf-8")
                            st.success(f"`{p}` created!")
                            st.rerun()
                        except Exception as e:
                            st.error(f"Error: {e}")