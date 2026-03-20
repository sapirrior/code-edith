import subprocess

def execute(command: str) -> str:
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=60
        )
        stdout = result.stdout.strip()
        stderr = result.stderr.strip()
        
        output = []
        if stdout:
            output.append(stdout)
        if stderr:
            output.append(f"Error/Warning: {stderr}")
        
        if not output:
            return f"Command '{command}' executed successfully with no output."
        return "\n".join(output)
    except Exception as e:
        return f"Execution Error: {str(e)}"
