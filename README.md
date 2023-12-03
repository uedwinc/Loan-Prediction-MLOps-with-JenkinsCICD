## CI/CD Pipeline for Machine Learning

- Build a CI/CD pipeline to deploy ML models in production
- Integrate GitHub with Jenkins, 
- Run the tests using Jenkins’s job and generate a test summary in Jenkins
- Build a Docker image, and run a Docker container using Jenkins
- Integrate Jenkins with an email account to get the status of the build and deployment.

### Tools and Technologies
[jenkins]() [docker]() [github]()

### Installing Jenkins

- Follow instructions here for Ubuntu: https://www.jenkins.io/doc/book/installing/linux/#debianubuntu

- Then do the following:

- Confirm Jenkins is running:
    ```
    systemctl status jenkins
    ```
- If it is not running, you can start jenkins using:
    ```
    sudo systemctl start jenkins
    ```
- Open up port 8080 on the jenkins server security group on AWS and launch jenkins web UI with the IP address and port

- Now, add the Jenkins user to the Docker group:
    ```
    sudo usermod -aG docker jenkins
    ```

- For me, I will just launch the jenkins web UI used in the [jenkins project]()

### Building the CI/CD Pipeline

1. Develop the Codebase

- See directory structure for the codebase here: [link]

- Create [main.py]() file to run FastAPI app (fastAPI requires python 3.6+)

- Create the [requirements.txt]() file

- Create [Dockerfile]()

2. Create a Personal Access Token (PAT) on GitHub

- PATs are an alternative to using passwords for authentication to GitHub Enterprise Server when using the GitHub API or the command line.

- See instructions here: https://docs.github.com/en/enterprise-server@3.4/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens

- To generate or regenerate your PAT, you can go to Settings | Tokens (login required): https://github.com/settings/tokens

- If you are not prompted for your username and password, your credentials may be cached in your machine.

3. Create a webhook on the GitHub repository

- Go to your GitHub repo | Settings | Webhooks.

    - For me: https://github.com/uedwinc/Loan-Prediction-MLOps-with-JenkinsCICD/settings/hooks

- Provide a payload URL (http://jenkins-ip:8080/github-webhook/)

- Select the Content type as an application/json format. The Secret field is optional. Let’s leave it blank for now.

- Check 'Just the push event' and click to Add Webhook.

4. Configure Jenkins for Webhook and Email Integration

- Install Git. Github and Email Extension plugins

5. Create CI/CD pipeline using Jenkins