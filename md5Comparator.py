import requests
import hashlib
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('url1', metavar='<url1>', help='The first url to compare')
parser.add_argument('url2', metavar='<url2>', help='The second url to compare')
args = parser.parse_args()

hash1 = hashlib.md5(requests.get(args.url1).content).hexdigest()
hash2 = hashlib.md5(requests.get(args.url2).content).hexdigest()

print(args.url1+': '+hash1)
print(args.url2+': '+hash2)

if hash1 == hash2:
  print("\nHashes are IDENTICAL (Someone reposted)")
else:
  print("\nHashes are DISTINCT")
