from dc_base_scrapers.xml_scraper import GmlScraper


stations_url = "https://mapsenc.east-northamptonshire.gov.uk/arcgis/services/elections/elections/MapServer/WFSServer?service=WFS&version=1.1.0&request=GetFeature&typeNames=elections_elections%3APolling_Stations"
stations_fields = {
    '{http://giscoresrv.east-northamptonshire.gov.uk:6080/arcgis/services/elections/elections/MapServer/WFSServer}OBJECTID': 'OBJECTID',
    '{http://giscoresrv.east-northamptonshire.gov.uk:6080/arcgis/services/elections/elections/MapServer/WFSServer}Name': 'Name',
    '{http://giscoresrv.east-northamptonshire.gov.uk:6080/arcgis/services/elections/elections/MapServer/WFSServer}Address': 'Address',
}

districts_url = "https://mapsenc.east-northamptonshire.gov.uk/arcgis/services/elections/elections/MapServer/WFSServer?service=WFS&version=1.1.0&request=GetFeature&typeNames=elections_elections%3APolling_Districts"
districts_fields = {
    '{http://giscoresrv.east-northamptonshire.gov.uk:6080/arcgis/services/elections/elections/MapServer/WFSServer}OBJECTID_1': 'OBJECTID_1',
    '{http://giscoresrv.east-northamptonshire.gov.uk:6080/arcgis/services/elections/elections/MapServer/WFSServer}Code_District': 'Code_District',
    '{http://giscoresrv.east-northamptonshire.gov.uk:6080/arcgis/services/elections/elections/MapServer/WFSServer}Website': 'Website',
    '{http://giscoresrv.east-northamptonshire.gov.uk:6080/arcgis/services/elections/elections/MapServer/WFSServer}PollingStation': 'PollingStation',
    '{http://giscoresrv.east-northamptonshire.gov.uk:6080/arcgis/services/elections/elections/MapServer/WFSServer}PollingStationAddress': 'PollingStationAddress',
    '{http://giscoresrv.east-northamptonshire.gov.uk:6080/arcgis/services/elections/elections/MapServer/WFSServer}Name': 'Name',
    '{http://giscoresrv.east-northamptonshire.gov.uk:6080/arcgis/services/elections/elections/MapServer/WFSServer}Address': 'Address',
    '{http://giscoresrv.east-northamptonshire.gov.uk:6080/arcgis/services/elections/elections/MapServer/WFSServer}Distance': 'Distance',
}

council_id = 'E07000152'


stations_scraper = GmlScraper(stations_url, council_id, 'stations', stations_fields, 'OBJECTID')
stations_scraper.scrape()
districts_scraper = GmlScraper(districts_url, council_id, 'districts', districts_fields, 'OBJECTID_1')
districts_scraper.scrape()
