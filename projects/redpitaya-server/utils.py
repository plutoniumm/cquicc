import subprocess;

def getParams(path:str):
    params = {};
    if '?' in path:
        params = path.split('?')[1].split('&');
        params = {x.split('=')[0]:x.split('=')[1] for x in params};
    return params;

def cli(command:str):
    print("Running command: ",command)
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