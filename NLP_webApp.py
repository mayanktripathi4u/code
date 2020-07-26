import streamlit as st

# NLP packages
import spacy
import en_core_web_sm
from textblob import TextBlob
from gensim.summarization import summarize 

def text_analyzer(my_text):
	# nlp = spacy.load('en') # for me linking or shortcut not available

	nlp = en_core_web_sm.load()

	docx = nlp(my_text)

	# tokens = [token.text for token in docx]
	allData = [('"Tokens" : {}, \n"Lemma" : {}'.format(token.text, token.lemma_)) for token in docx]
	return allData

def entity_analyzer(my_text):
	nlp = en_core_web_sm.load()

	docx = nlp(my_text)

	entities = [(entity.text, entity.label_) for entity in docx.ents]

	return entities	

# pkgs




def main():
	""" NLP App with Streamlit """
	st.title("NLP Web App")
	st.subheader("Natural Language Processing on the web")

	# Tokenization
	if st.checkbox("Show Tokens and Leema"):
		st.subheader("Tokenize your Text")
		message = st.text_area("Enter Your Text","Type here...")

		if st.button("Analyze"):
			# st.success(message.title())
			nlp_result = text_analyzer(message)
			st.json(nlp_result)

	# Named Entity
	if st.checkbox("Show Named Entities"):
		st.subheader("Extract entities from your Text")
		message = st.text_area("Enter Your Text","Type here...")

		if st.button("Extract"):
			# st.success(message.title())
			nlp_result = entity_analyzer(message)
			st.json(nlp_result)

	# Sentiment Analysis
	if st.checkbox("Show Sentiment Analysis"):
		st.subheader("Sentiment of your Text")
		message = st.text_area("Enter Your Text","Type here...")

		if st.button("Analyze"):
			blob = TextBlob(message)
			result_sentiment = blob.sentiment
			st.success(result_sentiment)

	# Test Summarization
	if st.checkbox("Show Text Summarization"):
		st.subheader("Enter your Text")
		message = st.text_area("Enter Your Text","Type here...")

		options = st.selectbox("Choice your summarizer", ("gensim","sumy"))

		if st.button("summarize"):
			if options == 'gensim':
				st.text("Using Gensim....")
				summary_result = summarize(message)
				st.success(summary_result)

			# elif options == 'sumy':
			# 	st.text("Using Gensim....")
			# 	summary_result = summarize(message)

			# To work with sumy summarizer we have to install various other packages.. skipping for now.
		# st.text("Done!!")


	st.sidebar.subheader("About the App")
	st.sidebar.text("NLP App with Streamlit")

	st.sidebar.info("Made by Mayank using Streamlit")




if __name__ == '__main__':
	main()	