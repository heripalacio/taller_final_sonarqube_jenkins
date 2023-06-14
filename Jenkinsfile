pipeline {
    agent any
    
    triggers {
        // Configurar el trigger para que se dispare al recibir un POST
        httpRequestTrigger(credentialsId: 'jenkins-credentials', 
                           serverPort: 8080, 
                           method: 'POST')
    }
    
    stages {
        stage('Compile') {
            steps {
                // Compilar el proyecto aquí
                sh 'python compile_script.py'
            }
        }
        
        stage('Unit Test') {
            steps {
                // Ejecutar pruebas unitarias
                sh 'python unit_test_script.py'
                
                // Verificar el resultado de las pruebas
                script {
                    def unitTestResult = sh(returnStatus: true, script: 'python check_unit_test_result.py')
                    if (unitTestResult == 0) {
                        echo 'Las pruebas unitarias pasaron correctamente.'
                    } else {
                        error 'Las pruebas unitarias fallaron. Consulta los detalles del error.'
                    }
                }
            }
        }
        
        stage('Code Coverage') {
            steps {
                // Cargar el reporte de cobertura (jacoco, por ejemplo)
                sh 'python load_coverage_report.py'
            }
        }
        
        stage('SonarQube Analysis') {
            steps {
                // Desplegar la aplicación en SonarQube
                withSonarQubeEnv('SonarQubePruebas'){
                    sh 'python deploy_sonarqube.py'
                }
                
            }
        }
    }
}

