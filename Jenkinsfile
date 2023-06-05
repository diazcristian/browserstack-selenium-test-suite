pipeline {
  agent any
  stages {
    stage('Setup') {
       script {
          def secretsFile = readFile 'secrets.yml'
          def secrets = readYaml text: secretsFile

          secrets.each { secret ->
            environment[secret.name] = secret.value
        }
        sh 'python3 -m venv bsenv'
        sh '''
        source bsenv/bin/activate
        pip3 install -r requirements.txt
        python3 scripts/parallel.py
        '''
      }
    }
  }
}
