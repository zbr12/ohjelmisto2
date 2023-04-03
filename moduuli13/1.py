from flask import Flask, request

app = Flask(__name__)
@app.route('/alkuluku/<luku>')
def alkuluku(luku):
    luku = int(luku)
    alkuluku = 1
    for i in range(2, luku):
        if luku%i == 0:
            alkuluku = 0
            break
    if alkuluku == 1:
        vastaus = {
            "Number" : luku, 
            "isPrime" : "true"
        }
    else:
        vastaus = {
            "Number" : luku, 
            "isPrime" : "false"
        }
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)