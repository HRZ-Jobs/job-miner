from extract.job_extractor import IJobExtractor

from app.url_builder import URLBuilder

class InfoJobsExtractor(IJobExtractor):

    def build_url(self, vacancy):
        builder = URLBuilder("https://www.infojobs.com.br/empregos.aspx")
        builder.vacancy(f"palabra={builder.__quote_str__(vacancy)}")
        
        return builder.build()

    def extract_jobs(self):
        return super().extract_jobs()
        