import subprocess
import os

def run_command(command):
    """Run a command in the shell and print the output."""
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate()
    if process.returncode != 0:
        print(f"Error running command: {command}")
        print(err.decode('utf-8'))
    else:
        print(out.decode('utf-8'))

def update_github_project():
    """Update the GitHub project from the local computer."""
    # Path to your project directory
    project_directory = r"C:\Users\NAYIF\Desktop\Tabnotificiation\project\SocietyManagementSystem\ResidentialManagementSystemMAIN\ResidentialManagementSystemMAIN"

    # Change to the project directory
    os.chdir(project_directory)

    # Check the status of the repository
    run_command("git status")

    # Stage changes
    run_command("git add .")

    # Commit changes with a message
    commit_message = "Your commit message here"
    run_command(f"git commit -m \"{commit_message}\"")

    # Pull the latest changes from the remote repository
    branch_name = "main"  # Change this if you are using a different branch
    run_command(f"git pull origin {branch_name}")

    # Push changes to GitHub
    run_command(f"git push origin {branch_name}")

if __name__ == "__main__":
    update_github_project()
