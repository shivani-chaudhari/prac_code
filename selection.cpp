#include <bits/stdcpp++.h>
using namespace std;

int main(){
    int n,i,j,min_idx,temp;
    cin>>n;

    int arr[n];
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }

    for(i=0;i<n-1;i++){
        min_idx=i;
        for(j=i+1;j<n;j++)
            if(arr[min_idx]>arr[j])
                min_idx=j;
            temp=arr[i];
            arr[i]=arr[min_idx];
            arr[min_idx]=temp;    
    }
    for(int i=0;i<n;i++)
        cout<<arr[i]<<"";
    return 0;
}