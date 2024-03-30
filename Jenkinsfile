pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = '797d7ca8-2746-4f09-88f6-c1ec903c7e2d' // Jenkins credentials ID for Docker Hub login
        DOCKER_IMAGE_NAME = 'umoo/flask-app' // Docker image name
        DOCKERFILE_PATH = 'Dockerfile' 
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("umoo/flask-app", "-f ${env.DOCKERFILE_PATH} .")
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', env.DOCKER_HUB_CREDENTIALS) {
                        docker.image(env.DOCKER_IMAGE_NAME).push('latest')
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Docker image build and push successful!'
        }
        failure {
            echo 'Docker image build or push failed!'
        }
    }
}
