class User {
  // ...
}

class AdminUser extends User {
  // ...
}

class TrialUser extends User {
  // ...
}

interface Representer {
  public String represent(AdminUser user);
  public String represent(TrialUser user);
}

class JsonRepresenter implements Representer {
  public String represent(AdminUser user) {
    return "a";
  }

  public String represent(TrialUser user) {
    return "b";
  }
}

class StringRepresenter implements Representer {
  public String represent(AdminUser user) {
    return "c";
  }

  public String represent(TrialUser user) {
    return "d";
  }
}

class Main {
  void main(string[] args) {
    User user = new AdminUser();
    Representer representer = new JsonRepresenter();

    representer.represent(user);
  }
}
