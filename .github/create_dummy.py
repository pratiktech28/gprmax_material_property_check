import h5py
import numpy as np
with h5py.File('material_test.out', 'w') as f:
    g = f.create_group('src_0')
    # Ek sin wave daal dete hain jo hamare ref_trace se match kare
    data = np.sin(np.linspace(0, 10, 100))
    g.create_dataset('Ez', data=data)
print("Dummy material_test.out created!")