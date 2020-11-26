pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh "chmod +x /scripts/test.sh"
                sh "./scripts/test.sh"
            }
        }
        stage('Build') {
            steps {
                sh "chmod +x /scripts/build.sh"
                sh "./scripts/build.sh"
            }
        }
        stage('Push') {
            steps {
                sh "chmod +x /scripts/push.sh"
                sh "./scripts/push.sh"
            }
        }    
        stage('Deploy') {
            steps {
                sh "chmod +x /scripts/deploy.sh"
                sh "./scripts/deploy.sh"
            }
        }
    }
}