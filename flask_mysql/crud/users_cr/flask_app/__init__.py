from flask import Flask
app = Flask(__name__)
app.secret_key = 'My Secret Key! SHHHHH'

#import multiprocessing as mp
#print('CPUs:', mp.cpu_count())