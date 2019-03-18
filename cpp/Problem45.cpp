#include <iostream>
#include <math.h>

using namespace std;

bool isTriangular(unsigned long int num){
	bool triangular = false;
	double sol = (-1 + sqrt(1 + 8*num))/2.0;
	double intOrNot = fmod(sol, 1.0);
	if (intOrNot == 0.0){
		triangular = true;
	}
	return triangular;
}

bool isPentagonal(unsigned long int num){
	bool pentagonal = false;
	double sol = (1 + sqrt(1 + 24*num))/6.0;
	double intOrNot = fmod(sol, 1.0);
	if (intOrNot == 0.0){
		pentagonal = true;
	}
	return pentagonal;
}

bool isHexagonal(unsigned long int num){
	bool hexagonal = false;
	double sol = (1 + sqrt(1 + 8*num))/4.0;
	double intOrNot = fmod(sol, 1.0);
	if (intOrNot == 0.0){
		hexagonal = true;
	}
	return hexagonal;
}

int main() {
	int count = 0;
	unsigned long int i = 1;
	while(count != 3){
		if (isTriangular(i)!=0 && isPentagonal(i)!=0 && isHexagonal(i)!=0){
			cout << "Tn = Pn = Hn: " << i << endl;
			count ++;
		}
		i++;	
	}
	//Checking the answer again.
	unsigned long int ans = 1533776805;
	cout << "Check the num: " << isTriangular(ans) << "\t" << isPentagonal(ans) << "\t" << isHexagonal(ans) << endl;
	return 0;
}
