#include <iostream>
#include <vector>
#include <math.h>
#include <time.h>

using namespace std;

bool perfectSquare(unsigned long int n){
	bool perfect_square = true;
	double root_n= sqrt(n);
	if (fmod(root_n, 1) != 0)perfect_square = false;
	return perfect_square;
}

int main(){
	float start = clock();
	unsigned long int N = 10000000000;
	unsigned long int x, y, z;
	int found = 0;
	int xyzsum = 0;
	for(z=1; z*z<N; z++){
		for(y=z+1; y*y<N; y++){
			int ypz = perfectSquare(y+z);
			int ymz = perfectSquare(y-z);
			if(ypz == 0 || ymz == 0)continue;
			for(x=y+1; x*x<N; x++){
				int xpy = perfectSquare(x+y);
				int xmy = perfectSquare(x-y);
				if(xpy == 0 || xmy ==0)continue;
				int xpz = perfectSquare(x+z);
				int xmz = perfectSquare(x-z);
				
				if(xpy!=0 && xmy!=0 && xpz!=0 && xmz!=0 && ypz!=0 && ymz!=0){
					xyzsum = x + y + z;
					cout << "x:= " << x << " y:= " << y << " z:= " << z << endl;
					found++;
				}
			}		
		}
	}
	cout << "Found: " << found << endl;
	cout << "Total run time: " << (clock() - start)/CLOCKS_PER_SEC << "sec" << endl;
	return 0;
}
