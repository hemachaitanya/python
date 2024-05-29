pipeline{
    agent {
        label "name"
    }
    stages{
        stage('clean up'){
            steps{
                script{
                    def process_name = "<process name>"
                    def output = sh(ReturnStdout = true, script: "ps -ef | grep -v grep |grep ${process name} | awk '{print$2}'").trim() 
                    def processIds = processList.split('\n')
                    for (pid in processIds){
                        sh "kill -9 ${pid}"
                        sh "echo "kill the processIds ${pid}""
                    }
                }
            }
        }
    }
}