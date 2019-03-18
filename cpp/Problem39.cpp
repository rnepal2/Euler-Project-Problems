#include <iostream>
#include <vector>
#include <math.h>
#include <time.h>

using namespace std;

static inline bool right_triangle(vector<int> &triangle){
	bool is_right_triangle = false;
	int a = triangle[0];
	int b = triangle[1];
	int c = triangle[2];
	if(a<b+c && b<c+a && c<a+b){
		if(a*a == b*b + c*c || b*b == a*a + c*c || c*c == a*a + b*b){
			is_right_triangle = true;
		}
	}
	return is_right_triangle;
}

int right_traingle_for_n(int perimeter){
	int count = 0;
	for (int i=1; i<perimeter/2; i++){
		for (int j=i; j<perimeter/2; j++){
			int k = perimeter - i - j;
			vector<int> new_triangle(3);
			new_triangle[0] = i;
			new_triangle[1] = j;
			new_triangle[2] = k;
			if (right_triangle(new_triangle) != 0)count++;
			new_triangle.resize(3); //resetting the triangle.
		}
	}
	return (int)count/3; // there will be repeations in the ans.
}
	
int main(){
	float start_time = clock();
	int max_perimeter = 1000;
	int count = 0;
	int number;
	for (int i=0; i<=max_perimeter; i+=2){
		int new_count = right_traingle_for_n(i);
		if (new_count > count){
			count = new_count;
			number = i;
		}
	}
	cout << "The number is: " << number << " and total number of right triangles are: " << count << endl;
	float final_time = clock();
	cout << "Total run time is: " << (final_time-start_time)/CLOCKS_PER_SEC << "sec" << endl;
    return 0;
}
