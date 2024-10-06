Task 1: Set Up a Simple HTML Project
Create a Simple HTML Project
Create a basic HTML file (e.g., index.html) and save it locally. 
Initialize a Git Repository
In the project directory, run the following commands to initialize a Git repository:
git init
git add .
git commit -m "Initial commit"
Push to GitHub
Create a new repository on GitHub
Push the local repository to GitHub:
git remote add origin https://github.com/yourusername/html-cicd-demo.git
git push -u origin master
Task 2: Set Up an AWS EC2/Local Linux Instance with Nginx
Launch an EC2 Instance (or Local Linux Machine)
For AWS EC2: Use the AWS console to launch a new EC2 instance running Ubuntu.
Install Nginx
Run the following commands on the EC2 instance or Linux machine to install Nginx:
sudo apt update
sudo apt install nginx -y
Start and Enable Nginx
Ensure Nginx is running and enabled to start on boot:
sudo systemctl start nginx
sudo systemctl enable nginx
Verify Nginx
Open the public IP address of your instance in a browser to verify that the default Nginx page is displayed.
Task 3: Write a Python Script to Check for New Commits
Install Python and GitHub API Library
Make sure Python is installed on the server and install the requests library:
sudo apt install python3 python3-pip -y
pip3 install requests
Create the Python Script
Create a file called cicdppl.py. This script will check for new commits in the GitHub repository using the GitHub API:
Make the Python Script Executable
Set the correct permissions on the Python script:
chmod +x cicdppl.py
Task 4: Write a Bash Script to Deploy the Code
Create a Bash Script to Deploy the Code
Create a file called cicdppl.sh. This script will clone the latest code from GitHub and restart Nginx:
Make the Bash Script Executable
Set the correct permissions on the bash script:
chmod +x cicdppl.sh
Task 5: Set Up a Cron Job to Run the Python Script
Edit Crontab
Open the cron job scheduler by running:
crontab -e
Add the Python Script to Crontab
Add the following line to the crontab to run the Python script every 5 minutes:
*/5 * * * * /usr/bin/python3 /path/to/check_commits.py >> /var/log/deploy.log 2>&1
This will run the Python script every 5 minutes and log output to /var/log/deploy.log.
Task 6: Test the Setup
Make a New Commit to the GitHub Repository
Modify your index.html file locally, and push the changes to the GitHub repository:
git add index.html
git commit -m "Updated HTML content"
git push origin master
Verify Automatic Deployment
After a few minutes, check the server to see if the new code has been deployed.
You can monitor the deployment process by checking the log file:
cat /var/log/deploy.log
