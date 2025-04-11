# py_allergy_parser_app

Steps for building buildozer.spec on Apple Silicon:
1. cd to root of project directory
> cd /path/to/project

2. Build the Dockerfile:
> docker build -t buildozer-local .

3. Run an interactive session on the buildozer-local image and build the spec

> docker run -it --rm -v $PWD:/app -e BUILDOZER_ALLOW_ROOT=1 buildozer-local buildozer init