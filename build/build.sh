rm -r ShellPy
mkdir ShellPy
cp -R ../Configuration/ ShellPy/
cp -R ../Engine/ ShellPy/
cp -R ../Shells/ ShellPy/
python setup.py install
pip install .
rm -r ShellPy
rm -r build
rm -r dist
rm -r ShellPy.egg-info
sleep 7
