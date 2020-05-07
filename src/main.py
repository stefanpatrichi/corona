# imports

import schedule
import time

from get_json import get_json
from cases import write_cases
from plot import plot

# main function

def main():
    get_json()
    write_cases()
    plot()

main()
