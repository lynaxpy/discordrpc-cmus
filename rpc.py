import discordrpc
from subprocess import check_output as cmd
from time import sleep, time
rpc = discordrpc.RPC(app_id=0000000000000000000)
start_time = time
button = discordrpc.Button(
  button_one_label="GitHub",
  button_one_url="https://github.com/lynaxpy",
  button_two_label="Repository",
  button_two_url="https://github.com/lynaxpy/discordrpc-cmus"
  )

while True:
    try:
        rpc.set_activity(
            act_type=2,
            state="cmus player",
            details=cmd("playerctl metadata title", shell=True, text=True).split(".mp3")[0],
            buttons=button,
            )
    except: rpc.set_activity(
            act_type=2,
            state="cmus player",
            details="Not Playing",
            buttons=button,
            )
    finally: sleep(5)
rpc.run()
