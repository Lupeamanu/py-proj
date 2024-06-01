# TODO
## Automated Python Project Creator

### Current:
- [ ] Parse args from command line
  - example: python main.py  My-Project 3.11.4
    - Should create a python project with the name My-Project using a virtual environment with python version 3.11.4
    - Python version should be optional. Default to 3.11.4
- [ ] Using args from user, create a directory with the project's name
- [ ] If a python version is specified in CLI, create venv with that version of python
- [ ] Else, create a venv using the default version of python
- [ ] Once creation of project is done, automatically activate venv

### Future features:
- [ ] Add cli argument for users to pass requirements.txt if dependencies are known for the project to automatically install dependencies