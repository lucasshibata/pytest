from abc import ABC, abstractmethod
class FormaGeometrica(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimetro(self):
        pass
    @abstractmethod
    def mensagem(self):
        pass

if __name__ == "__main__":
    # obj_form = FormaGeometrica() --------- não pode fazer isso