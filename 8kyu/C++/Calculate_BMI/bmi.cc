# include <string>
# include <iostream>

using namespace std;

string bmi(double w, double h) {
	double d_bmi = w/h/h;
	double typec = (int)(d_bmi * 100 + .5);
	double fin = typec / 100;
	cout << d_bmi << endl;
	if (fin <= 18.5) {
		return "Underweight";
	} else if (fin <= 25.0) {
		return "Normal";
	} else if (fin <= 30.0) {
		return "Overweight";
	} else if (fin > 30) {
		return "Obese";
	}
}

int main() {
	double w = 86.7, h = 1.7;
	cout << bmi(w, h) << endl;
	return 0;
}
