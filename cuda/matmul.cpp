#include <eigen3/Eigen/Dense>

int main()
{
    int N = 10000;
    Eigen::MatrixXf *x = new Eigen::MatrixXf[N];
    Eigen::MatrixXf *y = new Eigen::MatrixXf[N];
    Eigen::MatrixXf *z = new Eigen::MatrixXf[N];
    // initialize x and y arrays on the host
    for (int i = 0; i < N; i++) {
        x[i] = Eigen::MatrixXf::Random(100,100);
        y[i] = Eigen::MatrixXf::Random(100,100);
    }
    for (int i = 0; i < N; i++) {
	z[i] = x[i] * y[i];
    }
}
