pipeline {
    agent any

    parameters {
        string(defaultValue: '17', description: 'Enter a number:', name: 'number')
    }

    stages {
        stage('Run Python Script') {
            steps {
                script {
                    sh """
                    python3 -c '
number = 21
if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
                    '
                    """
                }
            }
        }
    }
}
# build using the parametes 

