"""Fingerprint for fixed classroom text."""

import hashlib


def demo_fingerprint():
    return hashlib.sha256(b"session-3-lab").hexdigest()
