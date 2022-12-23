from abc import ABCMeta, abstractmethod
import json


class User:
  def __init__(self, name):
    self.name = name


class AdminUser(User):
  def be_represented_by(self, serializer):
    return serializer.represent_admin_user(self)


class TrialUser(User):
  def be_represented_by(self, serializer):
    return serializer.represent_trial_user(self)



class Representer(metaclass=ABCMeta):
  def represent(self, user):
    return user.be_represented_by(self)

  @abstractmethod
  def represent_admin_user(self, user):
    pass

  @abstractmethod
  def represent_trial_user(self, user):
    pass


class JsonRepresenter(Representer):
  def represent_admin_user(self, user):
    return json.dumps({
      "admin": True,
      "name": user.name,
    })

  def represent_trial_user(self, user):
    return json.dumps({
      "trial": True,
      "name": user.name,
    })


class StringRepresenter(Representer):
  def represent_admin_user(self, user):
    return '<<{}>>'.format(user.name)

  def represent_trial_user(self, user):
    return '[TRIAL] {}'.format(user.name)


user = AdminUser('Homer')
representer = JsonRepresenter()

for user in AdminUser('Homer'), TrialUser('Bart'):
  for representer in JsonRepresenter(), StringRepresenter():
    print(representer.represent(user))
