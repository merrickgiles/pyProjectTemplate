You need to create a virtual environment, then install whatever your dependencies are by running pip install -r requirements.txt.

You may (or may not) have to run pip install -e (within your virtual environment) to get the modules working. I'm neurotic and like to work in parallel paths, and I find working with the modules in a pyproject less bothersome than modifying the path. But you do you.
