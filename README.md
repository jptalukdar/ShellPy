# ShellPy
ShellPy allows you to create and run custom shell where each statement is processed by your custom python functions

## Goal
To create an shell program that allows remote access with Authentication and encryption.
Each statement in the shell will be evaluated by user written python code with a separation with os shell

## Usage
Create any python script

```python
from ShellPy.Engine.Commands import commandsManager
@commands.add('echo') #echo or the name of the command you want to perform
def handlemytool(context): # A context object will be passed. Context object contains important information about the statement executed 
    return context.get('params') # params gives you the parameters pass with the command
```
commandsManager allows you to evaluate commands and perform action on them

```python
from ShellPy.Shells import shellManager
shellManager.runShellEngine()
```
This initialises and executes the shell

## Build
You can build and install the package by executing build.sh or build.bat inside folder build
This assumes you have python3 as the default python
