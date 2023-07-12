#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jackp
#
# Created:     12-07-2023
# Copyright:   (c) jackp 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import streamlit as st
from langchain.vectorstores import FAISS
import tempfile
from io import StringIO
#from InstructorEmbedding import INSTRUCTOR
#from langchain.embeddings import HuggingFaceInstructEmbeddings


#@st.cache_resource
#def instructor_embeddings():
#    instructor_embed = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-base", model_kwargs={"device": "cpu"})
#    return instructor_embed

#def ori_data(_file):
#    db = FAISS.load_local(f"/{file.name}", embed)
#    st.success('Database succussfully created!', icon="✅")
#    return db

#embed = instructor_embeddings()
newdb = None
file = st.file_uploader("Choose a file")
if file is not None:
    # To read file as bytes:
    #3newdb = ori_data(file)
    bytes_data = file.getvalue()
    with tempfile.TemporaryFile() as fp:
        fp.write(bytes_data)
    #fp.write(file)
    fp.read()
    st.write(fp)


#if newdb:
#    query = st.text_input("what?")
#    dd = db.similarity_search(query)
#    st.write = (dd)
