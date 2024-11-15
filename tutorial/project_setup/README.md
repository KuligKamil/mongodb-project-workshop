## Project Setup
### Please READ ME in preview mode or on Github 👀
### We kindly recommend to disable Copilot or any similar AI-driven tools for response generation for this workshop. 🤬

1. Fork & Clone the source code
   
2. Next go to the `mongodb-project-workshop` directory

3. Ensure you are using **Python Version 3.11** **or Higher.** We are using Python 3.11.9 for our project.


  HINT: if you need to manage multiple versions of Python we recommend to use **pyenv** 

  [https://github.com/pyenv/pyenv](https://github.com/pyenv/pyenv)
  
  For example:

  `pyenv install 3.11.9`


4. Setup environment. 
  
<aside>

  HINT: we recommend to use pyenv virtualenv  with PDM - Python package and dependency manager 
  
  [https://github.com/pyenv/pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)
  
  [https://pdm-project.org/latest/](https://pdm-project.org/latest/)

  <details>
  <summary>how to use pyenv virtualenv  & pdm</summary>

  create env named mongo-project-workshop-3.11.9

  `pyenv virtualenv 3.11.9 mongo-project-workshop-3.11.9`
  
  `pyenv local mongo-project-workshop-3.11.9`

  install pdm 

  `pip install pdm`

  install all dependencies

  `pdm install`

  run ruff check 

  `pdm run ruff check` 

  if you see `All checks passed!` everything setup correctly 🎉

  </details>
</aside>



 you can use old good `venv` [https://docs.python.org/3/library/venv.html](https://docs.python.org/3/library/venv.html)
 

  <details>
  <summary>how to use `venv`</summary>

  create `venv`

  `python -m venv .`

  next activate it

  on mac, linux or WSL

  `source ./bin/activate`

  or on windows 

  * cmd.exe

  `C:\> .\Scripts\activate.bat`

  * PowerShell

  `PS C:\> .\Scripts\Activate.ps1`

  run ruff check

  `run ruff check`

  if you see `All checks passed!` everything setup correctly 🎉

  </details>
 

5. Create file with environment variables `.envrc` file or `.env` file

* Set the `MONGODB_URI` variable in `.envrc` to for your database connection (It will be shown in the next step, how to get the variables)
* Set the `PYTHONPATH` variable in `.envrc` to your project path
   in mac, linux & WSL `export PYTHONPATH=$PWD`
   in windows [link for tutorial](https://www.youtube.com/watch?v=PXqcHi2fkXI)

### That’s it! You’re ready to work! 🎉🎉🎉
