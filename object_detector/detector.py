
import descriptor
#import classifier

class Detector(object):
    
    def __init__(self, descriptor=descriptor.HOG(), classifier):
        self._descriptor = descriptor
        self._classifier = classifier

    def describe(self):
        pass

    def train(self):
        pass
    
    def predict(self):
        pass


# Todo : Abstract Factory�� detector / classifier �� create �غ���. 
class HogSvmDetector(Detector):
    def __init__(self):
        self._descriptor = descriptor.HOG()
        self._classifier = None
    
    def describe(self):
        pass

    def train(self):
        pass
    
    def predict(self):
        pass

