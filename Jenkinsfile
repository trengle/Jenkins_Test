pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh '''
                    docker pull python:3.11

                    docker run --rm \
                        -v $PWD:/app \
                        -w /app \
                        python:3.11 \
                        bash -c "pip install pytest"
                '''
            }
        }

        stage('Test') {
            steps {
                // add -q to run pytest in quiet mode
                sh '''
                    docker run --rm \
                        -v $PWD:/app \
                        -w /app \
                        python:3.11 \
                        bash -c "pytest"
                '''
            }
        }
    }
}
