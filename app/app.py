import os
import sys
from flask import Flask, render_template, request, session
from argparse import Namespace

from calculate_this_readability import main as main
app = Flask(__name__)
# app.secret_key = 'crytographyisnotmystrongsuit'
app.secret_key = os.urandom(24)

#  set the max file size to 20mb.  If an ecoli fasta is
#    larger than this, then its probably not an e coli
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024


@app.route("/", methods=['GET','POST'])
def index():
    session["FINISHED"] = False
    session["LOADED"] = False
    in_text = ""
    if request.method == 'POST':
        print(request.form.__dict__)
        if request.form['submitupload'] == "analyze" :
            # for secure filenames. Read the documentation.
            in_text = request.form["textinput"].replace('"', '').replace("'", '')
            in_text = " ".join(in_text.split("\n"))
            print(in_text)
            teaser = in_text
            header = "Here is the first bit of your file:"
            session["LOADED"] = True
            results = main(args=[in_text, None])
            print(results)
            ###   Now lets run the main function
            profile = ""
            ###
            return render_template(
                'index.html',
                header=header,
                teaser=teaser,
                content=teaser,
                results=results,
                profile=profile
            )
        else:
            pass
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
