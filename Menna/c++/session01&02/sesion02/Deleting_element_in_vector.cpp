int main() {

  std::vector<int> vect{1,5,4,8,9,12};
  
  int no;

    std::cout<<"enter the no. you want to delete : "<<std::endl;
    std::cin>>no;

    std::cout<<"///////////////////////"<<std::endl;

    for(int i=0;i<vect.size();i++)
    {
      if(no==vect[i])
      {
        vect.erase(vect.begin()+i);  //using index of element
      }
    }
    for(int i : vect)
      std::cout<<i<<std::endl;
    
    return 0;
}
