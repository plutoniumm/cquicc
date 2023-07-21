import subprocess;
from commands import check_scpi;

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
    running = check_scpi();
    if running:
        return True, "SCPI Server already running";

    success, out = cli("systemctl enable redpitaya_scpi");
    if not success:
        return False, "Unable to enable scpi service";

    if "Created symlink" in out:
        return True, "SCPI Service enabled";
    else:
        return False, "Unable to enable scpi service";
