#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <Eigen/Dense>

namespace py = pybind11;
using namespace Eigen;

// double sum(double a, double b) {
//     return a + b;
//  }

// PYBIND11_MODULE(svd_module, m) {
//     m.def("sum", &sum, "Compute SVD using Eigen");
// }
// Compute SVD function
std::tuple<py::array_t<double>, py::array_t<double>, py::array_t<double>> compute_svd(py::array_t<double> input) {
    // Convert input numpy array to Eigen matrix
    py::buffer_info buf = input.request();
    int rows = buf.shape[0];
    int cols = buf.shape[1];
    auto ptr = static_cast<double *>(buf.ptr);
    Map<MatrixXd> A(ptr, rows, cols);

    // Compute SVD
    JacobiSVD<MatrixXd> svd(A, ComputeFullU | ComputeFullV);
    MatrixXd U = svd.matrixU();
    MatrixXd S = svd.singularValues().asDiagonal();
    MatrixXd V = svd.matrixV();

    return std::make_tuple(
        py::array_t<double>({rows, rows}, U.data()),  // U matrix
        py::array_t<double>({rows, cols}, S.data()),  // S diagonal matrix
        py::array_t<double>({cols, cols}, V.data())   // V matrix
    );
}

// Define module
PYBIND11_MODULE(svd_module, m) {
    m.def("compute_svd", &compute_svd, "Compute SVD using Eigen");
}