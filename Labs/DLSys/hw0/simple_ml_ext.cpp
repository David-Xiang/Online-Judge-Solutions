#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <cmath>
#include <iostream>

namespace py = pybind11;

void mat_copy_rows_float(const float *in, float *out, size_t m_start,
                         size_t m_end, size_t n) {
    for (size_t i = m_start; i < m_end; ++i) {
        for (size_t j = 0; j < n; ++j) {
            out[(i - m_start) * n + j] = in[i * n + j];
        }
    }
}

void mat_copy_rows_uchar(const unsigned char *in, unsigned char *out,
                         size_t m_start, size_t m_end, size_t n) {
    for (size_t i = m_start; i < m_end; ++i) {
        for (size_t j = 0; j < n; ++j) {
            out[(i - m_start) * n + j] = in[i * n + j];
        }
    }
}

void mat_multiply(const float *in1, const float *in2, float *out, size_t m,
                  size_t n, size_t p) {
    for (size_t i = 0; i < m; ++i) {
        for (size_t j = 0; j < p; ++j) {
            out[i * p + j] = 0;
            for (size_t k = 0; k < n; ++k) {
                out[i * p + j] += in1[i * n + k] * in2[k * p + j];
            }
        }
    }
}

void mat_softmax_inplace(float *in, size_t m, size_t n) {
    for (size_t i = 0; i < m; ++i) {
        float sum = 0;
        for (size_t j = 0; j < n; ++j) {
            sum += exp(in[i * n + j]);
        }
        for (size_t j = 0; j < n; ++j) {
            in[i * n + j] = exp(in[i * n + j]) / sum;
        }
    }
}

void mat_eye(const unsigned char *in, float *out, size_t m, size_t n) {
    // in: m * 1
    // out: m * n
    std::fill(out, out + m * n, 0.0f);
    for (size_t i = 0; i < m; ++i) {
        out[i * n + in[i]] = 1.0f;
    }
}

void mat_transpose(const float *in, float *out, size_t m, size_t n) {
    for (size_t i = 0; i < m; ++i) {
        for (size_t j = 0; j < n; ++j) {
            out[j * m + i] = in[i * n + j];
        }
    }
}

void mat_sub_inplace(float *in1, float *in2, size_t m, size_t n) {
    for (size_t i = 0; i < m; ++i) {
        for (size_t j = 0; j < n; ++j) {
            in1[i * n + j] -= in2[i * n + j];
        }
    }
}

void mat_multiply_scalar_inplace(float *in, float scalar, size_t m, size_t n) {
    for (size_t i = 0; i < m; ++i) {
        for (size_t j = 0; j < n; ++j) {
            in[i * n + j] *= scalar;
        }
    }
}

void print_mat_float(const float *in, size_t m, size_t n) {
    for (size_t i = 0; i < m; ++i) {
        for (size_t j = 0; j < n; ++j) {
            std::cout << in[i * n + j] << " ";
        }
        std::cout << std::endl;
    }
}

void print_mat_uchar(const unsigned char *in, size_t m, size_t n) {
    for (size_t i = 0; i < m; ++i) {
        for (size_t j = 0; j < n; ++j) {
            std::cout << in[i * n + j] - 0 << " ";
        }
        std::cout << std::endl;
    }
}

void softmax_regression_epoch_cpp(const float *X, const unsigned char *y,
                                  float *theta, size_t m, size_t n, size_t k,
                                  float lr, size_t batch) {
    /**
     * A C++ version of the softmax regression epoch code.  This should run a
     * single epoch over the data defined by X and y (and sizes m,n,k), and
     * modify theta in place.  Your function will probably want to allocate
     * (and then delete) some helper arrays to store the logits and gradients.
     *
     * Args:
     *     X (const float *): pointer to X data, of size m*n, stored in row
     *          major (C) format
     *     y (const unsigned char *): pointer to y data, of size m
     *     theta (float *): pointer to theta data, of size n*k, stored in row
     *          major (C) format
     *     m (size_t): number of examples
     *     n (size_t): input dimension
     *     k (size_t): number of classes
     *     lr (float): learning rate / SGD step size
     *     batch (int): SGD minibatch size
     *
     * Returns:
     *     (None)
     */
    size_t batches = ceil(m * 1.0 / batch);
    for (size_t i = 0; i < batches; ++i) {
        size_t row_start = i * batch;
        size_t row_end = fmin((i + 1) * batch, m);
        size_t instances = row_end - row_start;

        float X_b[instances * n];
        unsigned char y_b[instances];

        mat_copy_rows_float(X, X_b, row_start, row_end, n);
        mat_copy_rows_uchar(y, y_b, row_start, row_end, 1);

        float Z_b[instances * k];
        mat_multiply(X_b, theta, Z_b, instances, n, k);
        mat_softmax_inplace(Z_b, instances, k);

        float I_b[instances * k];
        mat_eye(y_b, I_b, instances, k);

        float X_b_t[n * instances];
        float gradient[n * k];
        mat_transpose(X_b, X_b_t, instances, n);
        mat_sub_inplace(Z_b, I_b, instances, k);
        mat_multiply(X_b_t, Z_b, gradient, n, instances, k);
        mat_multiply_scalar_inplace(gradient, lr / batch, n, k);
        mat_sub_inplace(theta, gradient, n, k);
    }
}


/**
 * This is the pybind11 code that wraps the function above.  It's only role is
 * wrap the function above in a Python module, and you do not need to make any
 * edits to the code
 */
PYBIND11_MODULE(simple_ml_ext, m) {
    m.def("softmax_regression_epoch_cpp",
    	[](py::array_t<float, py::array::c_style> X,
           py::array_t<unsigned char, py::array::c_style> y,
           py::array_t<float, py::array::c_style> theta,
           float lr,
           int batch) {
        softmax_regression_epoch_cpp(
        	static_cast<const float*>(X.request().ptr),
            static_cast<const unsigned char*>(y.request().ptr),
            static_cast<float*>(theta.request().ptr),
            X.request().shape[0],
            X.request().shape[1],
            theta.request().shape[1],
            lr,
            batch
           );
    },
    py::arg("X"), py::arg("y"), py::arg("theta"),
    py::arg("lr"), py::arg("batch"));
}
