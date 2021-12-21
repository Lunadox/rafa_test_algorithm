import argparse

args = argparse.ArgumentParser(description="Ludox's Argparse Pratics")

# args.add_argument('-q','--quit',required=False)
args.add_argument('-x','--xval',type=int,required=False)

argvar = vars(args.parse_args())

pass