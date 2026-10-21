"""Render an explicit immutable image into the deployment; no cluster changes."""
import argparse
from pathlib import Path
import re

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--image', required=True)
args = parser.parse_args()
if not re.fullmatch(r'rotezsolutions/nginx-devops-assignment@sha256:[0-9a-f]{64}', args.image):
    parser.error('Use the published rotezsolutions image with its full sha256 digest')
source = Path(__file__).resolve().parents[1] / 'k8s/deployment.yaml'
print(source.read_text().replace('nginx-devops-app:release-required', args.image), end='')
