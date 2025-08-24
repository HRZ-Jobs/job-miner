from extract.modules.infojobs_extractor import InfoJobsExtractor

url = InfoJobsExtractor().build_url(vacancy='cientista de dados')
print(url)