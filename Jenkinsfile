pipeline {
    agent any

    environment {
        // Store your bot token securely in Jenkins credentials
        WEBEX_BOT_TOKEN = credentials('webex-bot-token')  
        WEBEX_ROOM_ID   = '09e40a50-8590-11f0-a6a6-01d219d77e7a'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/<your-username>/<your-repo>.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install -r requirements.txt || true'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'python3 -m unittest discover'
            }
        }
    }

    post {
        success {
            script {
                def message = "✅ Build SUCCESS for ${env.JOB_NAME} #${env.BUILD_NUMBER}"
                sh """
                curl -X POST \
                  -H "Authorization: Bearer ${WEBEX_BOT_TOKEN}" \
                  -H "Content-Type: application/json" \
                  -d '{"roomId":"${WEBEX_ROOM_ID}", "text":"${message}"}' \
                  https://webexapis.com/v1/messages
                """
            }
        }
        failure {
            script {
                def message = "❌ Build FAILED for ${env.JOB_NAME} #${env.BUILD_NUMBER}"
                sh """
                curl -X POST \
                  -H "Authorization: Bearer ${WEBEX_BOT_TOKEN}" \
                  -H "Content-Type: application/json" \
                  -d '{"roomId":"${WEBEX_ROOM_ID}", "text":"${message}"}' \
                  https://webexapis.com/v1/messages
                """
            }
        }
    }
}
