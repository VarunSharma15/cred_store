pipeline
{
	agent any
	stages{
		stage("running the python script....")
		{
			steps{
				script{
					def sout = new StringBuffer();
					def serr = new StringBuffer();
					def cmdarray=["python", "C:\\Users\\vs255034\\OneDrive - Teradata\\Desktop\\new\\findingip.py"]
					def ip=cmdarray.execute()
					ip.consumeProcessOutput(sout, serr);
					ip.waitForProcessOutput();
					def actualOut= sout.toString();
					print(actualOut)
					}
				}
		}
	}
}
