############################################################################
# Environment Setup (Python)
############################################################################

# 1. Install Python (this should automatically install pip)
#   https://devguide.python.org/#status-of-python-branches
#
#   - D:\workspace> python --version
#   Python 3.9.5
#    (TODO - Steps on Ubuntu)

# 2. Create a folder

# 3. Install virtualenv
#   - D:\workspace> pip install virtualenv

# 4. Setup virtualenv
#   - D:\workspace> mkdir training.python (project directory)
#   - D:\workspace\learning.python> cd training.python
#   - D:\workspace\learning.python> mkdir .tpvenv (will contain environment,
#       typically .venv)
#   - D:\workspace\learning.python> virtualenv -p
#       C:\Python39\python.exe .tpvenv
#   - Note: If "virtualenv" not found then the "PATH" environment variable
#   isn't setup right. Check what that looks like ( "echo %PATH%" ) and \
#   update it to include the one you intalled ( typically under "Program Files"
#   or the user's "AppData" folders ). For example -
#  C:\Users\satviks\Desktop\Python\workspace\training.python>echo %PATH%
#        E:\openjdk-11.0.2_windows-x64_bin\jdk-11.0.2\bin;E:\openjdk-11.0.2_windows-x64_bin\jdk-11.0.2\bin;C:\Program Files\Python38\Scripts\;C:\Program Files\Python38\;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\WINDOWS\System32\OpenSSH\;C:\Program Files\PuTTY\;C:\Program Files\nodejs\;C:\Program Files\TortoiseGit\bin;C:\Program Files (x86)\GitExtensions\;C:\Program Files\apache-ant-1.10.14\bin;C:\Program Files\apache-maven-3.9.5;C:\Program Files (x86)\CheckPoint\Endpoint Security\Endpoint Common\bin;C:\Program Files\Git\cmd;E:\sonar-scanner-cli-4.6.2.2472-windows\sonar-scanner-4.6.2.2472-windows\bin;C:\Users\satviks\AppData\Roaming\Python\Python38\site-packages\virtualenv\;C:\Users\satviks\AppData\Roaming\Python\Python38\Scripts;C:\Users\satviks\AppData\Local\Programs\Python\Python312\Scripts\;C:\Users\satviks\AppData\Local\Programs\Python\Python312\;E:\sonarqube-9.3.0.51899;C:\Users\satviks\AppData\Local\Programs\Microsoft VS Code\bin;E:\sonarqube-9.3.0.51899\bin;E:\openjdk-11.0.2_windows-x64_bin\jdk-11.0.2
#
#   - karand@Karand-Laptop:~/workspace/training.python$ virtualenv -p
#       /usr/bin/python3.9 .tpvenv

# 5. Activate and deactivate environment
#   - (.tpvenv) D:\workspace\training.python>.tpvenv\Scripts\activate
#   - ... do your thing ...
#   - (.tpvenv) D:\workspace\training.python>.tpvenv\Scripts\deactivate
#   - D:\workspace\training.python>
#
#   - karand@Karand-Laptop:~/workspace/training.python$ source
#   .tpvenv/bin/activate

# 6. When different Python version to be used, simply create another folder
#   and repeat steps 4 and 5.

# 7. Version
#   (.tpvenv) D:\workspace\training.python\project-regex\regex>python
#   --version
#   Python 3.9.5

# 8. VSCode
#   - python extension
#   - pylint extension
#   - settings.json
#   - pylint - https://pypi.org/project/pycodestyle/
