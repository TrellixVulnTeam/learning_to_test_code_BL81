from scripts.gists.oop.abstract_factory import Pet, Dog, Cat, PetShop, random_animal


class ConcreteExample(Pet):
    def speak(self):
        raise NotImplementedError
    

class TestPetShop:
    def test_returns_1(self):
        example = ConcreteExample("dummy_name")
        assert example.concrete_method() == True