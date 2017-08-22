import pickle


cities = ["Paris", "Dijon", "Lyon", "Strasbourg"]
fh = open("data.pkl", "rb")
for inline in fh:
    print inline

fh.close()