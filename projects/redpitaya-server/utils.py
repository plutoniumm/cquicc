import subprocess;
from commands import check_scpi;

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

def run_scpi():
    try:
        running = check_scpi();
    except Exception as e:
        return False, "Unable to check if SCPI is running";

    if running:
        return True, "SCPI Server already running";

    success, out = cli("systemctl enable redpitaya_scpi");
    print("CLI", success, out);
    if not success:
        return False, "Unable to enable scpi service";
    else:
        return True, "SCPI Service enabled";
