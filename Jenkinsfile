pipeline{
    agent {label 'DEV'}
    tools {
        maven 'MAVEN-3.9.6'
    }
    stages{
        stage('git checkout'){
            steps{
                git url: " https://github.com/spring-projects/spring-petclinic.git",
                    branch: "main"
            }
            input {
                message "Should we continue?"
                ok "Yes, we should."
                submitter "alice,bob"
                parameters {
                    string(name: 'PERSON', defaultValue: 'Mr Jenkins', description: 'Who should I say hello to?')
                }
            }
        }
       stage('build') {
            steps {
                sh "mvn clean package"
            }

            when {
                branch 'main'
                beforeInput true
            }
            }
    }

}