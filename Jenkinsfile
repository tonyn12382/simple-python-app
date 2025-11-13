pipeline {
    agent any

    environment {
        WEBEX_BOT_TOKEN = 'MDM1MzBlMTQtZTUwYi00MmU1LTk3YTItOWZlZTFmYTRkN2I1OTFlMDcyNGQtYWMy_P0A1_e58072af-9d57-4b13-abf7-eb3b506c964d'
        WEBEX_ROOM_ID   = '09e40a50-8590-11f0-a6a6-01d219d77e7a'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/tonyn12382/simple-python-app.git'
            }
        }

        stage('Setup Virtualenv') {
            steps {
                sh '''
                # Create a virtual environment
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt || true
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh '''
                . venv/bin/activate
                python -m unittest discover -s tests -p "test_*.py"
                '''
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
