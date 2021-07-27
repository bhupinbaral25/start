from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/prime/<int:num>")
def prime(num):
    count=0
    for i in range(num):
        if num % (i+1) == 0:
            count = count+1
    if count==2:
        results={ 
            "Number": num,
            "result": True
        }
    else:
         results={ 
            "Number": num,
            "result": False
        }
    return jsonify(results)

if __name__=='__main__':
    app.run(debug=True)