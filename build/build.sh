rm -r ShellPy
mkdir ShellPy
cp -R ../Configuration/ ShellPy/
cp -R ../Engine/ ShellPy/
cp -R ../Shells/ ShellPy/
python setup.py install
pip install .
sleep 7