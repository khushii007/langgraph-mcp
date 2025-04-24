pipeline {
    agent any

    environment {
        LANGSMITH_API_KEY = credentials('langsmith-api-key')
        OPENAI_API_KEY = credentials('openai-api-key')
        GITHUB_PERSONAL_ACCESS_TOKEN = credentials('github-token')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/khushii007/langgraph-mcp.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip install --user -r requirements.txt'
                    sh 'pip install .'
                    sh 'pip install --user pytest'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh 'export PATH=$PATH:$HOME/.local/bin && pytest'
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    // Optional: You can add any build steps here if needed (e.g., Docker build)
                    echo "Building the project (optional)"
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Add your deploy steps here (e.g., Docker deployment, or any cloud API)
                    echo "Deploying to production"
                }
            }
        }
    }
    
    post {
        always {
            echo 'Cleaning up...'
            cleanWs()  // Optional: Clean up workspace after the build
        }
    }
}
