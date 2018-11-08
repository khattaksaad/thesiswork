glove:
	wget -P ./data/ "https://nlp.stanford.edu/data/glove.840B.300d.zip"
	unzip ./data/glove.840B.zip -d data/glove.840B/
	rm ./data/glove.840B.zip

run:
	python build_data.py
	python train.py
	python evaluate.py
