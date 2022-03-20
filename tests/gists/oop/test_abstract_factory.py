from numpy import isin
from scripts.gists.oop.abstract_factory import Pet, Dog, Cat, PetShop, random_animal


class ConcreteExample(Pet):
    def speak(self):
        raise NotImplementedError
    

class TestPetShop:
    def test_returns_1(self):
        example = ConcreteExample("dummy_name")
        assert example.concrete_method() == True
        
    def test_init_cat_shop_ok(self):
        cat_shop = PetShop(Cat)
        assert cat_shop.pet_pactory is not None
        assert isinstance(cat_shop, PetShop) == True
        
    def test_init_dog_shop_ok(self):
        dog_shop = PetShop(Dog)
        assert dog_shop.pet_pactory is not None
        assert isinstance(dog_shop, PetShop) == True

