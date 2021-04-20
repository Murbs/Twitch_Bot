import subprocess

callBot = "pipenv run python bot.py"
subprocess.Popen('cmd.exe /K cd <FILEPATH TO BOT GOES HERE>')
subprocess.run(callBot, shell=True)