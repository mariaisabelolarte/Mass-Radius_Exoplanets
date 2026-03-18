#!/bin/bash
set -e

wget -q -O datos_exoplanetas.csv "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=SELECT+pl_name,pl_rade,pl_bmasse+FROM+ps+WHERE+pl_rade+IS+NOT+NULL+AND+pl_bmasse+IS+NOT+NULL&amp;format=csv"

python3 constructor_db.py

python3 analisis_visual.py
