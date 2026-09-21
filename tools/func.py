from subprocess import run

# run a command in cmd
def run_command(command:str) -> int:
    try:
        run(command, shell=True)
        return 0
    except:
        return 1