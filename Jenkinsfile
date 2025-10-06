pipeline {
  /* Opción recomendada: usar contenedor Docker con Python 3.11 */
  agent { 
    docker { 
      image 'python:3.11-slim'
      args '-u root'  /* ejecutar como root para instalar paquetes si hiciera falta */
    } 
  }
  options { 
    timestamps()
    ansiColor('xterm')
    buildDiscarder(logRotator(numToKeepStr: '10'))
  }
  stages {
    stage('Preparar entorno') {
      steps {
        sh 'python --version'
        sh 'pip install --upgrade pip'
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Tests') {
      steps {
        sh 'mkdir -p reports'
        sh 'PYTHONPATH=$PWD pytest --junitxml=reports/junit.xml --cov=src --cov-report=xml:reports/coverage.xml --cov-report=term-missing'
      }
      post {
        always {
          junit 'reports/junit.xml'
          /* Si tienes el plugin Cobertura instalado, publica la cobertura.
             Si no lo tienes aún, instala "Cobertura" o "Coverage" y descomenta una de las siguientes:
          */
          // publishCoverage adapters: [coberturaAdapter('reports/coverage.xml')]
          // cobertura coberturaReportFile: 'reports/coverage.xml', onlyStable: false, failUnhealthy: false, failUnstable: false
          archiveArtifacts artifacts: 'reports/**', fingerprint: true, onlyIfSuccessful: false
        }
      }
    }

    /* ====== Plantillas de etapas opcionales (deja comentadas hasta tener pruebas) ====== */

    // stage('Pruebas API (Postman/Newman)') {
    //   agent { docker { image 'node:20-alpine' } }
    //   steps {
    //     sh 'npm i -g newman'
    //     sh 'newman run api/coleccion.postman_collection.json -e api/entorno.postman_environment.json --reporters cli,junit --reporter-junit-export reports/newman.xml'
    //   }
    //   post { always { junit 'reports/newman.xml' } }
    // }

    // stage('E2E Web (Cypress)') {
    //   agent { docker { image 'cypress/included:13.6.6' } }
    //   steps {
    //     sh 'cypress run --headless'
    //     // Para guardar reportes JUnit, añade un reporter JUnit en la conf de Cypress o usa mochawesome + transform
    //   }
    // }

  }
  post {
    always {
      echo "Build finalizado. Revisa pestañas: Console Output, Test Result y (si configuraste) Coverage."
    }
  }
}
