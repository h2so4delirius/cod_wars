#include<vector>
#include<iostream>
using namespace std;

int score(const vector<int>& dice) {
  vector<int>num = {0,0,0,0,0,0};
  int res = 0;
  for(auto i:dice){
      num[i-1]++;
  }
  for(int i = 0;i < 6;i++){
      int pop1 = num[i] % 3;
      int pop2 = num[i] / 3;
      if(i != 0){
          res += pop2 * (i + 1) * 100;
      }
      else{
          res += pop2 * 1000;
      }
      if(i == 0){
          res += pop1 * 100;
      }
      if(i == 4){
          res += pop1 * 50;
      }
  }
    return res;
}



int main(){
    cout<<score({2, 3, 4, 6, 2})<<endl;
    cout<<score({2, 4, 4, 5, 4})<<endl;
    return 0;
}
