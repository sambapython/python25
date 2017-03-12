import logging
logging.basicConfig(filename="log2.txt",format="%(asctime)s->%(levelname)s->%(message)s", level=logging.DEBUG)
import paramiko as pmk
ssh=pmk.SSHClient()
ssh.set_missing_host_key_policy(pmk.AutoAddPolicy())
ssh.connect("localhost",username="samba-python",password="samba")
stdin,stdout,stderr = ssh.exec_command("ps -aux")
logging.info("running command: ps -aux")
err = stderr.read()
if err:
	logging.error(err)
else:
	logging.debug(stdout.read())