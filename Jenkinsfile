pipeline {
    agent none 
    stages {

        stage('Build') {
            agent {
                docker { image 'python:3.8-alpine3.16' } 
            }
            steps {
                sh 'python3.8 -m py_compile sources/prog.py sources/calc.py'
                stash(name: 'compiled-results', includes: 'sources/*.py*')
                echo "Webhook Test erfolgreich!"

            }
        }

        stage('Test') {
            agent {
                docker { image 'grihabor/pytest' }
            }
            steps {
                sh 'pytest -v --junit-xml test-reports/results.xml sources/test_calc.py'
            }
            post {
                always {
                    junit "test-reports/results.xml" 
                }
            }
        }

        stage('Deliver') {
            agent any 
            environment {
                VOLUME = "${env.WORKSPACE}/sources:/src"
                IMAGE = 'cdrx/pyinstaller-linux'
            }
            steps {
                dir(path: env.BUILD_ID) {
                    unstash(name: 'compiled-results')
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'pyinstaller -F prog.py'"
                }
            }
            post {
                success {
                    // Jenkins ist schlau genug, das Muster im gesamten Workspace zu finden
                    archiveArtifacts "**/sources/dist/prog"
                    // Aufräumen des spezifischen Build-Ordners
                    sh "rm -rf ${env.BUILD_ID}"
                }
            }
        }
        stage('Branch Info') {
            steps { echo "Du arbeitest gerade auf dem Branch: ${env.BRANCH_NAME}" }
        }

    } // Ende von stages
} // Ende von pipeline