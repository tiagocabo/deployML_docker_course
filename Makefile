
venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install --no-cache-dir -r requirements.txt # more safer to avoid conflicts with existing packages on cache
	touch venv/bin/activate

clean:
	rm -rf venv
	rm -rf .idea/

	find -iname "*.pyc" -delete

docker_init:
	sudo docker build -t rf_api .
	sudo docker run -p 5000:5000 --name rf_api rf_api

docker_stop:
	echo "deleting existing docker..."
	sudo docker stop rf_api
	sudo docker rm rf_api


