import streamlit as st
import os
st.title('Virtual Try On');
# input1 = st.file_uploader("Upload input image", type= ("png","jpg", "jpeg"))
# if input1:
#     st.image(input1, width=200, caption='Input image')
# input2 = st.file_uploader("Upload target clothing", type= ("png","jpg", "jpeg"))
# if input2:
#     st.image(input2, width=200, caption='Target image')


def file_selector(folder_path='.',key=1, title = 'Select a model'):
    filenames = os.listdir(folder_path)
    selected_filename = st.sidebar.selectbox(title, filenames,key=str(key))
    return os.path.join(folder_path, selected_filename)
filename = file_selector('./inputs/model/', key =1, title= 'Select a model')
filename1 = file_selector('./inputs/clothes/', key =2, title = 'Select cloth' )
submit = st.sidebar.button('Swap Clothes')

if filename:
    # st.write('You selected `%s`' % filename)
    st.image(filename, width=150, caption='Model')


if filename1:
    # st.write('You selected `%s`' % filename)
    st.image(filename1, width=150, caption='Cloth')


if filename and filename1 and submit:
    # os.sys('./run_smartfit.sh inputs/person_1.jpg inputs/clothing_1.jpg')
    os.system('./run_smartfit.sh '+ filename + ' '+ filename1)
    st.image('./output/output.png', width=150, caption='VITON')