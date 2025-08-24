from abc import ABC, abstractmethod

class IJobExtractor(ABC):

    @abstractmethod
    def extract_job(self):
        pass
