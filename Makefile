.PHONY: all

all:
	python update_timestamp.py
	git commit -a 
