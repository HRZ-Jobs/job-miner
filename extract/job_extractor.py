from abc import ABC, abstractmethod

from app.url_builder import URLBuilder

class IJobExtractor(ABC):

    @abstractmethod
    def build_url(self) -> URLBuilder:
        pass

    @abstractmethod
    def extract_jobs(self):
        pass
