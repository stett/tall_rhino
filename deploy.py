#!/usr/bin/env python
import os
import sys
import signal
import re
import subprocess
import time
import pyinotify

# This function tries to retrieve an environment
# variable. If it doesn't exist, it raises an exception.
def get_env_var(var_name):
    try:             return os.environ[var_name]
    except KeyError: raise Exception('The "%s" environment variable must be set before running deploy' % var_name)

# Get environment variables and set constants
BASE_DIR = os.path.realpath(os.path.join(os.path.realpath(__file__), '../'))
PROJECT_NAME = get_env_var('PROJECT_NAME')
PROJECT_ROOT = BASE_DIR#os.path.join(os.path.dirname(os.path.realpath(__file__)), PROJECT_NAME)
PROJECT_MANAGER = os.path.join(PROJECT_ROOT, 'manage.py')
SUPERVISOR_PROCESS = get_env_var('SUPERVISOR_PROCESS_NAME')
MIN_DEPLOYMENT_TIME = 3


print PROJECT_MANAGER

# Any newly changed file which matches one of the
# regular expressions in the IGNORED_FILES list will not
# invoke a redeployment when deploy is watching.
IGNORED_FILES = [
    r'^.*~$',
    r'^.*\.pyc$',
    r'^.*\/log',
    r'^.*\/env',
    r'^.*\/\.git',
    r'^.*\/CACHE\/.*$',
]

# If a changed file matches a regex corresponding to a
# specific deployment specifier, then the deployment
# processes for that specifier will be run.
DEPLOYMENT_SPECIFIERS = {
    'static': [ r'^.*\.css$', r'^.*\.less$', r'^.*\.sass$', r'^.*\.html$', r'^.*\.js$' ],
    'documentation': [ r'^.*\/doc\/.*\.rst$' ],
    'dynamic': [ r'^.*\.py$', r'^.*\.sh$' ],
}


# Run all deploy processes corresponding to the
# deployment specifiers in specs. By default, all
# specifiers are included.
def deploy(specs=DEPLOYMENT_SPECIFIERS.keys(), files=[]):

    #
    print('Deploying: %s' % BASE_DIR)

    # Get a list of files to deploy
    files = []
    for path, subdirs, fnames in os.walk(BASE_DIR):
        files += [os.path.join(path, fname) for fname in fnames]

    if 'static' in specs:

        # Compile collected .less files to css
        #print('Compiling LESS files')
        #less_files = [f for f in files if re.match(r'^.*\.less$', f)]
        #for less_file in less_files:
        #    css_file = '%s.css' % os.path.splitext(less_file)[0]
        #    print('Generating %s' % css_file)
        #    subprocess.call(['lessc', less_file, css_file])

        # Run staticfile collection
        print('Collecting static files')
        subprocess.call([PROJECT_MANAGER, 'collectstatic', '--noinput'])

        print('Compressing static files')
        subprocess.call([PROJECT_MANAGER, 'compress'])


    #if 'documentation' in specs:

        # Compile RST files to HTML
        #print('Compiling RST documentation to HTML')
        #rst_files = [f for f in files if re.match(r'^.*\/doc\/.*\.rst$', f)]
        #for rst_file in rst_files:
        #    html_file = '%s.html' % os.path.splitext(rst_file)[0]
        #    print('Generating %s' % html_file)
        #    subprocess.call(['rst2html5', rst_file, html_file])


    
    if 'dynamic' in specs:

        pass
        # Run unit tests
        #print('Running unit testRunning unit tests')
        #subprocess.call([PROJECT_MANAGER, 'test'])

        # Restart supervisor
        #print('Restarting supervisor process: %s' % SUPERVISOR_PROCESS)
        #subprocess.call(['sudo', 'supervisorctl', 'restart', SUPERVISOR_PROCESS])

    #
    print('Finished deploying: %s' % BASE_DIR)


def file_changed(f=None):

    # Check to see if it's been more than a few seconds since
    # the last deployment... don't want to re-deploy too quickly
    if time.time() - deploy.last_deployment_time <= MIN_DEPLOYMENT_TIME: return

    # Check to see if this file should be ignored
    for pattern in IGNORED_FILES:
        if re.match(pattern, f.pathname):
            return

    # Print the file changed message
    print('File changed: %s' % f.pathname)

    # Find the specific deployment specification.
    specs = []
    for spec in DEPLOYMENT_SPECIFIERS:
        for pattern in DEPLOYMENT_SPECIFIERS[spec]:
            if re.match(pattern, f.pathname):
                specs.append(spec)

    # Run the deployment
    if len(specs) > 0:
        deploy(specs)
        deploy.last_deployment_time = time.time()


def ignore_path(path):
    for pattern in IGNORED_FILES:
        if re.match(pattern, path):
            return True
    return False


def sigint_handler(signal, frame):
    print('Killing the notifier...')
    deploy.notifier.stop()
    deploy.watch_manager.close()
    sys.exit(0)


def watch():
    print('Watching for changes in %s' % PROJECT_ROOT)
    signal.signal(signal.SIGINT, sigint_handler)
    mask = pyinotify.IN_MODIFY | pyinotify.IN_DELETE
    deploy.watch_manager = pyinotify.WatchManager()
    deploy.watch_manager.add_watch(
        path = PROJECT_ROOT,
        mask = mask,
        proc_fun = file_changed,
        rec = True,
        auto_add = True)
    deploy.notifier = pyinotify.Notifier(deploy.watch_manager)
    deploy.notifier.loop()


deploy.last_deployment_time = 0
deploy.watch_manager = None
deploy.notifier = None

if __name__ == "__main__":
    if '-w' in sys.argv:
        watch()
    else:
        deploy()
