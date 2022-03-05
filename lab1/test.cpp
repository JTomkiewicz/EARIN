#include <chrono>
#include <cmath>
#include <iostream>
#include <vector>

void gradientDescent(const double *x, const double *y, const size_t n) {
  double a_curr, b_curr, c_curr, d_curr;
  a_curr = b_curr = c_curr = d_curr = 1.567812;
  size_t iterations = 500000;
  double learning_rate = 0.0000005;
  double cost_rising = 0;
  double cost = __FLT_MAX__;
  double y_predicted[n];
  double new_cost = 0;
  double ad, bd, cd, dd;
  size_t i;

  auto start = std::chrono::high_resolution_clock::now();
  std::cout << "Start computation of gradient dexcent\n";
  for (i = 0; i < iterations; i++) {
    ad = bd = cd = dd = 0;
    new_cost = 0;
    for (size_t it = 0; it < n; it++) {
      y_predicted[it] = a_curr * pow(x[it], 3) + b_curr * pow(x[it], 2) +
                        c_curr * x[it] + d_curr;
      new_cost += pow(y[it] - y_predicted[it], 2);
      ad += pow(x[it], 3) * (y[it] - y_predicted[it]);
      bd += pow(x[it], 2) * (y[it] - y_predicted[it]);
      cd += x[it] * (y[it] - y_predicted[it]);
      dd += y - y_predicted;
    }
    new_cost = new_cost / (float)n;
    ad = -(2 / (float)n) * ad;
    bd = -(2 / (float)n) * bd;
    cd = -(2 / (float)n) * cd;
    dd = -(2 / (float)n) * dd;
    // if (new_cost > cost) {
    //   cost_rising += 1;
    //   if (cost_rising > 10) {
    //     std::cout << "cost is rising istead of decresing, breaking the
    //     loop\n"; break;
    //   }
    // }
    cost = new_cost;
    if (cost < 0.1) {
      std::cout << "cost value low enough, breaking the loop\n";
      break;
    }
    a_curr = a_curr - learning_rate * ad;
    b_curr = b_curr - learning_rate * bd;
    c_curr = c_curr - learning_rate * cd;
    d_curr = d_curr - learning_rate * dd;
  }
  auto stop = std::chrono::high_resolution_clock::now();
  std::cout << "computation time :"
            << (float)std::chrono::duration_cast<std::chrono::microseconds>(
                   stop - start)
                       .count() /
                   (float)1000000
            << '\n';
  std::cout << "a_curr = " << a_curr << ", b_curr = " << a_curr
            << ", c_curr = " << a_curr << ", d_curr = " << a_curr
            << ", cost = " << cost << ", iters :" << i << '\n';
}

// char *expectedY(const char *x, const float a, const float b, const float c,
//                 const float d, const size_t n) {
//   char y[n];
//   for (size_t i = 0; i < n; i++) {
//     y[i] = a * pow(x[i], 3) + b * pow(x[i], 2) + c * x[i] + d;
//   }
//   return y;
// }

int main() {
  double a, b, c, d;
  a = 0.1;
  b = -0.5;
  c = -3;
  d = 11;
  double x[18] = {-2,  1.8, 1.6,  1, 4,   1, -0.7, -0.2, -0,
                  0.5, -1,  -1.5, 2, 2.5, 3, 10,   -10,  -0.4};
  double y[18];
  for (size_t i = 0; i < 18; i++) {
    y[i] = a * pow(x[i], 3) + b * pow(x[i], 2) + c * x[i] + d;
  }
  gradientDescent(x, y, 18);
  return 0;
}