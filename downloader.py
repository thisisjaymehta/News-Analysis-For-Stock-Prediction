import gdown

url = 'https://drive.google.com/uc?id=1W_A6BcSRbHY1Yc-J4WBJt4Qq0Jraa4hR'
output = 'nlp_model.h5'
gdown.download(url, output, quiet=False)
