import streamlit as st
from langchain.vectorstores import FAISS
from io import BytesIO
from InstructorEmbedding import INSTRUCTOR
from langchain.embeddings import HuggingFaceInstructEmbeddings
import tempfile
import zipfile

@st.cache_resource
def instructor_embeddings():
    instructor_embed = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-base", model_kwargs={"device": "cpu"})
    return instructor_embed

def ori_data(file_zip):
    with tempfile.TemporaryDirectory() as temp_dir:
        # Extract files from zip
        with zipfile.ZipFile(file_zip, 'r') as zip_ref:
            zip_ref.extractall(temp_dir)
        
        db = FAISS.load_local(temp_dir, embed)
        st.success('Database succussfully created!', icon="✅")
    return db

embed = instructor_embeddings()
newdb = None

# Upload .zip file
file_zip = st.file_uploader("Choose a .zip file", type="zip")

if file_zip is not None:
    bytes_data_zip = file_zip.getvalue()
    bytesio_zip = BytesIO(bytes_data_zip)

    newdb = ori_data(bytesio_zip)

if newdb:
    query = st.text_input("what?")
    # Use newdb instead of db
    dd = newdb.similarity_search(query)
    st.write(dd)
