#include <iostream>

#define DEFINE_NAME true

int main ()
{
  char *name;
  if (DEFINE_NAME)
    {
      name = (char *) "Name";
      std::cout << "Hello, " << name << "!";
    }
  else
    {
      std::cout << "Hello World!";
    }
  return 0;
}
