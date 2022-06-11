from typing import Tuple
from subprocess import Popen, STDOUT, PIPE

TEST_RUNS: Tuple[bytes] = (
    b"abc@abv.bg\n",
    b"peter@gmail.com\npetergmail.com\n",
    b"peter@gmail.hotmail\n",
    b"peter@gmail.hotmail@\n",
)

for test_run in TEST_RUNS:
    with Popen(
        ["python", "Email_Validator.py"], stdout=PIPE, stdin=PIPE, stderr=STDOUT
    ) as proc:
        print(proc.communicate(test_run)[0].decode())
