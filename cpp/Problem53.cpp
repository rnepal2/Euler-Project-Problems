#include <iostream>
#include <string>
#include <vector>
#include <math.h>


double factorial(int n){
  if (n==0 || n==1) {
    return 1;
  }else{
  return (double)(n*factorial(n-1));
 }
}

// binomial combinations
inline double nCr(int n, int r){
  return (double)factorial(n)/(factorial(n-r)*factorial(r));
}

int main(){

  double million = 1000000.0;
  int count = 0;
  for (int r=1; r<=100; r++){
    for(int n=r; n<=100; n++){
      double ncr = nCr(n, r);
      if (ncr > million){
        count += 1;
      }
    }
  }

  cout << "Number of combinations above million are: " << count << endl;
  return 0;
}
