pipeline {
  agent any
  stages {
    stage('Setup') {
      steps {
        configFileProvider([configFile(fileId: 'secrets', targetLocation: 'secrets.yml')]) {
          script {
            def secrets = readYaml file: 'secrets.yml'
            env.BROWSERSTACK_USERNAME = secrets.secrets.find { it.name == 'BROWSERSTACK_USERNAME' }.value
            env.BROWSERSTACK_ACCESS_KEY = secrets.secrets.find { it.name == 'BROWSERSTACK_ACCESS_KEY' }.value
            env.BROWSER_STACK_EMAIL = secrets.secrets.find { it.name == 'BROWSER_STACK_EMAIL' }.value
            env.BROWSER_STACK_PW = secrets.secrets.find { it.name == 'BROWSER_STACK_PW' }.value
          }
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
