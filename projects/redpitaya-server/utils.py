import subprocess;

def cli(command:str):
    print(f"Running command: {command}")
    try:
        result = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            shell=True,
            text=True,
            universal_newlines=True
        );
        out, error = result.communicate();

        if result.returncode != 0:
            return False, error;
        else:
            return True, out;
    except Exception as e:
        print("EXPLOSIONN")
        return False, e;