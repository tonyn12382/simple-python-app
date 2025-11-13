pipeline {
    agent any

    environment {
        BOT_TOKEN = "MDM1MzBlMTQtZTUwYi00MmU1LTk3YTItOWZlZTFmYTRkN2I1OTFlMDcyNGQtYWMy_P0A1_e58072af-9d57-4b13-abf7-eb3b506c964d"
        ROOM_ID   = "09e40a50-8590-11f0-a6a6-01d219d77e7a"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/tonyn12382/simple-python-app.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }

        stage('Notify WebEx') {
            steps {
                powershell """
                \$headers = @{
                    'Authorization' = 'Bearer ${env.BOT_TOKEN}'
                    'Content-Type' = 'application/json'
                }
                \$body = @{
                    roomId = '${env.ROOM_ID}'
                    text   = '✅ Jenkins build for branch ${env.BRANCH_NAME} completed successfully.'
                } | ConvertTo-Json

                Invoke-RestMethod -Uri 'https://webexapis.com/v1/messages' -Method Post -Headers \$headers -Body \$body
                """
            }
        }
    }

    post {
        failure {
            powershell """
            \$headers = @{
                'Authorization' = 'Bearer ${env.BOT_TOKEN}'
                'Content-Type' = 'application/json'
            }
            \$body = @{
                roomId = '${env.ROOM_ID}'
                text   = '❌ Jenkins build FAILED for branch ${env.BRANCH_NAME}.'
            } | ConvertTo-Json

            Invoke-RestMethod -Uri 'https://webexapis.com/v1/messages' -Method Post -Headers \$headers -Body \$body
            """
        }
    }
}
