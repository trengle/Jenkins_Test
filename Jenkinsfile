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
                sh 'docker pull python:3.11'
            }
        }

        stage('Lint') {
            steps {
                sh '''
                    docker run --rm \
                        -v $PWD:/app \
                        -w /app \
                        python:3.11 \
                        bash -c "pip install black && black --check ."
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                    docker run --rm \
                        -v $PWD:/app \
                        -w /app \
                        python:3.11 \
                        bash -c "pip install pytest && pytest -q"
                '''
            }
        }

        stage('Package') {
            steps {
                sh '''
                    docker build -t funcs-app .
                '''
            }
        }

        // stage('Deploy') {
        //     steps {
        //         sh '''
        //             # login
        //             aws ecr get-login-password --region us-west-1 \
        //                 | docker login --username AWS --password-stdin <your-account-id>.dkr.ecr.us-west-1.amazonaws.com

        //             # tag and push
        //             docker tag funcs-app:latest <your-account-id>.dkr.ecr.us-west-1.amazonaws.com/funcs-app:latest
        //             docker push <your-account-id>.dkr.ecr.us-west-1.amazonaws.com/funcs-app:latest
        //         '''
        //     }
        // }
    }
}
