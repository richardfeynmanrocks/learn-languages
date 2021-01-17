#include <cuda_runtime_api.h>
#include <cuda.h>
#include <iostream>
#include <math.h>
#include <eigen3/Eigen/Dense>
// Kernel function to add the elements of two arrays
__global__
void add(int n, Eigen::MatrixXf *x, Eigen::MatrixXf *y, Eigen::MatrixXf *z)
{
    int index = blockIdx.x * + blockDim.x + threadIdx.x;
    int stride = blockDim.x * gridDim.x;  
    for (int i = index; i < n; i+=stride)
        z[i] = x[i] * y[i];
}

int main(void)
{
    int N = 10000;
    Eigen::MatrixXf *x, *y, *z, *z2;

    // Allocate Unified Memory – accessible from CPU or GPU
    cudaMallocManaged((void**)&x, N*sizeof(Eigen::MatrixXf));
    cudaMallocManaged((void**)&y, N*sizeof(Eigen::MatrixXf));
    cudaMallocManaged((void**)&z, N*sizeof(Eigen::MatrixXf));

    // initialize x and y arrays on the host
    for (int i = 0; i < N; i++) {
        x[i] = Eigen::MatrixXf::Random(100,100);
        y[i] = Eigen::MatrixXf::Random(100,100);
    }

    int blockSize = 256;
    int numBlocks = (N + blockSize - 1) / blockSize;
    // Run kernel on 1M elements on the GPU
    add<<<numBlocks, blockSize>>>(N, x, y, z);

    // Wait for GPU to finish before accessing on host
    cudaDeviceSynchronize();

    // Free memory
    cudaFree(x);
    cudaFree(y);
  
    return 0;
}
