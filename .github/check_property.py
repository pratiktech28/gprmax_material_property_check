import numpy as np
import h5py
import argparse
import sys

def get_nrmse(sim_data, ref_data):
    """
    NRMSE Calculation: Root Mean Square Error divided by Range.
    """
    rmse = np.sqrt(np.mean((sim_data - ref_data)**2))
    data_range = np.max(ref_data) - np.min(ref_data)
    
    if data_range == 0:
        return rmse
        
    return rmse / data_range

def main():
    parser = argparse.ArgumentParser(description='GPRMax Physics Validation Tool')
    
    parser.add_argument('--input', type=str, required=True, 
                        help='Input HDF5 file path')
    parser.add_argument('--threshold', type=float, default=0.01, 
                        help='Maximum allowed NRMSE error')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    try:
        # 1. Load Data
        with h5py.File(args.input, 'r') as f:
            if 'src_0/Ez' in f:
                sim_trace = f['src_0/Ez'][:]
            else:
                first_key = list(f.keys())[0]
                sim_trace = f[first_key + '/Ez'][:]

        # 2. Reference Data 
        ref_trace = np.sin(np.linspace(0, 10, len(sim_trace))) 

        # 3. Calculation
        error_val = get_nrmse(sim_trace, ref_trace)

        print("-" * 30)
        print(f"Validation Result")
        print(f"NRMSE: {error_val:.6f}")
        print(f"Threshold: {args.threshold}")
        print("-" * 30)

        # 4. Final Verdict
        if error_val <= args.threshold:
            print("Status: PASS ✅")
            sys.exit(0)
        else:
            print("Status: FAIL ❌ (Error too high)")
            sys.exit(1)

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
