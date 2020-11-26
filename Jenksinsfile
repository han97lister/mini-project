pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh "chmod +x test.sh"
                sh "./scripts/test.sh"
            }
        }
        stage('Build') {
            steps {
                sh "chmod +x build.sh"
                sh "./scripts/build.sh"
            }
        }
        stage('Push') {
            steps {
                sh "chmod +x push.sh"
                sh "./scripts/push.sh"
            }
        stage('Deploy') {
            steps {
                sh "chmod +x deploy.sh"
                sh "./scripts/deploy.sh"
            }
        }
    }
}