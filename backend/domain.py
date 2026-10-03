import csv, hashlib, io, json, math, re
from datetime import datetime, timezone
from urllib.request import Request, urlopen
from .validation import validate_input, http_url, unique

def now(): return datetime.now(timezone.utc).isoformat()
def validate(data,records): return initialize(validate_input(data,CONFIG['example']),records)

def initialize(row,records):
    if row['level'] not in ['DEBUG','INFO','WARN','ERROR']: raise ValueError('Invalid log level')
    return dict(row,ingested_at=now())
def summary(rows): return {level:sum(r['level']==level for r in rows) for level in ['DEBUG','INFO','WARN','ERROR']}
def transition(row,action): raise ValueError('Log events are immutable')
