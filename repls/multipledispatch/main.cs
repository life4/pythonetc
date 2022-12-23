using System;

class User {
  // ...
}

class AdminUser : User {
  // ...
}

class TrialUser : User {
  // ...
}

interface Representer {
  String represent(AdminUser user);
  String represent(TrialUser user);
}

class JsonRepresenter : Representer {
  public String represent(AdminUser user) {
    return "a";
  }

  public String represent(TrialUser user) {
    return "b";
  }
}

class StringRepresenter : Representer {
  public String represent(AdminUser user) {
    return "c";
  }

  public String represent(TrialUser user) {
    return "d";
  }
}



class MainClass {
  public static void Main (string[] args) {
    // `dynamic` keyword tells C#
    // to postpone method selection until runtime
    dynamic user = new AdminUser();
    Representer representer = new JsonRepresenter();

    Console.WriteLine(representer.represent(user));
  }
}
