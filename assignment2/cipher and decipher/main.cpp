#include <bits/stdc++.h>

using namespace std;

int main()
{
char arr[27] ={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};
string ar[27]={"aaaaa","aaaab","aaaba","aaabb","aabaa","aabab","aabba","aabbb","abaaa","abaab","ababa","ababb","abbaa","abbab","abbba","abbbb","baaaa","baaab","baaba","baabb","babaa","babab","babba","babbb","bbaaa","bbaab"};
string s;
int z;
int decimal=0,counter=0;
while(true){
cout<<" Choose a number"<<endl;
cout<<"1-Cipher"<<endl;
cout<<"2-Decipher"<<endl;
cout<<"3-end"<<endl;
cin>>z ;
if(z==1){
  cout<<"ENTER THE MESSAGE"<<endl;
  cin>>s;
  for(int i=0;i<s.length();i++)
  {
      for(int j=0;j<26;j++)
      {
         if(s[i]==arr[j])
         {
             cout<<ar[j];


         }
      }
  }
cout<<endl; }
  else if(z==2)
  {
    cout<<"ENTER THE MESSAGE"<<endl;
     cin>>s;
     for(int i=1 ;i<=(int)s.size();i++)
     {
         if((s[i-1]=='b') || (s[i-1]=='a'))
         {
             if((s[i-1]=='b'))
             {
                 decimal=decimal+pow(2,4-counter);
             }
             if((i%5)==0)
             {
                 cout<<arr[decimal];
                 decimal=0;
             }
         }
       counter++;
       if(i%5==0)
       {
           counter=0;
       }
     }


  }
  else if (z==3)
  {
      break;
  }
}

    return 0;
}
