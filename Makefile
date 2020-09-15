
venv: venv/bin/activate

venv/bin/activate: requirements.txt
	test -d venv || python3 -m venv .venv
	. .venv/bin/activate; pip install --no-cache-dir -Ur requirements.txt
	touch .venv/bin/activate

clean:
	rm -rf .venv
	rm -rf .vscode/
	find -iname "*.pyc" -delete
