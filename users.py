################################################################################
# Find the range of user ids assigned to regular users
################################################################################
uid_min = None
uid_max = None

with open('/etc/login.defs', 'r') as x:
    for line in x:
        if uid_min is None and line.startswith("UID_MIN"):
            uid_min = int(line.split()[-1])
        if uid_max is None and line.startswith("UID_MAX"):
            uid_max = int(line.split()[-1])

if uid_min is None:
    print("UID_MIN is undefined in /etc/login.defs, using 1000")
    uid_min = 1000

if uid_max is None:
    print("UID_MAX is undefined in /etc/login.defs, using 60,000")
    uid_max = 60000

################################################################################
# Print user details for each UID in the range detected above
################################################################################

def print_user(user: str, passwd: str, uid: int, gid: int, name: str, 
        homedir: str, shell: str):
    print(f'user:\t{user}')
    print(f'pass:\t{passwd}')
    print(f'uid: \t{uid}')
    print(f'gid: \t{gid}')
    print(f'name:\t{name}')
    print(f'home:\t{homedir}')
    print(f'shell:\t{shell}')


print("Printing real user accounts:")
with open('/etc/passwd', 'r') as x:
    for line in x:
        user, passwd, uid, gid, name, homedir, shell = line.split(':')
        uid = int(uid)
        gid = int(gid)
        if uid >= uid_min and uid <= uid_max:
            print_user(user, passwd, uid, gid, name, homedir, shell)
            input("Press Enter to show the next user...")
