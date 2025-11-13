pipeline {
    agent any

    environment {
        BOT_TOKEN = "NGZhZWIxMDAtMGU4OC00NTUwLThmZTQtYmQ3MWY1MTZmODM2NDRlODY3NGItYjVl_P0A1_e58072af" // your real bot token
        ROOM_ID   = "54c143f0-c03f-11f0-8ba9-e9128841882b" // your room ID
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/tonyn12382/simple-python-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Make sure Python is installed in the container
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Notify WebEx') {
            steps {
                script {
                    def message = "✅ Jenkins build for branch ${env.BRANCH_NAME} completed successfully."
                    sh """curl -s -X POST \
                        -H "Authorization: Bearer ${BOT_TOKEN}" \
                        -H "Content-Type: application/json" \
                        -d '{ "roomId": "${ROOM_ID}", "text": "${message}" }' \
                        https://webexapis.com/v1/messages"""
                }
            }
        }
    }

    post {
        failure {
            script {
                def failMessage = "❌ Jenkins build FAILED for branch ${env.BRANCH_NAME}."
                sh """curl -s -X POST \
                    -H "Authorization: Bearer ${BOT_TOKEN}" \
                    -H "Content-Type: application/json" \
                    -d '{ "roomId": "${ROOM_ID}", "text": "${failMessage}" }' \
                    https://webexapis.com/v1/messages"""
            }
        }
    }
}
