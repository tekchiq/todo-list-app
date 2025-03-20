pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'python -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh '. venv/bin/activate && python -m unittest discover -s tests'
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo Deploying Flask Todo App...'
                sh 'nohup . venv/bin/activate && python app.py &'
            }
        }
    }
}
