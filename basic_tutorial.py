import streamlit as st 


# Text / Title
st.title("Streamlit Tutorials.")
st.title("This is a Title")

# Header / Subheader
st.header("This is a header")
st.subheader("This is a Subheader")


# Text
st.text("Hellp Streamlit... using text function")
st.write("Hellp Streamlit... using write function")


# Markdown
st.markdown("### This is a Markdown")

# Error / Colorful Text messages
st.success("Successful Message")

st.info("Information Message")

st.warning("Warning Message")

st.error("Error / Danger Message")

st.exception("NameError ('name three not defined.')")

# Get help info about python
st.help(range)

# Writing Text (Super function)
st.write("Text with Write")
st.write(range(10))

# Images
# from PIL import Image
# img = Image.open('airplane1.jpg')
# # st.image(img) # Original size
# st.image(img, width =300, caption = "Simple Airplane Image") # restrict the size

# Videos Files
# vid_file = open("File_Name.mp4", "rb").read()
# # vid_bytes = vid_file.read()
# st.video(vid_file)

# Audio Files
# aud_file = open("File_Name.mp3", "rb").read()
# st.audio(aud_file, format = 'audio/mp3')


# Widgets
# Checkbox
st.checkbox("Option 1")

if st.checkbox("Show/Hide"):
	st.text("Showing or Hiding Widget")

# Radio Button
st.radio("Select Gender", ("Male", "Female","Others"))

status = st.radio("What is your status", ("Active", "Inactive"))
if status == "Active":
	st.success("Cool you are Active")
else:
	st.warning("Oops... seems you are Inactive now. Please select Active")

# Select Box / Dropdown
occupation = st.selectbox("Select Occupation", ["Programmer", "Data Scientist", "Doctor", "Business", "Other"])

st.write("You selected ", occupation)


# MultiSelect 
multiSel = st.multiselect("Select your skills", ("SQL Server", "Oracle", "Python", "Medical", "Finance")) # Either Tuple or List is accepted.
st.write("You choose total of ", len(multiSel), " skills.")
st.write("Selectd skills are : ", multiSel)

# Slider
level = st.slider("What is your level", 1, 10)

# Buttons
st.button("Simple Button") # Simple button, no action

if st.button("About"):  # Button with some action.
	st.text("You selected About button")

# Receive text input / keyboard inputs
firstname = st.text_input("Enter Your First Name :", "Type here...")
st.write("Welcome ", firstname)

lastname = st.text_input("Enter Your Last Name :", "Type here...")
if st.button("Submit"):
	result = lastname.title() # Will convert the text into title case.
	st.success(result)


# Text Area
message = st.text_area("Enter Your Message :", "Type here...")
if st.button("Submit1"):
	result = message.title() # Will convert the text into title case.
	st.info(result)

# Date Input
import datetime
today = st.date_input("Today is ", datetime.datetime.now())

# Time
tm = st.time_input("The time is ", datetime.time())

# DIsplay JSON
st.text("Display JSON")
st.json({'name':"Mayank", 'gender':"Male", 'age': '36'})

# DIsplay Raw Code
st.text("DIsplay Raw Code")
st.code("import numpy as np")


with st.echo():
	# This will also show all the comments along with code.
	import pandas as pd 
	df = pd.DataFrame() # This is to import Empty Data Frame
	# This is displaying raw code using "st.echo()"



# Progress Bar
# import time
# my_bar = st.progress(0)
# for i in range(10):
# 	my_bar.progress(i + 1)


# Spinner
# with st.spinner("Waiting .."):
# 	time.sleep(5)

# st.success("Finished!")


# Balloons
# st.balloons()


# Sidebars
st.sidebar.header("About")
st.sidebar.text("This is a Streamlit Tutorial")

# Functions
# def run_functions():
# 	return range(100)

# st.write(run_functions())	

@st.cache	# This will cachle it
def run_functions2():
	return range(100)

st.write(run_functions2())	


# Plots
st.pyplot()


# DataFrames
st.dataframe(df)

# Tables
st.table(df)

