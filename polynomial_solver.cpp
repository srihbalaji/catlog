#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

// Function to calculate the Lagrange interpolation polynomial
double lagrangeInterpolation(const vector<double>& x, const vector<double>& y, double xValue) {
    double result = 0.0;
    int n = x.size();
    
    for (int i = 0; i < n; i++) {
        double term = y[i];
        
        for (int j = 0; j < n; j++) {
            if (i != j) {
                term *= (xValue - x[j]) / (x[i] - x[j]);
            }
        }
        
        result += term;
    }
    
    return result;
}

int main() {
    // Example input: (x, y) pairs representing the roots
    vector<double> x = {1, 2, 3}; // Example x values
    vector<double> y = {4, 7, 12}; // Example y values (constant terms corresponding to x)

    // Calculate the constant term using Lagrange interpolation at x = 0
    double c = lagrangeInterpolation(x, y, 0);

    // Output the constant term
    cout << "Constant term (c) of the polynomial is: " << c << endl;

    return 0;
}
