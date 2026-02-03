pipeline {
    agent any

    stages {
        stage('Run Python Tests') {
            steps {
                sh '''
                    docker run --rm \
                        -v $PWD:/app \
                        -w /app \
                        python:3.11 \
                        python test_funcs.py
                '''
            }
        }
    }
}
