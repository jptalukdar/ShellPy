mkdir ShellPy
copy  ../Configuration ShellPy
copy ../Engine ShellPy
copy ../Shells ShellPy
python setup.py install
pip install .
pause