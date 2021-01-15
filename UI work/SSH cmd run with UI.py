import subprocess
import sys
import PySimpleGUI as sg
from paramiko import SSHClient

client = SSHClient()
client.load_system_host_keys()
#client.connect(' should be the host here ', username='  ', password='  ')

def main():
    layout = [  [sg.Text('Enter a command:')],
                [sg.Input(key='_IN_')],             # input field to type a command
                [sg.Output(size=(60,15))],          # an output area where commands are printed out
                [sg.Button('Run'), sg.Button('Exit')] ]     # buttons

    window = sg.Window("Amir's terminal", layout)


    while True:             # loop
        event, values = window.Read()
        if event in (None, 'Exit'):         # if i want to exit
            break

        if event == 'Run':                  # the two lines of code needed to get button and run command
            runCommand(cmd=values['_IN_'], window=window)

    window.Close()

def runCommand(cmd, timeout=None, window=None):   # This function runs the actual  command
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ''
    for line in p.stdout:
        line = line.decode(errors='replace' if (sys.version_info) < (3, 5) else 'backslashreplace').rstrip()
        output += line
        print(line)
        window.Refresh() if window else None
    retval = p.wait(timeout)
    return (retval, output)

if __name__ == '__main__':
    main()





