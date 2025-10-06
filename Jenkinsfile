pipeline {
  /* Opción SIN Docker (usa Python disponible en el agente) */
  agent any
  options { 
    timestamps()

    buildDiscarder(logRotator(numToKeepStr: '10'))
  }
  stages {
    stage('Preparar venv') {
      steps {
        sh 'python3 --version || python --version'
        sh 'python3 -m venv .venv || python -m venv .venv'
        sh '. .venv/bin/activate && pip install --upgrade pip && pip install -r requirements.txt'
      }
    }
    stage('Tests') {
      steps {
        sh 'mkdir -p reports'
        sh '. .venv/bin/activate && PYTHONPATH=$PWD pytest --junitxml=reports/junit.xml --cov=src --cov-report=xml:reports/coverage.xml --cov-report=term-missing'
      }
      post {
        always {
          junit 'reports/junit.xml'
          // publishCoverage adapters: [coberturaAdapter('reports/coverage.xml')]
          // cobertura coberturaReportFile: 'reports/coverage.xml', onlyStable: false, failUnhealthy: false, failUnstable: false
          archiveArtifacts artifacts: 'reports/**', fingerprint: true, onlyIfSuccessful: false
        }
      }
    }
  }
}
