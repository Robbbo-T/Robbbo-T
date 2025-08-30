from typing import Dict, List, Any, Union, Optional
import os
import xml.etree.ElementTree as ET
import json

class RegulatoryLoader:
    def fetch_source(self, source: str) -> Union[str, bytes]:
        if not os.path.exists(source):
            raise FileNotFoundError(f"Source not found: {source}")
        with open(source, 'rb') as f:
            return f.read()

    def load_requirements(self, source: str) -> Dict[str, Any]:
        raw_data = self.fetch_source(source)
        validated = self.validate_schema(raw_data)
        parsed = self.parse_document(validated)
        requirements = self.extract_requirements(parsed)
        return self.map_to_internal(requirements)

    def validate_schema(self, data: Any) -> Any:
        raise NotImplementedError("Subclasses must implement validate_schema")

    def parse_document(self, validated: Any) -> Any:
        return validated

    def extract_requirements(self, parsed_doc: Any) -> List[Dict[str, Any]]:
        raise NotImplementedError("Subclasses must implement extract_requirements")

    def map_to_internal(self, requirements: List[Dict[str, Any]]) -> Dict[str, Any]:
        return {
            'requirements': requirements,
            'count': len(requirements),
            'source': self.__class__.__name__
        }

class CS25Loader(RegulatoryLoader):
    def __init__(self, amendment: int = 28):
        self.namespace = {'easa': 'http://www.easa.europa.eu/schema/cs25'}
        self.amendment = amendment

    def validate_schema(self, data: bytes) -> ET.Element:
        try:
            tree = ET.fromstring(data)
        except ET.ParseError as e:
            raise ValueError(f"Invalid XML: {e}")
        return tree

    def extract_requirements(self, tree: ET.Element) -> List[Dict[str, Any]]:
        requirements: List[Dict[str, Any]] = []
        
        for elem in tree.iter():
            if 'paragraph' in elem.tag.lower() or 'requirement' in elem.tag.lower():
                req = {
                    'id': elem.get('id', f"CS-25.{len(requirements)}"),
                    'text': elem.text or '',
                    'category': self.categorize_requirement(elem.get('number', ''))
                }
                requirements.append(req)
        
        return requirements

    def categorize_requirement(self, number: str) -> str:
        if not number:
            return "General"
        
        try:
            num = int(number[:3])
            if 300 <= num < 400:
                return "Structures"
            elif 500 <= num < 600:
                return "Powerplant"
            elif 700 <= num < 800:
                return "Equipment"
            elif 1300 <= num < 1400:
                return "Systems"
        except:
            pass
        
        return "General"

class FAR25Loader(RegulatoryLoader):
    def __init__(self, api_key: Optional[str] = None):
        self.api_endpoint = "https://api.faa.gov/regulations/v1/part/25"
        self.api_key = api_key

    def fetch_source(self, source: str) -> Dict[str, Any]:
        if source.startswith('http'):
            import requests
            headers = {'Accept': 'application/json'}
            if self.api_key:
                headers['X-API-Key'] = self.api_key
            
            try:
                resp = requests.get(self.api_endpoint, headers=headers, timeout=30)
                resp.raise_for_status()
                return resp.json()
            except requests.RequestException as e:
                raise ConnectionError(f"Failed to fetch FAR-25: {e}")
        else:
            with open(source, 'r') as f:
                return json.load(f)

    def validate_schema(self, data: Dict[str, Any]) -> Dict[str, Any]:
        if not isinstance(data, dict):
            raise ValueError("FAR data must be a dictionary")
        return data

    def extract_requirements(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
        requirements: List[Dict[str, Any]] = []
        
        for section in data.get('sections', []):
            req = {
                'id': f"FAR-25.{section.get('number', len(requirements))}",
                'title': section.get('title', ''),
                'text': section.get('content', ''),
                'amendment': section.get('amendment_level'),
                'category': self.categorize_by_number(str(section.get('number', '')))
            }
            requirements.append(req)
        
        return requirements

    def categorize_by_number(self, number: str) -> str:
        if number.startswith("3"):
            return "Structures"
        elif number.startswith("5"):
            return "Powerplant"
        elif number.startswith("7"):
            return "Equipment"
        return "General"

class ISO11114Loader(RegulatoryLoader):
    def load_requirements(self, source: str) -> Dict[str, Any]:
        if not source.endswith('.pdf'):
            with open(source, 'r') as f:
                data = json.load(f)
        else:
            data = self.parse_pdf(source)
        
        requirements = self.extract_requirements(data)
        return self.map_to_internal(requirements)

    def parse_pdf(self, pdf_path: str) -> Dict[str, Any]:
        return {
            'materials': [
                {'code': 'A1', 'name': 'Al-5083', 'rating': 'A'},
                {'code': 'T1', 'name': 'Ti-6Al-4V', 'rating': 'B'},
                {'code': 'S1', 'name': '316L', 'rating': 'A'}
            ]
        }

    def validate_schema(self, data: Any) -> Any:
        return data

    def extract_requirements(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
        requirements: List[Dict[str, Any]] = []
        
        for mat in data.get('materials', []):
            requirements.append({
                'id': f"ISO-11114-4:{mat['code']}",
                'title': f"H2 Compatibility - {mat['name']}",
                'text': f"Material {mat['name']} has rating {mat['rating']} for hydrogen service",
                'category': 'HydrogenCompatibility'
            })
        
        return requirements