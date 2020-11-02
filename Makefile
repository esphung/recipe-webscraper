all:
	make clean
	make run
clean:
	rm -rf *.pysc
	rm -rf data.json
	rm -rf __pycache__
run:
	python3 main.py
