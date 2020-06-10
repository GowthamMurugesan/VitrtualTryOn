import streamlit as st
import os
st.title('Virtutal Try On');
# input1 = st.file_uploader("Upload input image", type= ("png","jpg", "jpeg"))
# if input1:
#     st.image(input1, width=200, caption='Input image')
# input2 = st.file_uploader("Upload target clothing", type= ("png","jpg", "jpeg"))
# if input2:
#     st.image(input2, width=200, caption='Target image')


def file_selector(folder_path='.',key=1):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames,key=str(key))
    return os.path.join(folder_path, selected_filename)

filename = file_selector('./inputs', key =1)
if filename:
    st.write('You selected `%s`' % filename)
    st.image(filename, width=200, caption='Input image')

filename1 = file_selector('./inputs', key =2 )
if filename1:
    st.write('You selected `%s`' % filename)
    st.image(filename1, width=200, caption='Input image')

submit = st.button('Swap Clothes')

if submit:
    # os.sys('./run_smartfit.sh inputs/person_1.jpg inputs/clothing_1.jpg')
    os.system('./run_smartfit_gowtham.sh '+ filename + ' '+ filename1)
    st.image('./output/output.png', width=200, caption='Input image')