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
#import streamlit as st
#from langchain.vectorstores import FAISS
#import tempfile
#from io import StringIO
#from InstructorEmbedding import INSTRUCTOR
#from langchain.embeddings import HuggingFaceInstructEmbeddings


#@st.cache_resource
#def instructor_embeddings():
#    instructor_embed = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-base", model_kwargs={"device": "cpu"})
#    return instructor_embed

#def ori_data(file):
#    db = FAISS.load_local(file, embed)
#    st.success('Database succussfully created!', icon="✅")
#    return db

#embed = instructor_embeddings()
#newdb = None
#file = st.file_uploader("Choose a file")
#if file is not None:
#    # To read file as bytes:
#    #3newdb = ori_data(file)
#    bytes_data = file.getvalue()
 #   stringio = StringIO(file.getvalue().decode("utf-8"))
#    with tempfile.TemporaryFile() as fp:
#        fp.write(stringio)
        #fp.write(file)
#        fp.read()
 #       newdb = ori_data(fp)
#        st.write(fp)


#if newdb:
#    query = st.text_input("what?")
#    dd = db.similarity_search(query)
#    st.write = (dd)
import streamlit as st
from langchain.vectorstores import FAISS
from io import BytesIO
from InstructorEmbedding import INSTRUCTOR
from langchain.embeddings import HuggingFaceInstructEmbeddings


@st.cache_resource
def instructor_embeddings():
    instructor_embed = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-base", model_kwargs={"device": "cpu"})
    return instructor_embed

import tempfile

def ori_data(file):
    with tempfile.NamedTemporaryFile(delete=False) as temp:
        temp.write(file.read())
        temp_path = temp.name
    db = FAISS.load_local(temp_path, embed)
    st.success('Database succussfully created!', icon="✅")
    return db

embed = instructor_embeddings()
newdb = None
file = st.file_uploader("Choose a file", type="faiss")
if file is not None:
    # To read file as bytes:
    bytes_data = file.getvalue()
    # Use BytesIO instead of StringIO
    bytesio = BytesIO(bytes_data)
    # Pass BytesIO object to ori_data function
    newdb = ori_data(bytesio)


if newdb:
    query = st.text_input("what?")
    # Use newdb instead of db
    dd = newdb.similarity_search(query)
    st.write(dd)
