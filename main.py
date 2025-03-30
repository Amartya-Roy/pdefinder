"""
Module: main.py
This module provides a command-line interface for running the PDE discovery pipeline.
"""

import argparse
from pdefinder import run_pde_finder

def main():
    parser = argparse.ArgumentParser(description="Run PDE-FIND discovery.")
    parser.add_argument('--dataset', type=str, default='KS', help="Dataset name (e.g., 'KS', 'Burgers', 'chafee-infante')")
    parser.add_argument('--P', type=int, default=5, help="Maximum polynomial power to include in the candidate library")
    parser.add_argument('--D', type=int, default=5, help="Maximum derivative order to include in the candidate library")
    parser.add_argument('--epochs', type=int, default=1000, help="Number of optimization epochs")
    
    args = parser.parse_args()
    run_pde_finder(dataset=args.dataset, P=args.P, D=args.D, num_epochs=args.epochs)

if __name__ == "__main__":
    main()
