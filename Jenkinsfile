pipeline {
    agent any

    triggers { githubPush() }        
    
    environment {
        DJANGO_SETTINGS_MODULE = "hotel_project.test_settings"
        VENV_DIR = ".venv"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "✅ Checking out code"
                checkout scm
            }
        }

        stage('Setup Virtualenv') {
            steps {
                echo "✅ Setting up virtual environment"
                bat """
                    python -m venv %VENV_DIR%
                    call %VENV_DIR%\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Run Migrations') {
            steps {
                echo "✅ Running migrations"
                bat """
                    call %VENV_DIR%\\Scripts\\activate
                    python manage.py migrate
                """
            }
        }

        stage('Run Tests with Coverage') {
            steps {
                echo "✅ Running pytest with coverage"
                bat """
                    call %VENV_DIR%\\Scripts\\activate
                    pytest --cov=hotel --cov-report=term-missing --cov-report=html
                """
            }
        }
    }

    post {
        always {
            echo "📦 Pipeline finished"
        }
        success {
            echo "✅ All steps completed successfully"
        }
        failure {
            echo "❌ Pipeline failed"
        }
    }
}
