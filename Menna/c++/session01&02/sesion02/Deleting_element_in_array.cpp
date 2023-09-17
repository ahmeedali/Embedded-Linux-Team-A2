int main() {

  std::array<int,5> arr={1,2,3,4,5};

  std::cout<<"enter the no. you want to delete : "<<std::endl;

  int no;

  std::cin>>no;
  std::cout<<"///////////////////////"<<std::endl;

  for(int i=0;i<5;i++){
    if(arr[i]==no)
    {
       for(int j=i;j<5;j++)
       {
        arr[j]=arr[j+1];
       }
    }else
    {
        std::cout<<"no is not in the array"<<std::endl; 
    }
  }
     for(int i : arr)
       std::cout<<i<<std::endl;

    return 0;
}
