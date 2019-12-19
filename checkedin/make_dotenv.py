import sys
from datetime import datetime
from os import path


def make_dotenv_file(force=False):
    if path.isfile('.env') and not force:
        print('.env file exists, skipping.\n' +
              'Run with -f to override your current file.')
        return

    env_params = []
    with open('checkedin/settings.py') as fp:
        l = fp.readline()
        while l:
            if 'os.getenv' in l:
                env_params.append(l[l.index('(')+2:l.index(')')-1])
            l = fp.readline()

    f = open('.env', 'w')
    f.write('#\n# Generated at ' + str(datetime.now()) + '\n#\n')
    for param in env_params:
        f.write(param + '=\n')
    f.close()

    print('Generated .env file with ' + str(len(env_params)) + ' env params.')


if __name__ == '__main__':
    force = False
    if '-f' in sys.argv:
        force = True
    make_dotenv_file(force=force)
