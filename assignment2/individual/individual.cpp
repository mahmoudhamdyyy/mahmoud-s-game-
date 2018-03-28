#include<iostream>

using namespace std;

int main()
{
int weight, height, age, candym, candyf, candy,bmrm, bmrf;
string M, F, gender;
     candy = 230;
cout << "To calculate BMR enter the following: \n";
cout << "Enter his or her weight in pounds: ";
cin >> weight;
cout << " Enter height in inches: ";
 cin >> height;
cout << " Enter age in years: ";
 cin >> age;
cout << " Enter M for male or F for female: ";
 cin >> gender;
bmrf = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age);
bmrm = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age);
     candyf = (bmrf / candy);
     candym = (bmrm / candy);
     if(gender == "m")
     {
         cout << "As a male you need to typically eat about " << candym
                 << " candy bars to maintain your weight";
     }
     else if(gender == "f")
     {
         cout << "As a female you need to typically eat about " << candyf
                 << " candy bars to maintain your weight";
     }
     else
     {
         cout << "Invalid input. ";
     }















}

