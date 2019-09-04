import subprocess
import os
for i in range(0, 9999):
	s = str(i).zfill(4)
	subprocess.run(["qpdf.exe", f"-password={s}", '-decrypt', 'test.pdf', 'result.pdf'])
	if os.path.exists('result.pdf'):
		print(s)
		exit(0)
