# regulatory/loaders.py
from typing import Dict, List, Any, Union, Optional
import os
import xml.etree.ElementTree as ET
import json

class RegulatoryLoader:
    """Base class for loading regulatory requirements"""
    
    def fetch_source(self, source: str) -> Union[str, bytes]:
        """Default fetch: read from local file"""
        if not os.path.exists(source):
            raise FileNotFoundError(f"Source not found: {source}")
        with open(source, 'rb') as f:
            return f.read()

    def load_requirements(self, source: str) -> Dict[str, Any]:
        """Main loading pipeline"""
        raw_data = self.fetch_source(source)
        validated = self.validate_schema(raw_data)
        parsed = self.parse_document(validated)
        requirements = self.extract_requirements(parsed)
        return self.map_to_internal(requirements)

    def validate_schema(self, data: Any) -> Any:
        """Override in subclasses"""
        raise NotImplementedError("Subclasses must implement validate_schema")

    def parse_document(self, validated: Any) -> Any:
        """Default pass-through"""
        return validated

    def extract_requirements(self, parsed_doc: Any) -> List[Dict[str, Any]]:
        """Override in subclasses"""
        raise NotImplementedError("Subclasses must implement extract_requirements")

    def map_to_internal(self, requirements: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Map to internal format"""
        return {
            'requirements': requirements,
            'count': len(requirements),
            'source': self.__class__.__name__
        }

class CS25Loader(RegulatoryLoader):
    """Loader for EASA CS-25 requirements"""
    
    def __init__(self, amendment: int = 28):
        self.namespace = {'easa': 'http://www.easa.europa.eu/schema/cs25'}
        self.amendment = amendment

    def validate_schema(self, data: bytes) -> ET.Element:
        """Validate CS-25 XML format"""
        try:
            tree = ET.fromstring(data)
        except ET.ParseError as e:
            raise ValueError(f"Invalid XML: {e}")
        
        # For now, accept any XML - real implementation would check schema
        return tree

    def extract_requirements(self, tree: ET.Element) -> List[Dict[str, Any]]:
        """Extract CS-25 requirements"""
        requirements: List[Dict[str, Any]] = []
        
        # Simplified extraction - real implementation would use proper XPATH
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
        """Categorize by CS-25 paragraph number"""
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
    """Loader for FAA FAR Part 25"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_endpoint = "https://api.faa.gov/regulations/v1/part/25"
        self.api_key = api_key

    def fetch_source(self, source: str) -> Dict[str, Any]:
        """Fetch from FAA API or local file"""
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
            # Load from local JSON file
            with open(source, 'r') as f:
                return json.load(f)

    def validate_schema(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Validate FAR JSON structure"""
        if not isinstance(data, dict):
            raise ValueError("FAR data must be a dictionary")
        
        required_keys = ['regulations', 'part']
        for key in required_keys:
            if key not in data:
                raise ValueError(f"Missing required key: {key}")
        
        return data

    def extract_requirements(self, data: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Extract FAR-25 requirements from JSON"""
        requirements: List[Dict[str, Any]] = []
        
        regulations = data.get('regulations', [])
        for reg in regulations:
            if reg.get('part') == '25':
                sections = reg.get('sections', [])
                for section in sections:
                    req = {
                        'id': f"FAR-25.{section.get('number', len(requirements))}",
                        'text': section.get('text', ''),
                        'category': self.categorize_far_requirement(section.get('number', ''))
                    }
                    requirements.append(req)
        
        return requirements

    def categorize_far_requirement(self, number: str) -> str:
        """Categorize FAR-25 requirements by section number"""
        if not number:
            return "General"
        
        try:
            num = int(number)
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