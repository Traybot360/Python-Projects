from termcolor import colored

def hanoi(a, b, c, disks):
    if disks == 1:
        print('-------------------------')
        print('Move disk ' + colored('1','cyan') +' from ' + colored(a,'green') + ' to ' + colored(c,'magenta') + '.')
        return
    elif disks > 1:
      hanoi(a, c, b, disks - 1)
      print('Move disk ' + colored(disks,'magenta') +' from ' + colored(a,'cyan') + ' to ' + colored(c,'green') + '.')
      hanoi(b, a, c, disks - 1)
    else:
      print('-------------------------')
      print(colored('Number must be => 1','red'))
      print('-------------------------')

disks = 0
while disks < 1:   
  disks = int(input('Enter number of disks: '))
  hanoi('A', 'B', 'C', disks)
